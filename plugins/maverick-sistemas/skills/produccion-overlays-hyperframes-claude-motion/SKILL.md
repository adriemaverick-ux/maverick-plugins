---
name: produccion-overlays-hyperframes-claude-motion
description: Flujo decidido por Adrie (2026-10-12) para animaciones y overlays de los videos de la marca - Claude Motion para explorar, HyperFrames (skill oficial y CLI local) para producir overlays precisos en HTML/CSS/GSAP, CapCut para el montaje final. Usar al crear cualquier overlay, gráfico explicativo o animación para un video en cámara. Gatillos - "overlay", "animación", "HyperFrames", "Claude Motion", "gráfico para el video", "animar este guion".
---

# Overlays con HyperFrames + Claude Motion

## Objetivo
Producir overlays claros, editables y con la marca vigente sobre un video en cámara, sin decorar por decorar. Fuente de verdad: la nota de la bóveda `03 - Go-to-market/Flujo de video - Claude Motion, HyperFrames y CapCut - 2026-10-12.md`. **Léela antes de empezar**, junto con `Marca Maverick y contenido` y `Sistema de diseño Maverick`.

## Quién hace qué
1. **Guion** (gancho, cuerpo hablado, cierre, indicaciones de grabación, momentos de overlay): lo prepara un asistente y **Adrie lo revisa antes de grabar**. Nada de resultados comerciales ni datos de clientes inventados.
2. **Claude Motion**: para *explorar* animaciones. Se prueba el guion o el brief visual, se ajusta y se exporta un MP4. Es distinto de Claude Code y de HyperFrames. **No hay conversión automática de su proyecto a HyperFrames**: su MP4 sirve de **referencia** de ritmo y composición.
3. **HyperFrames**: produce los overlays finales como composiciones **HTML/CSS/GSAP** con la skill oficial *HyperFrames by HeyGen* y el CLI `hyperframes` local (código abierto, sin créditos por render ni marca de agua visible). Se revisan y ajustan visualmente en **HyperFrames Studio** (`npx hyperframes preview`) antes de renderizar.
4. **CapCut Desktop**: montaje final (grabación, voz, subtítulos, overlays, efectos, exportación).

## Pasos (los 7 del método de Maverick)
1. **Partir del guion y del plano real.** Por cada aparición: frase hablada, segundo aproximado, idea que debe entenderse, duración de lectura y espacio libre alrededor de Adrie. Un overlay explica lo que la voz sola no deja claro; no decorar cada frase.
2. **Dirigir antes de programar.** Uno o dos fotogramas clave por escena: foco, qué cambia, qué debe recordar el espectador. Si Adrie tiene un MP4 de Claude Motion que le gusta, usarlo como referencia concreta.
3. **Aplicar el diseño vigente** (ver `produccion-sistema-visual-maverick`): Inter 800 para titulares, Inter 500/600 para texto, JetBrains Mono en mayúsculas para etiquetas. Dark: fondo #0A0C10, superficie #12151C, borde #252B36, primario #3D8BFF, ámbar #FFB020 (**un acento por escena**), texto #F4F5F7. Light: fondo #F7F4EE, superficie #FFFFFF, primario #1F6FEB, ámbar #D97F00, texto #12151C. Construir primero el fotograma de **máxima visibilidad** y luego entradas y salidas, para detectar solapamientos antes de animar.
4. **Animar relaciones, no solo apariciones.** Una metáfora visual por idea (la consulta pasa a cotización y muestra el siguiente paso; un estado cambia; una visita aparece en el calendario). Variar duración, trayectoria y easing según jerarquía, dentro de una familia de movimientos coherente. Incluir un momento quieto para leer. Evitar tres tarjetas que entran una tras otra con el mismo movimiento.
5. **Módulos editables.** Separar titulares, diagramas de proceso, fichas de caso, chips de estado y llamadas a la acción en composiciones reutilizables; texto y color parametrizados para corregir sin rehacer. Guardar código y recursos del proyecto.
6. **Revisar en Studio y por etapas** (decisión de Adrie del 2026-10-12: *código + revisión visual en Studio*). El asistente construye la estructura y el movimiento en el proyecto HTML/GSAP; después abre **ese mismo proyecto** con `npx hyperframes preview`. Studio muestra lienzo, capas, inspector y línea de tiempo para ajustar texto, posición, estilo, duración y fotogramas clave compatibles. Si un cambio afecta varias escenas o la lógica de animación, el asistente lo corrige en el código. Studio y el CLI trabajan sobre los **mismos archivos**: no se exporta ni convierte el proyecto entre ellos. Reproducir y revisar tras cada ajuste; correr `hyperframes lint` y `hyperframes check`; corregir desbordes, textos, ritmo, contraste y timing con la voz; **renderizar solo cuando se vea bien en Studio** y pase lint/check (`hyperframes render --output salida.mp4`, con `--quality high` para la entrega). **Ver el archivo exportado**, no solo la previsualización; probarlo sobre el A-roll en CapCut y en pantalla de teléfono.
7. **Exportar para el montaje.** Base 1080×1920 a 30 fps (60 solo con razón visual). Para **escenas a pantalla completa** (el formato decidido): **MP4 opaco normal**. Solo si algún día se quiere una capa parcial: MOV ProRes 4444 o WebM con alfa (comprobar importación en CapCut) o croma verde **#00B140**. Guardar también un MP4 de revisión.

## Preparación del entorno (una vez)
- Confirmar `node`, `hyperframes`, Chrome y FFmpeg con `hyperframes doctor`; instalar el CLI oficial si falta.
- Si `doctor` marca **FFmpeg ausente** pero el proyecto trae `ffmpeg-static` en `node_modules`, poner esa carpeta en el PATH antes de renderizar (verificado el 2026-10-12: así renderizó bien, con `hyperframes` 0.8.149). Los avisos de whisper, TTS, MusicGen y Docker son opcionales y no bloquean.
- Crear el proyecto con `hyperframes init` o reutilizar uno. Tamaño vertical 1080×1920, 30 fps.

## Plantilla por overlay
| Frase hablada | Segundo | Idea | Lectura | Zona libre | Movimiento | Módulo |
|---|---|---|---|---|---|---|

## Formato B: pantalla dividida con el flujo visible (propuesto por Adrie, 2026-10-12)
Un panel muestra el **workflow animado armándose al compás de la voz** y el otro muestra la **cara de Adrie siempre visible**. Pensado para piezas que explican un proceso (consulta → cotización → seguimiento → próxima visita).
- **Recomendación a probar:** pantalla dividida como base en piezas de proceso; **pantalla completa (Formato A)** solo en 1 o 2 momentos de énfasis por video. [criterio propio; probar y medir]
- **Montaje:** HyperFrames renderiza **solo el panel del flujo** (por ejemplo 1080×1056) y CapCut compone la división con el clip recortado alrededor de la cara (por ejemplo 1080×864). Así se ajusta sin re-renderizar. Automatizar la composición dentro de HyperFrames (medios del usuario en la línea de tiempo) es una opción posterior, no probada.
- **Encuadre de la cara:** recortar una franja del vertical 1080×1920 centrada en la cara (ojos en el tercio superior de la franja). Para esto sí hace falta ver el clip.
- **Zonas seguras:** la parte baja de Reels/Shorts la cubren botones y texto de la app. Primera propuesta: **cara arriba, flujo abajo**, manteniendo ojos y boca por encima de ~65% de la altura total y los elementos clave del flujo fuera del ~35% inferior. [criterio propio; las fuentes discrepan; verificar en el teléfono]
- **El flujo se construye por etapas:** cada paso aparece cuando Adrie lo dice (tiempo de la transcripción) y queda en pantalla; un elemento "viaja" por los estados; mantener un momento quieto para leer.

## Formato C: burbuja redonda + pizarra estática con scroll (decisión de Adrie, 2026-10-13; corregida)
**No es una animación.** La pizarra es un **tablero digital largo y estático** (esquemas, fichas, listas, textos grandes) y **Adrie lo desliza con la mano mientras explica**; su cara va en una **burbuja redonda chica**. Se descartó la versión con elementos que aparecen y se animan (tarjetas, flechas, token viajero): queda solo como plantilla alternativa.
- **Cómo lo hace la gente (búsqueda 2026-10-13, fuentes de tutoriales):** lienzo vertical largo (Canva, Figma, FigJam, Notion o HTML), **grabación de pantalla deslizando despacio** mientras se habla (Mac: Mayús + Comando + 5), recorte a la región útil y cámara en burbuja; en CapCut también se puede simular el scroll animando con fotogramas clave la posición vertical de una imagen larga.
- **Tablero:** 1080 px de ancho, **una pantalla (800 px de alto) por idea**, texto grande, paleta Maverick, una línea de hilo a la izquierda, "Ejemplo ficticio" donde haya datos inventados. El orden de arriba hacia abajo sigue los bloques del guion de 9 bloques, **sin rótulos internos de bloque**.
- **Escenario final 1080×1920:** burbuja de cara ~320 px arriba a la derecha (anillo azul eléctrico), ventana de la pizarra de unos 800 px (aprox. de 480 a 1280), subtítulos debajo y nada importante en el 35 % inferior.
- **Dos formas de grabar:** (1) abrir `visor-pieza1.html` en Chrome y **grabar la pantalla mientras se desliza y se habla**; (2) importar la imagen larga a CapCut y **animar el desplazamiento con fotogramas clave** para tener control del ritmo. La cara se graba aparte y se pone en círculo en CapCut.
- **Ritmo:** una idea por pantalla; deslizar al terminar de decir cada idea, sin rapidez.
- **Archivos:** plantilla en `assets/tablero-pieza-1/` (tablero y visor). Versión estática renderizada en `Maverick Videos/pieza-1-tablero/`.
- **A probar contra A y B** (retención, envíos por alcance, conversaciones de dueños por cada 1 000 alcanzadas).

## Evidencia del estudio de Reels (2026-10-12)
En 20 Reels de 5 creadores, **42 de 46 overlays eran parciales** (la cara sigue visible) y solo 4 a pantalla completa; los subtítulos palabra por palabra son casi universales; Nick Saraev usa **animación arriba y su cara abajo** con subtítulos al centro. Apoya el Formato B como base y la pantalla completa solo para énfasis. [observado en 20 videos; muestra pequeña]

## Skills oficiales de HyperFrames (instaladas el 2026-10-12)
Instaladas en `~/Downloads/Maverick Videos/.claude/skills/` (11 skills, ~6 MB, de HeyGen, Apache-2.0; revisadas: solo usan procesos normales de CLI/FFmpeg). Se instalaron **solo para esa carpeta** para no cargarlas en todas las sesiones. Para instalarlas globales: `npx hyperframes skills`.
- **`talking-head-recut`**: capa parcial junto a su cara (títulos cinéticos, lower-thirds, datos, citas, paneles laterales, picture-in-picture). Para las escenas a pantalla completa de Adrie se usa la ruta **`motion-graphics`** de la skill `hyperframes` y los blueprints de `hyperframes-animation`.
- **`hyperframes-animation`**: 22 *blueprints* de movimiento (p. ej. `kinetic-type-beats`, `grid-card-assemble`, `cursor-ui-demo`, `dataviz-countup`, `titlecard-reveal`, `typewriter-reveal`, `comparison-split`, `device-surface-showcase`) y un catálogo de **transiciones** (CSS y shader). Leer `blueprints-index.md` y `transitions/overview.md`.
- **`hyperframes-creative`**: especificación de diseño del video (`frame.md`), presets y reglas visuales.
- **`hyperframes-registry`**: más de 50 escenas listas (`npx hyperframes add <bloque>`).
- **`media-use`** (+ `hyperframes-audio`): transcripción con palabras sincronizadas, **20 efectos de sonido incluidos** (whoosh, pop, click, riser, impacto, tecleo…), etalonaje y tratamientos de imagen. Algunos scripts de voz y música usan servicios externos con claves: **no pegar claves en notas ni proyectos**.
- **`hyperframes-core`, `-cli`, `-studio`, `-keyframes`**: contrato de composición, comandos y revisión en Studio.

## Formato decidido: escenas a pantalla completa que tapan la imagen (2026-10-12)
Adrie aclaró que aquí el "overlay" **no es transparente: tapa todo el cuadro**. Es una escena animada (b-roll de motion graphics) que entra sobre el video en cámara mientras **su voz sigue sonando**, y luego vuelve a él. Consecuencias:
- **Exportar MP4 normal opaco** 1080×1920 a 30 fps (el alfa/croma solo si algún día se quiere una capa parcial).
- En CapCut la escena va **encima** del A-roll y se **silencia su audio propio**; la voz de Adrie sigue por debajo sin cortes.
- **La ruta de HyperFrames para esto es `motion-graphics`** (unidad corta, menos de 10 s, donde el movimiento es el mensaje: tipografía cinética, contadores, flujos, tarjetas). `talking-head-recut` queda para cuando se quiera una capa parcial junto a su cara.
- **El clip hablado sirve para el tiempo, no para la zona libre:** su transcripción con palabras sincronizadas marca en qué segundo exacto empieza y termina cada frase que se va a visualizar, y las escenas se animan al compás de la voz.
- **Su cara es la identidad (no hay logo gráfico):** no tapar demasiado seguido. Alternar cara → escena → cara; escenas de 3 a 8 s; que cada una explique algo que la voz sola no deja claro; entrar y salir con una transición y un efecto de sonido corto; volver a su cara antes de que pase mucho tiempo. Proporción orientativa a probar [criterio propio, no verificado]: que la cara siga siendo la mayor parte del video.

## Para elevar la calidad (informe de motion, 2026-10-12)
Ver `~/Downloads/Motion Research/01_craft_de_overlays_que_retienen.md`: curvas y duraciones (entrada decelera, salida acelera y es más corta), resortes con poco rebote (0 a 15%) para tono B2B, escalonado de 3 a 5 fotogramas, el overlay lleva **una palabra clave o dato y no repite la transcripción**, un token que "viaja" por los estados del proceso, y un margen conservador de zona segura (~15% arriba, 35% abajo, 10% izquierda, 15% derecha; verificar en el teléfono). Las cifras de retención de ese informe son [vendor]/[no verificado].

## Reglas de marca
- Sin cifras ni promesas sin respaldo; ejemplos **ficticios con la etiqueta "Ejemplo ficticio"**; no presentar una maqueta como sistema instalado.
- Sin nombre, logo ni datos de clientes sin permiso (Galecc solo descriptivo).
- CTA de marca: «Si este paso se pierde en tu empresa, cuéntame cómo lo llevas hoy».
- Solo efectos de sonido; la música con licencia se monta aparte en CapCut.

## Errores comunes
- Usar la prueba anterior como plantilla: tenía **Arial y la paleta vieja**; no copiarla.
- Dar por probado Claude Motion o una integración MCP cuando solo se usó el CLI local.
- Overlays que tapan la cara o los subtítulos; texto demasiado pequeño en teléfono.
- Animar todo con el mismo movimiento.

## Alternativa en la nube (opcional, no es el flujo por defecto)
El conector de HeyGen expone herramientas en la nube (`compose`, `render_video`, e importar un MP4 de Claude Motion al HyperFrames Studio). Son **una vía distinta**: `render_video` es de pago y el flujo decidido usa el CLI local. Usarlas solo si Adrie lo pide y confirma el costo. No están probadas con este flujo.

## Nivel de evidencia
Flujo y método: [decisión de Adrie, 2026-10-12]. Verificado por Claude el 2026-10-12: `hyperframes doctor`, `lint`, `check` y `render` funcionan en tu Mac (8 s, 240 fotogramas, 9.7 s de render) con el proyecto de prueba de Codex. Prueba hecha: circuito composición → lint/check → render local → revisión; **la revisión visual en Studio todavía no se ha probado** y no hay calidad final validada sobre grabación real. Detalles técnicos del CLI: [oficial, documentación de HyperFrames; no verificados por Claude en esta sesión].

## Fuente
Bóveda Maverick MP: *Flujo de video - Claude Motion, HyperFrames y CapCut*, *Sistema de diseño Maverick*, *Marca Maverick y contenido*. Docs: hyperframes.heygen.com (render, composiciones, determinismo, studio).

## Vigencia
2026-10-12. Revisar tras la primera pieza real sobre grabación, la primera revisión en Studio y la prueba de overlay transparente en CapCut (pendientes en la bitácora).
