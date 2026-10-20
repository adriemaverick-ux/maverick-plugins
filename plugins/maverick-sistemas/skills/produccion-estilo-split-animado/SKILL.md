---
name: produccion-estilo-split-animado
description: Estilo visual y de animación «split» para los Reels de Maverick - gráfico animado arriba y la cámara de Adrie en un recuadro redondeado abajo, que alterna con cara completa; titular de dos estilos con subrayado, escalonado, contador, marco de esquinas, cursor animado y subtítulo de una palabra. Incluye la plantilla HTML 1080x1920 con 5 escenas de ejemplo. Usar al crear o adaptar un tablero animado, al pedir "estilo split", "pantalla dividida", "animaciones como el Reel de referencia" o al convertir un guion en escenas animadas.
---

# Estilo split animado (gráfico arriba, cara abajo)

Se toma el **sistema y los movimientos** de un Reel de referencia de un creador de marketing (estudiado cuadro a cuadro; ficha y receta en la bóveda: `03 - Go-to-market/Biblioteca de ejemplos/Receta - estilo split (pantalla dividida animada) - 2026-10-20`). **No se copia** su identidad: paleta, tipografías exactas, nombre, cifras ni promesas. Se aplica con la paleta de Maverick (crema, azul y **un solo acento ámbar**; ver `produccion-sistema-visual-maverick`). Complementa la regla de Adrie: todo gráfico de apoyo va **animado** y no repite la voz.

## El sistema (se repite en cada escena)
1. **Dos modos que se alternan:** *split* (titular y gráfico arriba, cámara en recuadro redondeado abajo) al explicar; *cara completa* (la cámara crece a toda la pantalla) al hablar directo, para cambiar de plano y dar confianza.
2. **Una idea = una escena** de 6 a 10 s con su titular.
3. **Titular en dos estilos:** sans gruesa + **una palabra en serif cursiva con el acento y subrayado que se dibuja**; entra palabra por palabra (desenfoque a nitidez).
4. **Un gráfico por escena**, de desenfocado a nítido, con elementos **escalonados** (~0,13 s entre uno y otro).
5. **Cifra que sube** en una etiqueta de color; **marco de esquinas** al final para resaltar lo importante.
6. **Cursor animado** que se mueve (~0,9 s por tramo) y hace clic: da sensación de demostración real.
7. **Subtítulo de una palabra** en negrita entre el gráfico y la cámara (blanco sobre el video en cara completa); cambia cada ~0,3 a 0,5 s. Se hace en CapCut con subtítulos automáticos: no va sincronizado con la voz dentro del tablero.
8. Fondo claro con retícula suave; el tablero no lleva música propia.

## La plantilla
`assets/estilo-split-plantilla.html` (1080x1920, sin dependencias salvo las fuentes de Google; servir con `python3 -m http.server 8765 --bind 127.0.0.1` si se graba con Screenity, que no funciona en `file://`, ver `produccion-grabar-con-tablero-y-screenity`). Trae 5 escenas de ejemplo **con datos ficticios** rotulados «Ejemplo ficticio»: contador y fichas, tres tarjetas dispersas unidas a un «?», cara completa, tablero con clic que cambia una fila, y comentario con palabra clave.
- **Teclas:** Espacio o clic = siguiente · ← anterior · R repetir · F pantalla completa.
- **Parámetros:** `?e=N` salta a la escena N (0 a 4) · `?sub=1` muestra palabras para ver el ritmo · `?cara=0` oculta la etiqueta «Tu cámara aquí» · `?grab=1` oculta la ayuda · `?auto=1` avanza solo.
- **Adaptar a una pieza:** cambiar `titulo` (con `<em>palabra</em>` para la serif) y el `build()` de cada escena en el arreglo `ESC`; reutilizar `mueve()`, `clic()`, `cuenta()` y `marco()`. La función `revisa()` en la consola lista elementos que se salen del escenario.

## Pasos para una pieza nueva
1. Partir del guion aprobado de Adrie (`guion-9-bloques`); una escena por idea, con el titular de 4 a 6 palabras y una palabra de acento.
2. Elegir el gráfico de cada escena (mock de tablero, tarjetas, contador, comentario); decidir cuáles van en *split* y cuáles en cara completa (hook y cierre suelen ir a cara completa o con el recuadro grande).
3. Armar las escenas en la plantilla, revisar con `revisa()` y en móvil (zona segura: el recuadro de cámara y el subtítulo no deben tapar los botones de Instagram).
4. Grabar con Screenity o componer en CapCut sobre el recuadro oscuro; añadir subtítulos de una palabra.
5. Pasar `produccion-qa-antes-de-publicar` y `marca-afirmaciones-prohibidas-y-revision`.

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
