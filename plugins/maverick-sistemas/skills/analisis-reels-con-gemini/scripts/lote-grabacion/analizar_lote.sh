#!/bin/bash
# Analiza en lote, SIN gastar tokens de Claude, todos los .mp4 de una carpeta (grabaciones recortadas 9:16, sin audio):
#  1) mide el ritmo de edición con ffmpeg (medir_edicion.py) -> medicion_<nombre>.json
#  2) saca una copia 4x más lenta y la pasa por la skill de Gemini con el prompt de anatomía -> fichas/<nombre>_x4.json
# Uso: herramientas/analizar_lote.sh <carpeta-con-mp4>
# La clave de Gemini se carga del archivo privado; nunca se muestra.
D="${1:?indica la carpeta con los .mp4}"; BASE="$(cd "$(dirname "$0")/.." && pwd)"
SK="$HOME/Downloads/maverick-sistemas/skills/analisis-reels-con-gemini"; FF=/opt/homebrew/bin/ffmpeg
PY="$BASE/herramientas/venv/bin/python"
set -a; . "$HOME/.config/maverick/gemini.env"; set +a
mkdir -p "$D/analisis/fichas" "$D/analisis/lento"
for v in "$D"/*.mp4; do
  n="$(basename "${v%.mp4}")"; echo "== $n"
  python3 "$SK/scripts/medir_edicion.py" "$v" --umbral 0.03 --zona-alto 0.5 --json "$D/analisis/medicion_$n.json" >/dev/null
  [ -s "$D/analisis/lento/${n}_x4.mp4" ] || "$FF" -nostdin -y -v error -i "$v" -an -vf "setpts=4*PTS,scale=720:1280" -r 24 -c:v libx264 -crf 24 -preset veryfast -pix_fmt yuv420p "$D/analisis/lento/${n}_x4.mp4"
  [ -s "$D/analisis/fichas/${n}_x4.json" ] || "$PY" "$SK/scripts/analizar_reel_gemini.py" "$D/analisis/lento/${n}_x4.mp4" --out "$D/analisis/fichas" --prompt "$SK/references/prompt-anatomia-de-edicion.md" 2>&1 | grep -E "^\[(ok|aviso|error)" | cut -c1-120
done
echo "LOTE LISTO"
