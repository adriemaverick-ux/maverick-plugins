#!/bin/bash
# Graba cada Reel de lista_reels.txt en una ventana NUEVA de Chrome (no toca tus pestañas), la captura por su id,
# recorta el visor 9:16, corta el bucle y lo deja en videos/. Silencia el sonido durante la tanda y lo restaura.
# Solo se ve el visor del Reel: el recorte excluye mensajes y barras. Uso: ./grabar_tanda.sh
cd "$(dirname "$0")"; FF=/opt/homebrew/bin/ffmpeg; T=${T:-85}
caffeinate -dimsu -w $$ </dev/null >/dev/null 2>&1 &
MUTED=$(osascript -e 'output muted of (get volume settings)'); osascript -e 'set volume output muted true'
WID=$(osascript <<'AS'
tell application "Google Chrome"
set w to make new window
set bounds of w to {0, 33, 1470, 956}
return id of w
end tell
AS
)
trap 'osascript -e "tell application \"Google Chrome\" to close (every window whose id is $WID)" >/dev/null 2>&1; pkill -f reactivar.sh; [ "$MUTED" = "false" ] && osascript -e "set volume output muted false"' EXIT
(nohup ./reactivar.sh $WID >/dev/null 2>&1 </dev/null &)
n=0; total=$(wc -l < lista_reels.txt | tr -d ' ')
while IFS='|' read -r cuenta vistas codigo; do
  n=$((n+1)); f="videos/${cuenta}_${vistas}_${codigo}.mp4"
  [ -s "$f" ] && { echo "[$n/$total] ya existe $f"; continue; }
  echo "[$n/$total] $(date +%H:%M:%S) $vistas $codigo"
  osascript -e "tell application \"Google Chrome\" to set URL of active tab of window id $WID to \"about:blank\"" >/dev/null; sleep 1
  osascript -e "tell application \"Google Chrome\" to set URL of active tab of window id $WID to \"https://www.instagram.com/reel/$codigo/\"" >/dev/null; sleep 1
  CG=$(osascript -l JavaScript herramientas_ventanas.js </dev/null 2>/dev/null | grep "y=33 w=1470" | sort -t= -k2 -n | tail -1 | sed 's/id=\([0-9]*\).*/\1/')
  [ -z "$CG" ] && { echo "  sin ventana; salto"; continue; }
  screencapture -v -V $T -x -l$CG crudos/raw.mov </dev/null >/dev/null 2>&1
  if [ -s crudos/raw.mov ]; then
    CROP="900:1600:1020:224"
    "$FF" -nostdin -y -v error -i crudos/raw.mov -an -vf "crop=$CROP,scale=720:1280" -c:v libx264 -crf 22 -preset veryfast -pix_fmt yuv420p crudos/recortado.mp4 \
      && python3 recortar_bucle.py crudos/recortado.mp4 "$f" || echo "  error al recortar"
  else echo "  captura vacía (¿permiso de pantalla?)"; fi
  rm -f crudos/raw.mov crudos/recortado.mp4; sleep 2
done < lista_reels.txt
echo "TANDA COMPLETA $(date +%H:%M:%S)"
