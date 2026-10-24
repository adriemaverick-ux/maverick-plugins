# Plantilla: síntesis de estilo a partir de varias fichas

Entrada: de 10 a 20 fichas JSON (una por Reel). Salida: una nota en la bóveda (`03 - Go-to-market/Estudio de Reels - AAAA-MM-DD.md`).

1. **Tabla resumen** (una fila por Reel): cuenta, formato, duración, tipo de hook, segundos hasta el primer beneficio, cortes por 10 s, tipo de overlay, uso de efectos de sonido, estilo de subtítulos.
2. **Hooks:** conteo por tipo; los 5 mejores con su texto (parafraseado, sin copiar largo); qué tienen en común; cómo los diría Adrie en el idioma del dueño de empresa de mantenimiento.
3. **Ritmo:** cortes por 10 s (media y rango), duración media del plano, dónde caen los rompe-patrones.
4. **Overlays y animación:** tipos más usados, cobertura (completa, parcial, dividida), cuánto tiempo ocupan, cómo entran y salen, qué relación tienen con lo que dice la voz.
5. **Sonido:** frecuencia de efectos, cuáles, sincronización, música.
6. **Subtítulos y texto:** estilo, tamaño, posición, palabra resaltada.
7. **Look:** paleta, contraste, fondo.
8. **Patrones que se repiten** vs **rarezas**: marcar lo que aparece en la mayoría y lo que es de una sola cuenta.
9. **Traducción a Maverick:** qué técnicas adoptar, cuáles no (hipérbole, cifras de dinero, lenguaje de Silicon Valley), y a qué blueprint de HyperFrames corresponde cada overlay (`kinetic-type-beats`, `grid-card-assemble`, `dataviz-countup`, `cursor-ui-demo`, `titlecard-reveal`, `typewriter-reveal`, `comparison-split`…).
10. **Calidad del análisis:** qué fichas se validaron a mano, qué incertidumbres marcó Gemini, y qué conclusiones son frágiles (poca muestra, muestreo de 1 fps).

Regla: es **estudio privado para inspirarse**. No se copian textos ni secuencias, no se republican videos de otros y los archivos no salen de la máquina de Adrie salvo hacia Gemini para el análisis.

## Parte 2: el sistema de hooks y guiones (lo que más vale)
Además de la edición, extraer **el sistema**, no las palabras:
1. **Biblioteca de fórmulas de hook:** las fórmulas abstractas con huecos que aparecen en `sistema_de_guion.formula_del_hook`, agrupadas por tipo y con cuántas veces se repiten por cuenta.
2. **Esqueletos de guion:** los 3 o 4 esqueletos más usados (beats, duración y palabras aproximadas, dónde cae la prueba y dónde se cierra el bucle abierto).
3. **Series y pilares:** qué temas y formatos repite cada cuenta (por ejemplo "error común", "caso de cliente", "demostración de pantalla"), con qué frecuencia y cómo los nombra.
4. **Texto de la publicación (caption):** estructura, longitud y uso de llamado a la acción.
5. **Sistema de conversión:** cómo pasa del contenido a la conversación (palabra clave en comentarios o DM, enlace en la bio, agendar llamada, destacadas con resultados), y qué automatización parece haber detrás.
6. **Voz:** longitud media de oración, nivel de formalidad, giros que repite. Es para entender el ritmo, no para imitar su voz: la voz de Adrie sale de su perfil de estilo.
7. **Plantillas de Maverick:** convertir cada fórmula y esqueleto en una plantilla con huecos en **el idioma del dueño de empresa de mantenimiento** (skills `hooks-*` y `tono-humano-calido-peru` de `copy-y-estilo`), con 1 ejemplo ficticio por plantilla y sin hipérbole, cifras de dinero ni promesas sin respaldo.
8. **Qué NO se toma:** afirmaciones de resultados, cifras de dinero, el mensaje de otro nicho, y cualquier frase literal.

**Principio:** se copia el **sistema** (la estructura que se repite), no el **texto**. Cada plantilla final debe poder escribirse sin ver el video original.
