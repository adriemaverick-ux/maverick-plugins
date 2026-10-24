# Estudio en lote de una cuenta (probado el 2026-10-22 con 18 Reels)

Copiar estos archivos a una carpeta de trabajo de estudio (por ejemplo `Maverick Videos/estudio-<cuenta>/`; `analizar_lote.sh` va en `Maverick Videos/herramientas/` y calcula sus rutas desde ahí). **Solo con permiso explícito de Adrie y sobre contenido público.**

1. `lista_reels.txt`: una línea por Reel, `cuenta|vistas|codigo` (el código es lo que sigue a `/reel/` en la URL).
2. `grabar_tanda.sh`: abre cada Reel en una **ventana nueva** de Chrome (no toca las pestañas de Adrie), la graba con `screencapture -v -V 85 -x -l<id>` (el id de CoreGraphics se saca con `herramientas_ventanas.js`; el de AppleScript no sirve), la mantiene al frente con `reactivar.sh`, recorta el visor con **`crop=900:1600:1020:224` y escala a 720×1280** (calibrado para una ventana de 1470 px de ancho a y 33; calibrar de nuevo si cambia) y corta el bucle con `recortar_bucle.py`. Silencia el sonido del sistema durante la tanda y lo restaura al final: **comprobar después que el audio no quedó silenciado y que Chrome tiene las ventanas que tenía**. macOS pide una vez el permiso de pantalla. ~100 s por Reel. Sin audio.
3. `analizar_lote.sh <carpeta>`: por cada video, `medir_edicion.py` (ritmo, ffmpeg), una copia a 4× más lenta y la skill de Gemini con `references/prompt-anatomia-de-edicion.md`; la clave de Gemini sale de `~/.config/maverick/gemini.env` y nunca se muestra. Límite gratuito: 20 peticiones por modelo y día; la skill cae sola a otro modelo.
4. `medir_especificaciones.py <carpeta> salida.json`: colores, caja de la cara, subtítulo y ráfagas de movimiento, sin IA.

**No usar `detectar_visor.py`** (detección del visor por contenido): resultó poco fiable; el recorte fijo funciona mejor.
**Riesgo:** abrir muchas URLs de Instagram con un script puede parecer automatización; se hizo una sola vez, con permiso de Adrie, en una ventana de su sesión. No repetirlo en masa.
