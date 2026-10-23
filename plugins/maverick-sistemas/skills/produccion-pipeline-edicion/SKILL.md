---
name: produccion-pipeline-edicion
description: Cómo edita Claude los Reels de Maverick de punta a punta (del video en bruto al exportado) con el paquete de edición instalado en ~/video-editor-maverick, Premiere Pro y HyperFrames, aplicando las decisiones de Adrie - formato Kallaway (gráfico animado arriba, su cara en caja abajo), medidas medidas, subtítulos, una canción por Reel, QA y exportar solo con su visto bueno. Usar al editar, cortar, subtitular, poner gráficos animados, música o exportar un Reel o Short. Gatillos - "edita este video", "terminar el reel", "pon los gráficos", "pon música", "exporta", "prototipo kallaway", "hyperframes".
---

# Pipeline de edición de Maverick

Qué hace Claude entre el video en bruto de Adrie y el archivo listo para su visto bueno. **Nada se exporta, publica ni programa sin el visto bueno de Adrie** y nunca se hace clic en pantallas que publiquen.

## Dónde corre (verificar antes)
- **El paquete de edición** (atribuido a Alex Dilorenzo; autoría y licencia por confirmar) vive en `~/video-editor-maverick`. Sus skills (`edit-video`, `rough-cut`, `graphics-plan`, `graphics-build`, `edit-review`, `hyperframes*`, `premiere-pro`) **solo se cargan si la sesión se abre en esa carpeta**. Leer su `CLAUDE.md` y `my-rules.md` primero; `projects/<trabajo>/RUN.md` guarda el estado de cada trabajo.
- **Carril de acabado: Premiere Pro** (`.setup-complete` dice `lane=premiere`). Comprobar con `node lanes/premiere/premiere-bridge.mjs ping`: si responde pero `projectName` está vacío, **no hay proyecto abierto** y hay que pedirle a Adrie que abra su proyecto o pasarle el archivo. Si no responde: `./lanes/premiere/premiere-up.sh` y reintentar; no pedirle que reinicie nada antes de eso.
- **Entrada:** el video de Adrie se **copia** a `projects/<nombre-por-contenido>/raw/` (nunca se mueve ni se toca el original). El nombre del trabajo es el tema en kebab-case, no el nombre de la cámara ni una fecha.

## Los 8 pasos (siempre en este orden)
1. **Copiar** el original. 2. **Corte inicial**: transcripción palabra por palabra (WhisperX, una sola vez), quitar relleno y silencios; solo sobrevive lo que el espectador necesita saber ahora; repetición de una línea = usar la última toma. 3. **Audio**: ganancia medida y limitador, una sola cadena. 4. **Color** (solo cámara real): según el paquete. 5. **Gráficos**: plan → construcción → revisión (ver abajo). 6. **Efectos de sonido** solo si Adrie los pide. 7. **Revisión humana**: cambios de gusto se hacen en la conversación, uno por uno. 8. **Exportar**: solo con el visto bueno de Adrie; después `./finalize.sh <trabajo>` (primero sin `--apply`).
Un paso nombrado corre ese paso y se detiene: «solo el corte» no exporta.

## Formato Kallaway (principal) `[decisión de Adrie]`
- Gráfico animado **arriba** y su cara en **caja rectangular de esquinas redondeadas abajo**. **Su cara nunca va a pantalla completa** (solo en el formato Raw content). Una idea por escena, un evento visual cada **1 a 2 s**, cursor animado en cerca de la mitad de las escenas, ~1 de cada 5 escenas imita una pantalla real.
- **El contenido animado de arriba se construye en HyperFrames**, nunca en una plantilla HTML interactiva. Referencias hechas: `~/video-editor-maverick/projects/kallaway-prototipo-v2/hf` (crema) y `…-v3/hf` (**dark**, negro con puntos y rojo; fuente copiada en `assets/kallaway-hyperframes-v2` y `-v3-dark` de la skill `produccion-estilo-split-animado`). **Pendiente de Adrie:** si dark queda como estándar del formato (la paleta de marca crema, azul y ámbar solo vale si no lo pide).
- **Medidas de la referencia** (medidas con script; ficha 3f en la bóveda, `03 - Go-to-market/Estudio profundo - kallawaymarketing - sistema de edición y formato - 2026-10-21`), en 1080×1920: caja de la cara de **x 69 a 1008 (87 % del ancho)**, borde superior ≈ y 1395 en la referencia; **en Maverick la caja termina en y 1620** (zona segura: nada clave en los 200 px de arriba ni en los 300 de abajo), así que va de ~y 1150 a 1620. Subtítulo de **una palabra** centrado sobre la caja. Titular arriba en 2 líneas: sans negrita y **una palabra en serif cursiva** con subrayado o caja de acento. Fondo dark: negro puro con cuadrícula de puntos, un solo rojo (#E10613 relleno, #FF3B47 texto), verde solo para estados completados.
- **Subtítulos:** el estilo (una palabra animada o línea fija en mayúsculas) lo decide Adrie por formato; **preguntar antes de elegir**. En producción salen de la transcripción palabra por palabra, no de una voz de ejemplo.
- **Cara real:** el video de Adrie entra en la caja (recorte 9:16 con `face-frame.py --modes`, el paquete mide el encuadre); mientras no esté, la caja es un marcador.

## Construir y verificar el gráfico animado (HyperFrames)
Siempre con la versión fija y sin telemetría, desde la carpeta `hf` de la pieza:
```bash
export DO_NOT_TRACK=1 HYPERFRAMES_NO_TELEMETRY=1
npm_config_before=2026-10-01T23:59:59Z npx -y hyperframes@0.8.105 check
npm_config_before=2026-10-01T23:59:59Z npx -y hyperframes@0.8.105 snapshot --at 3,8,14
npm_config_before=2026-10-01T23:59:59Z npx -y hyperframes@0.8.105 render --quality draft
```
- **Nunca** `hyperframes upgrade`, `skills update` ni `init` sin `HYPERFRAMES_SKIP_SKILLS=1`; **no instalar paquetes** ni cambiar ajustes del sistema sin preguntar.
- Composición: HTML con `data-composition-id`, `data-width/height/duration` y **una sola línea de tiempo GSAP pausada** en `window.__timelines["<id>"]`. Sin `Math.random` ni relojes; `immediateRender:false` en un `fromTo` repetido sobre el mismo elemento; contraste ≥ 4,5 (`check` lo mide; un error de lint apaga las demás auditorías).
- Mirar 4 a 8 cuadros con `snapshot` antes de renderizar; el render en borrador va a Adrie, la exportación final solo con su visto bueno.

## Reglas de marca y seguridad (de `my-rules.md`)
- Español de Perú; «usted» en lo que va a clientes. **Sin IA como argumento de venta** en pantalla. Sin cifras, clientes ni promesas sin respaldo; todo dato inventado lleva **«Ejemplo ficticio»**. **Nunca mostrar datos de clientes** (Spektank, Galecc Service) sin permiso escrito.
- **Música:** una sola canción por Reel, de principio a fin, constante y **a −20 dB bajo la voz**, caída de 2 s al final; sin música si hay cifras o un tablero que explicar, salvo pedido. Solo con licencia comprobada y **nunca la carpeta `assets/_sfx-sin-licencia-NO-USAR`**. Vigente: guardar captura/registro de la ficha el día de la descarga y avisar si trae «Content ID Registered» (`03 - Go-to-market/Música para los videos - estilo y licencias - 2026-10-19`). La canción enérgica elegida está en `~/Downloads/Maverick Videos/musica/`.
- Las **portadas** salen de la escena 1 del Reel (skill `portadas-reels`): PNG 1080×1920 con el titular dentro del recorte 3:4 y sin cara.

## QA antes de enseñar
1. Gráficos: `uv run workflows/graphics-qa-short.py projects/<trabajo>` en verde (el paquete) y un solo ciclo de revisión.
2. Datos personales en pantalla: `uv run workflows/pii-scan.py projects/<trabajo>`.
3. Pasar `produccion-qa-antes-de-publicar` y `marca-afirmaciones-prohibidas-y-revision`.
4. **No inventar números del estudio de referencias:** de Gemini solo conteos y vocabulario (sus tiempos no valen); ritmo, color y geometría salen de ffmpeg (`medir_edicion.py`, `medir_especificaciones.py` en la skill `analisis-reels-con-gemini`).

## Errores comunes
- Abrir la sesión fuera de `~/video-editor-maverick` y esperar las skills del paquete.
- Asumir que Premiere «ve» el video: si el `ping` dice `activeSequence: null`, no hay nada abierto.
- Mover o tocar el original; exportar sobre el nombre del corte base.
- Poner la cara a pantalla completa en Kallaway, o la caja pasando y 1620.
- Repetir un hallazgo de Kallaway como regla sin decir que es `[medido, n=…]`.
- Usar subtítulos de ejemplo como si estuvieran sincronizados con la voz.

## Fuentes en la bóveda
`04 - Conocimiento/03 - Fichas de fuente/F-014 - Editor de video con Claude (paquete de Alex Dilorenzo)`, `…/Estudio profundo - kallawaymarketing…` (secciones 3e y 3f), `Sistema de portadas…`, `Aprendizajes técnicos - 2026-10-13`.
