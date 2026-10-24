---
name: produccion-estilo-split-animado
description: Formato Kallaway de los Reels de Maverick - gráfico animado arriba (HyperFrames) y la cara de Adrie siempre en una caja rectangular abajo, con titular de dos pesos, cursor animado y subtítulo de una palabra; trae tres prototipos renderizables (crema y dark) con las medidas medidas de la referencia. Usar al crear o adaptar escenas animadas, al pedir "formato Kallaway", "estilo split", "pantalla dividida" o al convertir un guion en escenas animadas.
---

# Formato Kallaway (gráfico animado arriba, cara abajo)

Sistema tomado de la cuenta de referencia `@kallawaymarketing` y **medido** en 18 Reels (ficha en la bóveda: `03 - Go-to-market/Estudio profundo - kallawaymarketing - sistema de edición y formato - 2026-10-21`, secciones 3e y 3f). No se copia su identidad: ni textos, ni cifras, ni marca. Proceso completo de edición: skill `produccion-pipeline-edicion`.

## El sistema (se repite en cada escena)
1. **Gráfico animado arriba y la cara de Adrie siempre en una caja rectangular de esquinas redondeadas abajo.** **Su cara nunca va a pantalla completa en este formato** (la cara completa existe solo en Raw content y en cámara completa en trípode + overlays).
2. **Una idea = una escena** con su titular; **un evento visual cada 1 a 2 s** (la referencia: uno cada ~1,2 s).
3. **Titular en dos pesos:** sans negrita apretada y **una palabra en serif cursiva** con subrayado o caja de acento; entra palabra por palabra (de desenfocado a nítido).
4. **Un gráfico por escena**, con elementos escalonados (~0,13 s); contadores, marcos de esquinas que se dibujan, trazos que se dibujan, resaltados y etiquetas a mano con flecha.
5. **Cursor animado** presente en cerca de la mitad de las escenas; ~1 de cada 5 escenas **imita una pantalla real** (teléfono, hoja, WhatsApp ficticio).
6. **Subtítulo de una palabra**, centrado sobre la caja de la cara, cambia con la voz (~2,5 cambios por segundo en la referencia).
7. **Medidas** (1080×1920): caja de la cara de x 69 a 1008 (87 % del ancho); en Maverick de ~y 1150 a 1620 (zona segura: nada clave en los 200 px de arriba ni en los 300 de abajo); subtítulo al ~66 % de la altura de la referencia (aquí ~y 1066 a 1150).
8. **Look:** la referencia es **negro con cuadrícula de puntos y un solo rojo** (el estilo dark, `kallaway-hyperframes-v3-dark`); hay también una versión **crema** con la paleta de marca (`kallaway-hyperframes-v2`). **Pendiente de Adrie:** cuál queda como estándar.
9. Sin música propia en el tablero; la canción del Reel (una sola, a −20 dB) se pone al final según `produccion-pipeline-edicion`.

## Prototipos renderizables (HyperFrames, 1080×1920, 18 s, con sus `fonts/`)
En `assets/`: `kallaway-hyperframes` (v1, crema), `kallaway-hyperframes-v2` (crema, con celdas, burbujas de WhatsApp, etiquetas a mano, checks y aviso) y `kallaway-hyperframes-v3-dark` (**dark**). Se copian a una carpeta `hf`, se verifican y se renderizan:
```bash
export DO_NOT_TRACK=1 HYPERFRAMES_NO_TELEMETRY=1
npm_config_before=2026-10-01T23:59:59Z npx -y hyperframes@0.8.105 check
npm_config_before=2026-10-01T23:59:59Z npx -y hyperframes@0.8.105 render --quality draft
```
La cara es un marcador ("Tu cámara aquí") hasta tener el video real. Las escenas de **búsqueda** (buscador genérico y perfil) se construyen igual: barra que se escribe letra por letra, sugerencias escalonadas, clic y resultado, con interfaz **genérica** (sin logos ni nombres de marcas).

## Pasos para una pieza nueva
1. Partir del guion aprobado (`guion-9-bloques`): una escena por idea, titular de 4 a 6 palabras con una palabra de acento.
2. Elegir el gráfico de cada escena (tablero, tarjetas, contador, comentario, pantalla de teléfono) y copiar el prototipo más cercano.
3. Construir en HyperFrames, pasar `check`, mirar 4 a 8 cuadros con `snapshot` y renderizar un borrador.
4. Meter el video real de Adrie en la caja y los subtítulos desde la transcripción (palabra por palabra); `produccion-pipeline-edicion` manda el resto.
5. Pasar `produccion-qa-antes-de-publicar` y `marca-afirmaciones-prohibidas-y-revision`.

## Errores comunes
- Mostrar datos como reales: todo ejemplo lleva «Ejemplo ficticio»; sin clientes reales (Spektank, Galecc Service) sin permiso escrito.
- Más de una idea por escena, o gráficos estáticos que solo repiten la voz.
- Dos acentos de color: es uno solo (rojo en dark; ámbar en crema).
- Poner la cara a pantalla completa en este formato, o que la caja pase de y 1620.
- Citar como regla un número del estudio sin decir que es `[medido, n=…]`.

## Nivel de evidencia
Ritmo, subtítulos, colores y geometría: [medido con scripts en 18 Reels, 15 con ritmo utilizable]; vocabulario de animaciones y fondo: [conteos de Gemini, sin tiempos fiables]. Que este formato retenga mejor que otros: [hipótesis], sin prueba propia (medir retención y conversaciones por 1.000 alcanzadas).

## Fuente
Bóveda: *Estudio profundo - kallawaymarketing…* (3e y 3f), *Receta - estilo split*, *Sistema de portadas*. Skills `produccion-sistema-visual-maverick`, `analisis-reels-con-gemini` y `produccion-pipeline-edicion`.

## Vigencia
2026-10-23. Probar con la cara y la voz reales de Adrie antes de fijar dark o crema.
