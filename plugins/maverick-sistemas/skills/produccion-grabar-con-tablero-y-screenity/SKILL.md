---
name: produccion-grabar-con-tablero-y-screenity
description: Procedimiento para grabar los Reels de Maverick con el tablero estático en Chrome y Screenity (servidor local, modo Área, zonas de cara y captions, teclas, guion lateral fuera del recorte, solución de problemas y conversión de WebM a MP4). Usar al preparar o grabar una pieza, al abrir el gráfico en Chrome o cuando Screenity no aparezca. Gatillos - "grabar", "Screenity", "abre el chart", "tablero", "presentador", "cámara", "captions".
---

# Grabar con el tablero y Screenity

Decisiones y archivos: bóveda `03 - Go-to-market/Recurso visual pieza 1 - Tablero - 2026-10-13`; plantilla de guion: `03 - Go-to-market/Plantilla de guion de 9 bloques` (skill `guion-9-bloques`). Archivos del tablero en `assets/tablero-pieza-1/` de la skill `produccion-overlays-hyperframes-claude-motion` y en `Maverick Videos/pieza-1-tablero/`.

## Preparar
1. **Servidor local** (las extensiones de Chrome **no funcionan en `file://`**): dentro de la carpeta del tablero, `python3 -m http.server 8765 --bind 127.0.0.1` (en segundo plano).
2. Abrir en **Google Chrome**: `http://127.0.0.1:8765/index.html` (menú de rubros) o directo `presentador-pieza1.html?frase=Control de plagas` / `presentador-pieza2.html?...`. Parámetros: `?rubro=...`, `?frase=...`, `?lateral=0` (oculta el guion lateral), `?tema=oscuro`.
3. Si el asistente debe abrirlo en el Chrome de Adrie: `open -a "Google Chrome" "<URL>"`.

## Grabar (Screenity)
- Instalar la extensión desde la tienda de Chrome y **fijarla** en la barra. Modos: **Pantalla, Área, Cámara**. Para el Reel: **Área**, activar **"Establecer un área de grabación"**, cámara y micrófono encendidos, **Iniciar grabación** y arrastrar el rectángulo para cubrir **solo la columna central** (el cuadro vertical).
- **Tecla F** = pantalla completa (si tapa la ventana de Screenity, no usarla). **Barra espaciadora, flecha abajo o rueda** = siguiente pantalla; flecha arriba = anterior.
- **Cuadro de lectura (derecha, fuera del recorte):** muestra la frase de la pantalla actual y un adelanto; no entra al video si solo se graba el área central. Si se graba la pestaña completa, recortar a 9:16 en CapCut.
- **Zonas:** cara en círculo abajo y centrada (~y 1380 a 1800 de 1920), captions encima (~y 1230 a 1370), contenido arriba (hasta ~y 1210). Verificar con una **prueba de 10 s** antes de grabar.

## Después
- Si el archivo sale en **WebM** y CapCut no lo abre: `ffmpeg -i entrada.webm -c:v libx264 -c:a aac salida.mp4` (usar el `ffmpeg-static` si no hay ffmpeg en el sistema).
- Captions y sonidos cortos en CapCut; revisar con `revisor-de-afirmaciones` y `produccion-qa-antes-de-publicar`.

## Problemas conocidos
- Screenity no aparece → la página se abrió desde `file://`; usar el servidor local.
- La cámara tapa contenido → achicar o bajar el círculo; el contenido ya vive arriba.
- Cuadro de lectura no se ve → ventana demasiado angosta (hace falta espacio a los lados) o `?lateral=0`.
- Elementos fuera de lugar → respetar las zonas; no agregar contenido en el tercio inferior.
