---
name: analisis-reels-con-gemini
description: Estudia Reels de marcas personales con Gemini (que mira el video y lo describe en una ficha estructurada) y luego extrae de las fichas el estilo de edición, los hooks, el ritmo, los overlays y el sonido para adaptarlos a Maverick. Usar cuando Adrie quiera analizar videos de otros creadores o aprender su edición. Gatillos - "analizar reels", "estudiar esta cuenta", "cómo editan", "extraer hooks de estos videos", "Gemini video".
---

# Análisis de Reels con Gemini

## Objetivo
Convertir un video en datos que se puedan comparar: Gemini **ve** (imagen y audio) y escribe una ficha; Claude **sintetiza** varias fichas en estilo de edición **y en el sistema de hooks y guiones** (fórmulas, esqueletos, series, cierre y conversión), y los traduce al idioma del cliente de Maverick. Se toma el **sistema**, no el texto.

## Cuentas del primer estudio (confirmadas por Adrie, 2026-10-12)
`trentonluera14`, `ramiro.cubria`, `francoaguilarr`, `nick_saraev`, `codiesanchez`. Opcional: Víctor Heras (usuario pendiente). Muestra: 3 o 4 Reels con más vistas recientes por cuenta + 1 típico. Cada cuenta aporta algo distinto: Franco (llamado "YO al DM"), Ramiro (hablar a cámara y consultoría), Nick (flujos de trabajo en pantalla), Codie (negocios pequeños), Trenton (edición y estructura en otro nicho).

## Quién hace qué
- **Gemini:** observa el video y devuelve la ficha JSON (usa el prompt de `references/prompt-ficha-de-reel.md`).
- **Claude:** lee las fichas, cuenta patrones, compara, señala lo que se repite, y escribe la guía en la bóveda.
- **Adrie:** elige los videos, valida a mano algunas fichas y decide qué adoptar.

## Ruta A: sin API (la más simple)
1. Adrie consigue **10 a 20 Reels** de marcas personales que le gusten: grabación de pantalla o archivo propio.
2. Sube cada video a Gemini (app o Google AI Studio), pega el prompt de la referencia y copia el JSON que devuelve.
3. Guarda cada JSON en un archivo (`cuenta - tema.json`) y se lo pasa a Claude.

## Ruta B: con la API (para varios videos seguidos)
1. La clave de Gemini de Adrie ya está guardada (2026-10-12) en `~/.config/maverick/gemini.env` (permisos solo del usuario, fuera de la bóveda y de git). Cargarla sin mostrarla: `set -a; . ~/.config/maverick/gemini.env; set +a`. Es el "Default Gemini API Key" del nivel gratuito. **Nunca pegarla en el chat, en notas ni en la bóveda.** Verificado: lista 62 modelos y existe `gemini-3.8-flash`.
2. Instalar el SDK: `pip install google-genai`.
3. Ejecutar `python3 scripts/analizar_reel_gemini.py video1.mp4 video2.mp4 --out fichas/` (el nombre del modelo se confirma en la documentación vigente; por defecto `gemini-3.8-flash`).
4. Las fichas quedan en `fichas/`. **Probado el 2026-10-12** con un Reel real (funciona con `gemini-3.5-flash`; los modelos 3.6 y 3.8 dieron 503 por alta demanda y el script reintenta con otros).

## Pasos de Claude con las fichas
1. **Validar a mano de 3 fichas**: extraer 4 o 5 fotogramas del video con FFmpeg (se puede usar el `ffmpeg-static` del proyecto de HyperFrames), mirarlos y comprobar que lo que dice la ficha coincide. Anotar el porcentaje de acierto y las incertidumbres.
2. **Normalizar**: unir las fichas en una tabla (cuenta, formato, hook, tiempo hasta el primer beneficio, cortes por 10 s, overlays, sonido, subtítulos).
3. **Sintetizar** con `references/plantilla-sintesis.md` y guardar la nota en la bóveda (`registrar-hallazgos-en-obsidian`).
4. **Separar patrón de rareza**: lo que aparece en la mayoría de las cuentas frente a lo de una sola.
5. **Traducir a Maverick**: qué técnica adoptar, en qué blueprint de HyperFrames se construye, y cómo diría el gancho Adrie en el idioma del dueño de empresa de mantenimiento (skills `hooks-*` y `tono-humano-calido-peru` de `copy-y-estilo`, si está instalado).
6. **Proponer 3 experimentos** pequeños para probar en la próxima pieza y cómo medirlos.

## Grabación de pantalla sin audio (decisión de Adrie, 2026-10-12)
Los Reels se graban con la pantalla (`screencapture -v -V <segundos> -x -R x,y,w,h`) **solo en la región del video**, en una ventana limpia de Chrome en la esquina superior izquierda; nunca la pantalla completa (puede mostrar mensajes privados). Sin audio: **Gemini inventa el sonido** (lo comprobó el piloto), así que el bloque `sonido` queda en null y lo hablado se toma de los **subtítulos visibles**. Adrie no usa el equipo mientras se graba. Los archivos van a `~/Downloads/Maverick Videos/estudio-reels/`.

## Límites (decirlos siempre)
- Gemini **puede equivocarse**: por eso se validan fichas a mano. Con el muestreo por defecto (**1 fotograma por segundo**) puede perder cortes muy rápidos o animaciones breves.
- Tiempos y conteos de cortes son aproximados [no verificado].
- El análisis automático no mide por qué un video rindió; solo describe cómo está hecho. Las vistas y el engagement del video son un dato aparte.
- Los videos son **contenido de otros**: uso privado, solo para estudiar. No copiar textos ni secuencias, no republicar, no guardarlos en lugares compartidos. Subirlos a Gemini los envía a Google: usar solo contenido público.

## Qué NO hacer
- No usar la cuenta de Instagram de Adrie con automatización ni scrapers para bajar videos: Instagram prohíbe la recolección automatizada y puede restringir la cuenta. Se estudian videos que Adrie guarda o graba él mismo.
- No pegar claves en el chat.

## Nivel de evidencia
Flujo descrito por plantillas de terceros [vendor/comunidad]; formato de entrada a Gemini y límites [oficial, documentación de Google, consultada 2026-10-12]; el script y el prompt son diseño propio [no probado].

## Vigencia
2026-10-12. Revisar los nombres de modelo y la forma de llamada del SDK de Gemini, que cambian seguido.


## Captura de un Reel o post de Instagram (procedimiento verificado el 2026-10-13)
- **Un video no carga en una pestaña en segundo plano.** Abrir la URL **visible** con `open -a "Google Chrome" "<URL>"`, esperar unos segundos y localizar la ventana con `herramientas/ventanas.js` (`osascript -l JavaScript`), buscando la de título "Instagram".
- Grabar la ventana con `screencapture -v -V <segundos> -x -l<ID> raw.mov` y recortar el cuadro del video con ffmpeg (en esta Mac y a ese tamaño de ventana: `crop=674:1198:797:245`; **calibrar** extrayendo un fotograma). Los Reels en bucle empiezan a mitad de frase: avisarlo.
- Para entender solo la **estructura** (por ejemplo una plantilla de guion con pizarra), una **hoja de contacto de fotogramas** (`fps=1/2,tile=5x5`) permite verla sin Gemini.
- **Gemini:** `gemini-3-flash-preview` analiza video bien; los modelos de **imagen no tienen cuota gratuita** (error 429). No extraer cookies ni automatizar Instagram en masa.
- Guardar la ficha en la **biblioteca de ejemplos** (estructura, no texto).
