---
name: produccion-estilo-split-animado
description: Estilo visual y de animación «split» para los Reels de Maverick - gráfico animado arriba y la cámara de Adrie en un recuadro redondeado abajo, que alterna con cara completa; titular de dos estilos con subrayado, escalonado, contador, marco de esquinas, cursor animado y subtítulo de una palabra. Incluye la plantilla HTML 1080x1920 con 5 escenas de ejemplo. Usar al crear o adaptar un tablero animado, al pedir "estilo split", "pantalla dividida", "animaciones como el Reel de referencia" o al convertir un guion en escenas animadas.
---

# Estilo split animado (gráfico arriba, cara abajo)

Se toma el **sistema y los movimientos** de un Reel de referencia de un creador de marketing (estudiado cuadro a cuadro; ficha y receta en la bóveda: `03 - Go-to-market/Biblioteca de ejemplos/Receta - estilo split (pantalla dividida animada) - 2026-10-20`). **No se copia** su identidad: paleta, tipografías exactas, nombre, cifras ni promesas. Se aplica con la paleta de Maverick (crema, azul y **un solo acento ámbar**; ver `produccion-sistema-visual-maverick`). Complementa la regla de Adrie: todo gráfico de apoyo va **animado** y no repite la voz.

## El sistema (se repite en cada escena)
1. **Un solo modo: split.** Titular y gráfico animado arriba y tu cámara siempre en el recuadro redondeado de abajo. **La cara nunca va a pantalla completa** (decisión de Adrie, 2026-10-21; la cara completa solo existe en el formato Raw content, que no usa esta plantilla).
2. **Una idea = una escena** de 6 a 10 s con su titular.
3. **Titular en dos estilos:** sans gruesa + **una palabra en serif cursiva con el acento y subrayado que se dibuja**; entra palabra por palabra (desenfoque a nitidez).
4. **Un gráfico por escena**, de desenfocado a nítido, con elementos **escalonados** (~0,13 s entre uno y otro).
5. **Cifra que sube** en una etiqueta de color; **marco de esquinas** al final para resaltar lo importante.
6. **Cursor animado** que se mueve (~0,9 s por tramo) y hace clic: da sensación de demostración real.
7. **Subtítulo de una palabra** en negrita entre el gráfico y la cámara; cambia cada ~0,3 a 0,5 s. Se hace en CapCut con subtítulos automáticos: no va sincronizado con la voz dentro del tablero.
8. Fondo claro con retícula suave; el tablero no lleva música propia.

## Regla: HyperFrames (2026-10-22)
Las escenas animadas de producción se construyen en **HyperFrames** (composición con una sola línea de tiempo pausada; ver las skills `hyperframes` y `hyperframes-core` del paquete de edición). La plantilla interactiva de abajo es solo para **ver ideas** y no se puede renderizar a video. El prototipo verificado está en `assets/kallaway-hyperframes/` (18 s; pasa `npx hyperframes check`; se renderiza con `npm_config_before=2026-10-01T23:59:59Z npx -y hyperframes@0.8.105 render --quality draft`).

## Prototipos en HyperFrames (2026-10-23)
En `assets/` hay tres composiciones renderizables (1080×1920, 18 s, con sus `fonts/`): `kallaway-hyperframes` (v1, crema), `kallaway-hyperframes-v2` (crema, con más eventos: celdas, burbujas de WhatsApp, etiquetas a mano, checks, aviso) y `kallaway-hyperframes-v3-dark` (**dark**, estilo Kallaway: negro con puntos, un rojo, titular blanco con palabra en serif cursiva). Se copian a una carpeta `hf`, se verifican con `hyperframes@0.8.105 check` y se renderizan; la cara es un marcador hasta tener el video real. Las medidas salen de la ficha 3f del estudio de Kallaway. Proceso completo: skill `produccion-pipeline-edicion`.

## La plantilla (solo vista previa)
`assets/estilo-split-plantilla.html` (1080x1920, sin dependencias salvo las fuentes de Google; servir con `python3 -m http.server 8765 --bind 127.0.0.1` si se graba con Screenity, que no funciona en `file://`, ver `produccion-grabar-con-tablero-y-screenity`). Trae 6 escenas de ejemplo **con datos ficticios** rotulados «Ejemplo ficticio»: contador y fichas, tres tarjetas dispersas unidas a un «?», tablero con clic que cambia una fila, comentario con palabra clave, **buscador genérico** (se escribe la consulta, salen sugerencias y resultados) y **búsqueda de un perfil** (se escribe el usuario, clic en el resultado, se abre el perfil y se toca «Seguir»).
- **Teclas:** Espacio o clic = siguiente · ← anterior · R repetir · F pantalla completa.
- **Parámetros:** `?e=N` salta a la escena N (0 a 5) · `?sub=1` muestra palabras para ver el ritmo · `?cara=0` oculta la etiqueta «Tu cámara aquí» · `?grab=1` oculta la ayuda · `?auto=1` avanza solo.
- **Adaptar a una pieza:** cambiar `titulo` (con `<em>palabra</em>` para la serif) y el `build()` de cada escena en el arreglo `ESC`; reutilizar `mueve()`, `clic()`, `cuenta()` y `marco()`. La función `revisa()` en la consola lista elementos que se salen del escenario.

## Pasos para una pieza nueva
1. Partir del guion aprobado de Adrie (`guion-9-bloques`); una escena por idea, con el titular de 4 a 6 palabras y una palabra de acento.
2. Elegir el gráfico de cada escena (mock de tablero, tarjetas, contador, comentario); todas van en split (la cara no va nunca a pantalla completa).
3. Armar las escenas en la plantilla, revisar con `revisa()` y en móvil (zona segura: el recuadro de cámara y el subtítulo no deben tapar los botones de Instagram).
4. Grabar con Screenity o componer en CapCut sobre el recuadro oscuro; añadir subtítulos de una palabra.
5. Pasar `produccion-qa-antes-de-publicar` y `marca-afirmaciones-prohibidas-y-revision`.

## Escenas de búsqueda (buscador y perfil)
Para mostrar que el prospecto «busca algo en internet» o «entra a tu perfil»: barra que se escribe letra por letra con cursor parpadeante, desplegable de sugerencias escalonado, clic en una sugerencia o resultado, resultados en tarjetas y marco de esquinas. Interfaz **genérica**: sin logos, nombres ni colores de Google o Instagram, URL de ejemplo (`ejemplo-uno.com`) y la etiqueta «Ejemplo ficticio». No mostrar resultados que parezcan reales ni cifras de seguidores inventadas.

## Errores comunes
- Mostrar datos como reales: todo ejemplo lleva «Ejemplo ficticio»; sin clientes reales (Spektank, Galecc Service) sin permiso escrito.
- Copiar nombres de herramientas de terceros, cifras o promesas de crecimiento del original.
- Usar IA como argumento en el titular.
- Más de una idea por escena, o gráficos estáticos que solo repiten la voz.
- Dos acentos de color: es uno solo (ámbar).

## Nivel de evidencia
Descripción del estilo: [observación] sobre una grabación de 60 s sin audio, contrastada con fotogramas; los tiempos son aproximados. Que este estilo retenga mejor que el tablero a pantalla completa: [hipótesis], sin prueba propia todavía (medir retención y conversaciones por 1.000 alcanzadas).

## Fuente
Receta y ficha del Reel de referencia en la bóveda (2026-10-20); skills `produccion-sistema-visual-maverick`, `produccion-grabar-con-tablero-y-screenity` y `analisis-reels-con-gemini`.

## Vigencia
2026-10-20. Probar con la voz y la cámara de Adrie antes de adoptarlo como formato fijo.
