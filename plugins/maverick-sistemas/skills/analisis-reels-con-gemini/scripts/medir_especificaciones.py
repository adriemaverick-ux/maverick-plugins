#!/usr/bin/env python3
"""Mide las especificaciones de diseño de Reels en pantalla dividida (sin IA, solo ffmpeg y Python estándar).
Uso: medir_especificaciones.py carpeta_de_videos salida.json
Devuelve por video y en conjunto (medianas): color de fondo, rojo de acento, caja de la cara (arriba/izquierda/derecha),
subtítulo (altura), titular (arriba y alto de línea) y duración de las ráfagas de movimiento.
Todas las posiciones son fracciones del alto/ancho del cuadro (0 a 1). Los videos deben ser 9:16 sin audio."""
import glob, json, os, statistics as st, subprocess, sys

FF = "/opt/homebrew/bin/ffmpeg"
W, H = 360, 640


def frames(path, fps, w, h, fmt):
    raw = subprocess.run([FF, "-nostdin", "-v", "error", "-i", path, "-an", "-vf", f"fps={fps},scale={w}:{h},format={fmt}",
                          "-f", "rawvideo", "-"], capture_output=True).stdout
    n_ch = 3 if fmt == "rgb24" else 1
    size = w * h * n_ch
    return [raw[i * size:(i + 1) * size] for i in range(len(raw) // size)]


def px(fr, x, y):
    i = (y * W + x) * 3
    return fr[i], fr[i + 1], fr[i + 2]


def lum(p):
    return 0.2126 * p[0] + 0.7152 * p[1] + 0.0722 * p[2]


def med(v):
    return st.median(v) if v else None


def runs(flags):
    out, s = [], None
    for i, f in enumerate(flags + [False]):
        if f and s is None:
            s = i
        if not f and s is not None:
            out.append((s, i - 1)); s = None
    return out


def analizar(path):
    fr = frames(path, 1, W, H, "rgb24")
    bg, red, tops, lefts, rights, subs, ttop, tline = [], [], [], [], [], [], [], []
    for f in fr:
        # fondo: píxeles oscuros de la zona del gráfico
        oscuros = [px(f, x, y) for y in range(int(H * .08), int(H * .55), 6) for x in range(4, W - 4, 6)]
        oscuros = [p for p in oscuros if lum(p) < 40]
        if len(oscuros) > 200:
            bg.append(tuple(int(med([p[k] for p in oscuros])) for k in range(3)))
        # acento rojo
        rojos = [px(f, x, y) for y in range(0, H, 4) for x in range(0, W, 4)]
        rojos = [p for p in rojos if p[0] > 170 and p[1] < 80 and p[2] < 100]
        if len(rojos) > 60:
            red.append(tuple(int(med([p[k] for p in rojos])) for k in range(3)))
        # ¿pantalla dividida? margen izquierdo (x≈2 %) oscuro a la altura de la cara y centro iluminado
        yb = int(H * .80)
        izq = lum(px(f, int(W * .04), yb))
        if izq > 10:
            continue
        # borde izquierdo y derecho de la caja a la altura yb
        fila = [lum(px(f, x, yb)) for x in range(W)]
        L = next((x for x in range(3, W // 2) if all(fila[x + k] > 18 for k in range(5))), None)
        R = next((x for x in range(W - 4, W // 2, -1) if all(fila[x - k] > 18 for k in range(5))), None)
        if L is None or R is None or not (0.03 < L / W < 0.12 and 0.88 < R / W < 0.97):
            continue
        # borde superior en una columna dentro de la caja (12 % del ancho desde el borde izquierdo)
        cx = L + int(W * .06)
        col = [lum(px(f, cx, y)) for y in range(H)]
        T = next((y for y in range(int(H * .60), int(H * .95)) if all(col[y + k] > 18 for k in range(6))), None)
        if T is None:
            continue
        lefts.append(L / W); rights.append(R / W); tops.append(T / H)
        # subtítulo: texto blanco entre el gráfico y la caja
        banda = range(int(H * .55), max(int(H * .55) + 5, T - 2))
        brillo = [sum(1 for x in range(int(W * .15), int(W * .85), 2) if lum(px(f, x, y)) > 225) for y in banda]
        rs = [r for r in runs([b > 4 for b in brillo]) if r[1] - r[0] >= 6]
        if rs:
            a, b = rs[-1]
            subs.append(((list(banda)[a] + list(banda)[b]) / 2) / H)
        # titular: texto blanco en la banda superior
        bt = range(int(H * .02), int(H * .22))
        brillo = [sum(1 for x in range(0, W, 2) if lum(px(f, x, y)) > 225) for y in bt]
        rs = [r for r in runs([b > 6 for b in brillo]) if r[1] - r[0] >= 6]
        if rs:
            ttop.append(list(bt)[rs[0][0]] / H)
            tline.append((rs[0][1] - rs[0][0] + 1) / H)
    # ráfagas de movimiento a 30 fps sobre la zona del gráfico (gris, 90x160)
    w2, h2 = 90, 160
    g = frames(path, 30, w2, h2, "gray")
    d = []
    for a, b in zip(g, g[1:]):
        s = 0
        for y in range(int(h2 * .10), int(h2 * .55)):
            o = y * w2
            s += sum(abs(a[o + x] - b[o + x]) for x in range(0, w2, 2))
        d.append(s / (int(h2 * .45) * (w2 // 2)))
    base = med(d) or 0
    umbral = max(0.35, base * 3)
    largos = [(r[1] - r[0] + 1) / 30 for r in runs([v > umbral for v in d]) if r[1] - r[0] >= 2]
    return dict(video=os.path.basename(path), cuadros=len(fr), fondo_rgb=med_rgb(bg), rojo_rgb=med_rgb(red),
                caja_izq=med(lefts), caja_der=med(rights), caja_arriba=med(tops), n_cuadros_split=len(tops),
                subtitulo_y=med(subs), titular_arriba=med(ttop), titular_alto_linea=med(tline),
                rafaga_s_mediana=med(largos), rafagas=len(largos))


def med_rgb(v):
    return [int(med([p[k] for p in v])) for k in range(3)] if v else None


def hexa(c):
    return "#%02X%02X%02X" % tuple(c) if c else None


if __name__ == "__main__":
    carpeta, salida = sys.argv[1], sys.argv[2]
    res = []
    for p in sorted(glob.glob(os.path.join(carpeta, "*.mp4"))):
        try:
            r = analizar(p)
        except Exception as e:  # un video dañado no detiene el lote
            r = dict(video=os.path.basename(p), error=str(e))
        print(r.get("video"), r.get("n_cuadros_split"), hexa(r.get("fondo_rgb")), hexa(r.get("rojo_rgb")), r.get("caja_arriba"), flush=True)
        res.append(r)
    ok = [r for r in res if r.get("n_cuadros_split")]
    resumen = {k: med([r[k] for r in ok if r.get(k) is not None]) for k in
               ["caja_izq", "caja_der", "caja_arriba", "subtitulo_y", "titular_arriba", "titular_alto_linea", "rafaga_s_mediana"]}
    for k in ["fondo_rgb", "rojo_rgb"]:
        v = [r[k] for r in res if r.get(k)]
        resumen[k] = hexa(med_rgb(v)) if v else None
        resumen[k + "_variantes"] = sorted({hexa(x) for x in v})[:30]
    resumen["videos_con_split_medido"] = len(ok)
    json.dump(dict(resumen=resumen, videos=res), open(salida, "w"), ensure_ascii=False, indent=1)
    print(json.dumps(resumen, ensure_ascii=False, indent=1))
