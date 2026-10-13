#!/usr/bin/env python3
"""Analiza uno o varios videos con la API de Gemini y guarda una ficha JSON por video.

Uso:
  export GEMINI_API_KEY=...        # en tu terminal; NUNCA pegues la clave en el chat ni en notas
  python3 analizar_reel_gemini.py reel1.mp4 reel2.mp4 --out fichas/
Opciones:
  --model   modelo de Gemini (por defecto: variable GEMINI_MODEL o gemini-3.5-flash; con reintento en otros modelos si hay alta demanda)
  --prompt  ruta del prompt (por defecto: ../references/prompt-ficha-de-reel.md)

NOTA: el nivel gratuito limita a 20 solicitudes por día y por modelo (error 429). Con facturación activada se levanta.
PROBADO el 2026-10-12 con un Reel de 11 s (google-genai 1.47, gemini-3.5-flash): genera la ficha JSON. Los modelos 3.6 y 3.8 dieron 503 por alta demanda ese día.
Requiere clave y el paquete google-genai. Revisa las primeras fichas a mano.
OJO: Gemini inventa sonido si el video no tiene audio; el prompt lo prohíbe, pero verifica.
"""
import argparse, json, os, re, sys, time
from pathlib import Path

def cargar_prompt(ruta):
    t = Path(ruta).read_text(encoding="utf-8")
    partes = t.split("\n---\n", 1)
    return (partes[1] if len(partes) == 2 else t).strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("videos", nargs="+")
    ap.add_argument("--out", default="fichas")
    ap.add_argument("--model", default=os.environ.get("GEMINI_MODEL", "gemini-3.5-flash"))
    ap.add_argument("--fallback", default="gemini-3-flash-preview,gemini-3.5-flash-lite,gemini-3.6-flash,gemini-3.8-flash", help="modelos a probar si el principal responde 503 (alta demanda)")
    ap.add_argument("--prompt", default=str(Path(__file__).resolve().parent.parent / "references" / "prompt-ficha-de-reel.md"))
    a = ap.parse_args()
    if not os.environ.get("GEMINI_API_KEY") and not os.environ.get("GOOGLE_API_KEY"):
        sys.exit("Falta la variable de entorno GEMINI_API_KEY (defínela en tu terminal, no en un archivo compartido).")
    try:
        from google import genai
    except ImportError:
        sys.exit("Instala el SDK: pip install google-genai")
    client = genai.Client()
    prompt = cargar_prompt(a.prompt)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    for v in a.videos:
        p = Path(v)
        if not p.exists():
            print(f"[saltado] no existe: {v}"); continue
        print(f"[subiendo] {p.name}")
        f = client.files.upload(file=str(p))
        while not f.state or f.state.name != "ACTIVE":
            if f.state and f.state.name == "FAILED":
                print(f"[error] procesamiento fallido: {p.name}"); break
            time.sleep(5); f = client.files.get(name=f.name)
        else:
            texto = None; hubo503 = False
            for ronda in range(4):
              if texto is not None: break
              if ronda and not hubo503: break   # solo reintentar con espera si fue alta demanda (503), no cuota
              if ronda: print(f"[aviso] ronda {ronda+1}: esperando {30*ronda}s por alta demanda"); time.sleep(30*ronda)
              for modelo in [a.model] + [m for m in a.fallback.split(",") if m and m != a.model]:
                  print(f"[analizando] {p.name} con {modelo}")
                  try:
                      try:   # forma de la documentación actual (interactions); si el SDK no la tiene, usar generate_content
                          r = client.interactions.create(model=modelo, input=[
                              {"type": "video", "uri": f.uri, "mime_type": f.mime_type},
                              {"type": "text", "text": prompt}])
                          texto = r.output_text
                      except AttributeError:
                          r = client.models.generate_content(model=modelo, contents=[f, prompt])
                          texto = r.text
                      break
                  except Exception as e:
                      if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                          print(f"[aviso] {modelo}: cuota diaria del nivel gratuito agotada (20 solicitudes por modelo y día); probando otro modelo")
                          hubo503 = hubo503 or False; continue
                      if "503" in str(e) or "UNAVAILABLE" in str(e):
                          print(f"[aviso] {modelo} no disponible por alta demanda; probando otro modelo")
                          hubo503 = True; time.sleep(3); continue
                      raise
            if texto is None:
                print(f"[error] ningún modelo respondió para {p.name}"); continue
            base = out / p.stem
            m = re.search(r"\{.*\}", texto, re.S)
            try:
                data = json.loads(m.group(0)) if m else None
            except Exception:
                data = None
            if data is not None:
                Path(str(base) + ".json").write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"[ok] {str(base)}.json")
            else:
                Path(str(base) + ".txt").write_text(texto, encoding="utf-8")
                print(f"[aviso] la respuesta no es JSON válido; guardada como {str(base)}.txt")
        try: client.files.delete(name=f.name)
        except Exception: pass

if __name__ == "__main__":
    main()
