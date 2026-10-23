#!/usr/bin/env python3
"""Mide con ffmpeg (sin IA) el ritmo de edición de un Reel vertical de formato split:
- % de tiempo en layout split (zona superior clara) frente a cara completa (oscuro) y cuándo cambia;
- eventos visuales grandes por 10 s (cortes y entradas de gráficos, agrupados);
- cambios de la franja del subtítulo por segundo (aprox.).
Uso: medir_edicion.py video.mp4 [--ffmpeg /ruta/ffmpeg] [--json salida.json]
No usa IA ni red. Pensado para correr en lote sobre las grabaciones de pantalla recortadas (720x1280 o similar)."""
import argparse, json, re, subprocess, shutil, sys, statistics as st

def ff(a): return a.ffmpeg or shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"

def duracion(f, video):
    p = subprocess.run([f, "-hide_banner", "-i", video], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", p.stderr)
    return int(m[1])*3600 + int(m[2])*60 + float(m[3]) if m else 0.0

def tiempos(f, video, vf):
    p = subprocess.run([f, "-nostdin", "-v", "info", "-i", video, "-an", "-vf", vf + ",showinfo", "-f", "null", "-"], capture_output=True, text=True)
    return [float(x) for x in re.findall(r"pts_time:([0-9.]+)", p.stderr)]

def agrupa(ts, gap):
    ev = []
    for t in ts:
        if not ev or t - ev[-1] > gap: ev.append(t)
    return ev

def layout(f, video, fps=10):
    W, H = 18, 32
    p = subprocess.run([f, "-nostdin", "-v", "error", "-i", video, "-an", "-vf", f"fps={fps},scale={W}:{H},format=gray", "-f", "rawvideo", "-"], capture_output=True)
    b = p.stdout; n = len(b)//(W*H); filas = int(H*0.55)
    est = []
    for i in range(n):
        fr = b[i*W*H:(i+1)*W*H][:W*filas]
        est.append("split" if sum(fr)/len(fr) > 110 else "cara_completa")
    return est, fps

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("video"); ap.add_argument("--ffmpeg"); ap.add_argument("--json"); ap.add_argument("--umbral", type=float, default=0.12, help="sensibilidad de eventos visuales (0.03 detecta animaciones suaves)"); ap.add_argument("--zona-alto", type=float, default=1.0, help="fracción superior del cuadro donde medir eventos (0.5 = mitad de arriba)"); ap.add_argument("--sub-y0", type=float, default=0.652, help="inicio vertical de la franja del subtítulo (fracción)"); ap.add_argument("--sub-alto", type=float, default=0.0625)
    a = ap.parse_args(); f = ff(a); dur = duracion(f, a.video)
    est, fps = layout(f, a.video)
    cambios = [round(i/fps, 1) for i in range(1, len(est)) if est[i] != est[i-1]]
    # ignora parpadeos de menos de 0.4 s
    seg = []; ini = 0
    for i in range(1, len(est)+1):
        if i == len(est) or est[i] != est[ini]:
            seg.append((est[ini], ini/fps, i/fps)); ini = i
    seg2 = []
    for s in seg:
        if seg2 and (s[2]-s[1] < 0.4 or seg2[-1][0] == s[0]): seg2[-1] = (seg2[-1][0], seg2[-1][1], s[2])
        else: seg2.append(s)
    t_split = sum(e-b for k, b, e in seg2 if k == "split"); t_cara = sum(e-b for k, b, e in seg2 if k != "split")
    ev = agrupa(tiempos(f, a.video, f"crop=iw:ih*{a.zona_alto}:0:0,select='gt(scene,{a.umbral})'"), 0.6)
    sub = agrupa(tiempos(f, a.video, f"crop=iw:ih*{a.sub_alto}:0:ih*{a.sub_y0},fps=20,select='gt(scene,0.03)'"), 0.12)
    r = {"video": a.video, "duracion_s": round(dur, 1),
         "layout": {"pct_split": round(100*t_split/max(dur,1)), "pct_cara_completa": round(100*t_cara/max(dur,1)),
                    "cambios_de_layout": len(seg2)-1, "bloques_cara_completa_s": [round(e-b, 1) for k, b, e in seg2 if k != "split"],
                    "bloques_split_s": [round(e-b, 1) for k, b, e in seg2 if k == "split"]},
         "eventos_visuales": {"total": len(ev), "por_10s": round(10*len(ev)/max(dur,1), 1), "s_por_evento": round(dur/max(len(ev),1), 2)},
         "subtitulo": {"cambios": len(sub), "por_segundo_aprox": round(len(sub)/max(dur,1), 2)}}
    print(json.dumps(r, ensure_ascii=False, indent=1))
    if a.json: open(a.json, "w", encoding="utf-8").write(json.dumps(r, ensure_ascii=False, indent=1))

if __name__ == "__main__": main()
