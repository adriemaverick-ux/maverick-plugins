---
name: produccion-fondo-del-video
description: Fondo de los videos en cámara de Maverick - decisión de Adrie (2026-10-13) de usar UN fondo hecho con IA, realista (casa con objetos reales), generado una vez y puesto al editar en CapCut, con la estética de la marca (grafito, azul eléctrico, ámbar). Incluye prompts, cómo grabar para que el recorte quede limpio, cómo integrarlo (luz, desenfoque, grano) y alternativa de set físico. Gatillos - "fondo", "background", "fondo con IA", "dónde grabo", "quitar el fondo", "set de grabación", "iluminación".
---

# Fondo del video: imagen de IA fija, puesta al editar

## Decisión
Adrie decidió (2026-10-13): **un fondo ya establecido hecho con IA**, que se **pone al editar**, y que parezca **un lugar real: una casa con objetos reales**, no un degradado ni algo genérico. Se genera **una vez**, se aprueba, y se reutiliza en todos los videos. Los fondos animados solo van en escenas a pantalla completa (ver `produccion-overlays-hyperframes-claude-motion`), nunca detrás de su cara.

## Qué debe transmitir
Alguien serio y cercano que conoce el trabajo real de talleres y servicios técnicos. Un espacio habitado y ordenado, no un estudio de influencer ni una oficina de catálogo.

## Estética (de `produccion-sistema-visual-maverick`, traducida a un lugar real)
- Base **grafito / madera oscura**; UNA luz **azul eléctrico** tenue (tira LED detrás de un estante); UNA **lámpara ámbar** cálida visible.
- 6 a 8 objetos con sentido: oficio del cliente (caja de herramientas, libreta de órdenes de trabajo, tablero con papeles de seguimiento), trabajo de Adrie (laptop cerrada, cuaderno) y de casa (planta, libros, taza).
- **Cero** logos, texto legible, pantallas con contenido, personas, manos ni fotos de personas.
- Centro vacío donde irá Adrie; el fondo con **menos contraste que su cara**; desenfoque suave (profundidad de campo corta).

## Cómo generarlo (una vez)
Herramientas: Gemini (modelos `gemini-3.1-flash-image` o `gemini-3-pro-image-preview`; **no hay cuota gratuita de imagen: requiere facturación**; se probó el 2026-10-13 y dio error de cuota), la app de Gemini, ChatGPT/Imágenes u otro generador. **Revisar los términos de uso del generador** para uso comercial. Pedir formato **9:16 vertical**, idealmente en alta resolución.

**Prompt base (inglés, funciona mejor en generadores):**
> Photorealistic vertical 9:16 photo of a lived-in, tidy home office corner in Lima, Peru, empty background plate for a talking-head video: no people, no text, no logos, no screens with content. Soft key light from a window on the left, a warm amber table lamp visible in the background, a subtle dim electric-blue LED strip glow behind a dark wood shelf, graphite-gray wall, dark wood furniture, a green plant, a few books, a closed laptop, a small toolbox and a notebook with work orders on a shelf. Shallow depth of field, background softly blurred, camera at eye level, empty center space where a person will sit, moody modern look, 6 to 8 objects only, slight film grain.

**Variantes** (cambiar solo el lugar): *living room corner with a bookshelf and a sofa edge*; *tidy home workshop-office with a pegboard of clean tools and a workbench edge*.

Generar 6 a 10 opciones, elegir **una**, pedir ajustes pequeños ("menos objetos", "más oscuro", "sin texto en los libros") y guardar el archivo final como `fondo-maverick-v1.png` junto con el **prompt exacto**. Si se cambia el fondo, subir la versión (v2) para no mezclar.

### Revisión de la imagen antes de aprobarla
- [ ] Sin texto raro, logos, letras inventadas en libros o carteles.
- [ ] Objetos coherentes (sin herramientas deformes, sin cables imposibles).
- [ ] La luz parece venir de un lugar creíble.
- [ ] Hay espacio libre en el centro y arriba/abajo para subtítulos.
- [ ] Se ve bien en pantalla chica y no "cansa" la vista.

## Cómo grabar para que el recorte quede limpio
1. **Fondo liso detrás de Adrie** (pared uniforme mate o **tela verde #00B140**), **a 1.5 m o más** para evitar sombras pegadas.
2. **Luz frontal suave y pareja** (ventana grande con cortina o luz con difusor) y **luz de contorno** tenue para separar pelo y hombros. Es lo que más mejora el recorte automático.
3. **Dirección de la luz igual a la del fondo de IA** (en el prompt, ventana a la izquierda): luz principal de Adrie desde la izquierda y relleno suave a la derecha.
4. Ropa que **no se parezca al color del fondo** de grabación; evitar verde si se usa croma; evitar brillos y bordes finos.
5. Encuadre vertical, ojos en el tercio superior, **cámara fija** (el fondo de IA es estático). Balance de blancos fijo.
6. Mantener la misma distancia a la cámara en todos los videos para que la escala de Adrie respecto al fondo no cambie.

## Cómo integrarlo en CapCut Desktop
1. Importar el A-roll y el `fondo-maverick-v1.png`. Fondo en la pista inferior, **ajustado a 1080×1920**.
2. En el clip de Adrie: **Quitar fondo (Remove BG) automático** o croma si grabó con tela verde. Revisar bordes cuadro a cuadro (pelo, hombros, manos) y suavizar el borde (feather 1 a 3).
3. **Integrar:** bajar un poco el brillo del fondo, igualar temperatura y contraste con el A-roll, **añadir grano muy leve** a todo el cuadro, y una **sombra suave** bajo Adrie si el recorte se ve "pegado".
4. Escalar y posicionar a Adrie (cabeza en el tercio superior); **no mover el fondo** entre cortes, salvo un zoom lento y mínimo para dar vida.
5. Subtítulos y overlays encima; las escenas a pantalla completa (HyperFrames) tapan todo y luego vuelven.
6. Exportar y **ver en el teléfono**: ¿se nota el recorte? ¿la luz de Adrie coincide con la del fondo?

Si el recorte automático falla con frecuencia, la solución es la **tela verde y mejor luz**, no un fondo más complejo.

## Qué hace la gente y mejor opción hoy (búsqueda 2026-10-13; fuentes mayormente de proveedores, sin pruebas independientes comparadas)
**Tres rutas habituales:** (1) generar el fondo dentro de una herramienta de estudio o transmisión (StreamYard y similares), (2) **reemplazar el fondo en la edición de un video ya grabado** (CapCut, Runway, Descript, Beeble), (3) generar un entorno en movimiento con IA de video. Para Maverick la ruta es la **2**, con una imagen fija.

**Por qué se nota falso (y qué hacer):**
- **Bordes** (pelo, hombros, manos al gesticular): es lo primero que se ve. Grabar con luz frontal pareja y luz de contorno, y revisar con gestos reales.
- **Luz que no coincide** (el fondo dice "luz desde la derecha" y la cara está iluminada desde la izquierda): **generar primero el fondo, y luego iluminar a Adrie para que coincida** en dirección, color y fuerza. Elegir un fondo cálido si la luz propia es cálida.
- **Sujeto nítido sobre fondo pixelado o sin profundidad:** igualar nitidez y resolución; un **desenfoque suave** del fondo suele convencer más que un cuarto muy detallado.
- **Fondo que se mueve o "se derrite":** usar **imagen fija** (o movimiento mínimo y lento), no video generado.
- **Sin sombra:** añadir una sombra suave de contacto para que Adrie no "flote".
- **Audio:** que el sonido no contradiga el espacio (evitar eco de cuarto vacío con un fondo acogedor).

**Herramientas para el recorte (comparación indicativa, no verificada por pruebas independientes):**
| Herramienta | Para qué | Nota |
|---|---|---|
| **CapCut Desktop** (quitar fondo / croma) | Opción por defecto: gratis, buena con personas en video vertical grabado con celular | Suele ir por detrás de Runway en pelo y giros rápidos de cabeza; revisar bordes |
| **Runway Green Screen** | Plan B si CapCut falla en el pelo o hay movimiento rápido | De pago (≈ 12 USD al mes según una reseña; **verificar precio actual**); mejor control del borde |
| **Descript** | Si ya se edita por transcripción | Rapidez, no precisión de borde |
| **Unscreen y similares** | Recortes puntuales | Pruebas citadas son de competidores; verificar con material propio |

**Para generar la imagen:** Nano Banana (modelos de imagen de Gemini) y otros generadores funcionan sin sintaxis especial. Método de consistencia que recomiendan las guías: **una imagen maestra** y, si se quieren otros ángulos, derivarlos de ella repitiendo la misma descripción del cuarto y la misma luz. **No hay cuota gratuita de imagen en la API de Gemini** (probado el 2026-10-13); alternativa: la app de Gemini o ChatGPT/Imágenes de forma manual, o activar facturación solo con aprobación de Adrie.

**Recomendación de trabajo (criterio propio sobre esas fuentes, a validar con el experimento):**
1. Generar **una imagen maestra** (v1) con luz clara y dirección definida, desenfoque suave y centro vacío.
2. **Grabar a Adrie con luz coincidente** (misma dirección y calidad) sobre pared lisa o tela verde, ya que esto es lo que más pesa en que no se note.
3. Recortar en **CapCut**; si el borde falla, pasar solo ese clip por **Runway**.
4. Integrar: color, grano leve, sombra de contacto, fondo estático.
5. Probar en el teléfono. Si el resultado se ve falso, **volver al set físico** de la sección siguiente: sigue siendo la opción más segura.
6. Evitar por ahora los **fondos en video generados con IA** detrás de la cara (riesgo de deformaciones y parpadeo).

## Consistencia
Un solo fondo maestro (v1) para todo el contenido; si se quiere variedad, **2 o 3 variantes aprobadas** con la misma paleta y luz, rotadas por tema. Guardar prompt, imagen final y notas en la bóveda.

## Alternativa: set físico real
Si algún día se prefiere un espacio real en vez de IA: pared grafito o rincón oscuro, 5 a 8 objetos con sentido, luz principal suave, rim azul tenue y lámpara ámbar, a 1.5-2 m de la pared, mismo rincón siempre con foto de referencia. Comprar luces solo con aprobación de Adrie.

## Experimento para validar (no asumir)
Mismo guion de 20 s con **A: fondo de IA integrado** y **B: pared lisa de siempre**; comparar retención a los 3 y 10 s y **conversaciones calificadas por cada 1,000 alcanzadas** (ver `canales-prueba-4-semanas`). Es criterio de producción, no una garantía de resultados.

## Errores comunes
- Fondo de IA con texto o logos inventados.
- Luz de Adrie que contradice la del fondo (se nota "recortado").
- Fondo más llamativo que la cara.
- Cambiar el fondo en cada video o usar uno distinto sin versionarlo.
- Recorte con halo o pelo cortado por mala luz de grabación.
- Usar la imagen sin revisar los términos del generador.
