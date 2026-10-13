---
name: produccion-fondo-del-video
description: Fondo de los videos en cámara de Maverick - decisión de Adrie (2026-10-13) de usar un fondo YA EXISTENTE de casa u oficina real (como el de Trenton Luera), descargado de un banco de imágenes y puesto al editar en CapCut, con la estética de la marca. Incluye dónde conseguirlo, cómo elegirlo, licencias, cómo grabar para el recorte y cómo integrarlo. Gatillos - "fondo", "background", "fondo de oficina", "fondo existente", "quitar el fondo", "dónde grabo", "iluminación".
---

# Fondo del video: fondo existente de casa u oficina, puesto al editar

## Decisión
Adrie decidió (2026-10-13): **usar un fondo que ya existe** (foto o video de una **casa u oficina normal y real**), **no generarlo con IA ni diseñarlo**. Se descarga **uno**, se elige y se **pone al editar** detrás de su recorte. Referencia: el estilo de **Trenton Luera**, cuyas fichas del estudio de Reels describen estudios con estantería, trofeos u oficina; **no se sabe si él usa un set físico o un fondo puesto en edición**, así que se toma como referencia de aspecto, no de método. Los fondos animados solo van en escenas a pantalla completa (ver `produccion-overlays-hyperframes-claude-motion`).

## Qué buscar (aspecto)
Un lugar **creíble y habitado, ordenado y no de catálogo**: oficina en casa, estudio con estantería, escritorio con lámpara. Alineado con la marca: tonos **grafito / madera oscura**, una luz **cálida** (ámbar) y, si es posible, un toque frío azul tenue. **Sin** logos, texto legible, personas ni pantallas con contenido. Centro vacío donde irá Adrie, desenfoque suave de fondo (profundidad de campo), **vertical 9:16** o con resolución suficiente para recortar a vertical sin pixelarse (mínimo 1080×1920 ya recortado; ideal una foto de 4000 px o más).

## Dónde conseguirlo (fondos existentes)
| Fuente | Qué ofrece | Licencia (verificar en su página oficial antes de publicar) |
|---|---|---|
| **Pexels** (fotos y videos) | Filtro por orientación vertical; buscar "home office", "study room", "bookshelf office", "workshop interior" | Uso comercial gratis sin atribución; no usar como logo o sugerir respaldo de una marca |
| **Pixabay** (fotos y videos) | Filtro de orientación; calidad desigual | Licencia propia, uso comercial permitido sin atribución |
| **Unsplash** (solo fotos) | Mucha foto de interiores de buena calidad | Uso comercial gratis; no revender sin modificar; **evitar Unsplash+** (reglas distintas) |
| **Freepik** gratis | Variedad | **Exige atribución** en el gratis; evitar salvo plan de pago |
| **Envato Elements** (de pago) | Fondos y videos de oficinas, licencia comercial | Suscripción (≈ 16.50 USD/mes según una página; **verificar**); confirmar términos de la licencia |
| **Biblioteca de CapCut / Canva** | Fondos y plantillas listos | Revisar la licencia de cada recurso |

Se consultó la web el 2026-10-13; los datos de licencias vienen de resúmenes de terceros y de las páginas de los servicios: **leer la licencia oficial de la fuente elegida antes de publicar**, y guardar la captura o el enlace de la licencia junto al archivo.

**Elegir con un filtro simple:** ¿la luz de la foto (ventana a la izquierda o derecha, cálida o fría) se puede imitar al grabar? ¿Hay espacio libre en el centro? ¿Parece una casa u oficina de verdad y no un estudio de renta? ¿Evita elementos que contradigan "cercano" (trofeos de lujo, banderas, marcas)? Guardar **3 o 4 candidatos** y probar cada uno con un recorte de 5 segundos; elegir **uno** (`fondo-maverick-v1`) y anotar su fuente y enlace.

## Cómo grabar para que el recorte quede limpio
1. **Fondo liso detrás de Adrie** (pared uniforme mate o **tela verde #00B140**), **a 1.5 m o más** para evitar sombras pegadas.
2. **Luz frontal suave y pareja** (ventana grande con cortina o luz con difusor) y **luz de contorno** tenue para separar pelo y hombros. Es lo que más mejora el recorte automático.
3. **Dirección de la luz igual a la del fondo elegido** (si la ventana de la foto está a la izquierda, la luz principal de Adrie viene de la izquierda): luz principal de Adrie desde la izquierda y relleno suave a la derecha.
4. Ropa que **no se parezca al color del fondo** de grabación; evitar verde si se usa croma; evitar brillos y bordes finos.
5. Encuadre vertical, ojos en el tercio superior, **cámara fija** (el fondo es estático). Balance de blancos fijo.
6. Mantener la misma distancia a la cámara en todos los videos para que la escala de Adrie respecto al fondo no cambie.

## Cómo integrarlo en CapCut Desktop
1. Importar el A-roll y el fondo elegido (`fondo-maverick-v1`). Fondo en la pista inferior, **ajustado a 1080×1920**.
2. En el clip de Adrie: **Quitar fondo (Remove BG) automático** o croma si grabó con tela verde. Revisar bordes cuadro a cuadro (pelo, hombros, manos) y suavizar el borde (feather 1 a 3).
3. **Integrar:** bajar un poco el brillo del fondo, igualar temperatura y contraste con el A-roll, **añadir grano muy leve** a todo el cuadro, y una **sombra suave** bajo Adrie si el recorte se ve "pegado".
4. Escalar y posicionar a Adrie (cabeza en el tercio superior); **no mover el fondo** entre cortes, salvo un zoom lento y mínimo para dar vida.
5. Subtítulos y overlays encima; las escenas a pantalla completa (HyperFrames) tapan todo y luego vuelven.
6. Exportar y **ver en el teléfono**: ¿se nota el recorte? ¿la luz de Adrie coincide con la del fondo?

Si el recorte automático falla con frecuencia, la solución es la **tela verde y mejor luz**, no un fondo más complejo.

## Qué hace la gente y mejor opción hoy (búsqueda 2026-10-13; fuentes mayormente de proveedores, sin pruebas independientes comparadas)
**Tres rutas habituales:** (1) generar el fondo dentro de una herramienta de estudio o transmisión (StreamYard y similares), (2) **reemplazar el fondo en la edición de un video ya grabado** (CapCut, Runway, Descript, Beeble), (3) generar un entorno en movimiento con IA de video. Para Maverick la ruta es la **2**, con un fondo **existente** (foto) y no generado.

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

**Generar con IA queda descartado** por decisión de Adrie (y la API de Gemini no tiene cuota gratuita de imagen; probado el 2026-10-13).

**Recomendación de trabajo (criterio propio sobre esas fuentes, a validar con el experimento):**
1. Elegir **un fondo existente** (v1) de las fuentes de arriba, con luz de dirección clara, desenfoque suave y centro vacío.
2. **Grabar a Adrie con luz coincidente** (misma dirección y calidad) sobre pared lisa o tela verde, ya que esto es lo que más pesa en que no se note.
3. Recortar en **CapCut**; si el borde falla, pasar solo ese clip por **Runway**.
4. Integrar: color, grano leve, sombra de contacto, fondo estático.
5. Probar en el teléfono. Si el resultado se ve falso, **volver al set físico** de la sección siguiente: sigue siendo la opción más segura.
6. Evitar por ahora los **fondos en video generados con IA** detrás de la cara (riesgo de deformaciones y parpadeo).

## Consistencia
Un solo fondo maestro (v1) para todo el contenido; si se quiere variedad, **2 o 3 variantes aprobadas** con la misma paleta y luz, rotadas por tema. Guardar prompt, imagen final y notas en la bóveda.

## Alternativa: set físico real
Si algún día se prefiere un espacio físico en vez de un fondo puesto en edición: pared grafito o rincón oscuro, 5 a 8 objetos con sentido, luz principal suave, rim azul tenue y lámpara ámbar, a 1.5-2 m de la pared, mismo rincón siempre con foto de referencia. Comprar luces solo con aprobación de Adrie.

## Experimento para validar (no asumir)
Mismo guion de 20 s con **A: fondo existente integrado** y **B: pared lisa de siempre**; comparar retención a los 3 y 10 s y **conversaciones calificadas por cada 1,000 alcanzadas** (ver `canales-prueba-4-semanas`). Es criterio de producción, no una garantía de resultados.

## Errores comunes
- Fondo con logos o texto visibles, o con licencia no verificada.
- Luz de Adrie que contradice la del fondo (se nota "recortado").
- Fondo más llamativo que la cara.
- Cambiar el fondo en cada video o usar uno distinto sin versionarlo.
- Recorte con halo o pelo cortado por mala luz de grabación.
- Usar la imagen sin revisar los términos del generador.
