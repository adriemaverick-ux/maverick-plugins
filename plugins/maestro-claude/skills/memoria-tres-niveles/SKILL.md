---
name: memoria-tres-niveles
description: Diseña la memoria de Claude en tres niveles (quién soy, qué hago, qué pasó antes) para no depender del historial del chat. Úsalo al configurar o auditar memoria. Triggers - memoria, memory, wrap-up, Obsidian, Pinecone, RAG, contexto entre sesiones.
---

# Memoria en tres niveles

## Objetivo
Que un chat nuevo dé el mismo buen consejo que uno de 200 mensajes. Lo importante se escribe en archivos; los modelos olvidan, truncan y alucinan.

## Pasos
1. Nivel 1, "quién soy" (corto plazo): instrucciones globales de Claude (ajustes > instrucciones personalizadas) de unas 200 palabras: rol, objetivos, tono, no-negociables. Nada sensible.
2. Nivel 2, "qué hago" (medio plazo): pide a Claude que organice tu trabajo en 6-8 categorías. Una carpeta por categoría con su CLAUDE.md (menos de 200 líneas: por qué existe, stack, decisiones tomadas, mapa de memoria, referencias) y una subcarpeta memory/ para decisiones, resúmenes y próximas acciones. Trabaja abriendo la carpeta correcta.
3. Nivel 3, "qué pasó antes" (largo plazo), con dos capas: (a) archivo de conversaciones: un skill de cierre (/wrap-up) que al final de cada sesión añade resumen, decisiones, próximas acciones y fecha, solo agregando; (b) conocimiento de referencia (libros, transcripciones, expertos).
4. Elige el almacén del nivel 3: Obsidian/carpeta de markdown si el volumen es pequeño o mediano y quieres leer y editar a mano (el índice crece y sube el coste en tokens); base vectorial (por ejemplo Pinecone) si es grande y quieres búsqueda semántica (no es legible a mano). Usa namespaces por tipo en vez de un índice por tema.
5. En el CLAUDE.md de cada proyecto escribe cuándo consultar cada índice ("ante preguntas de estrategia, busca en X").
6. Las claves de cualquier servicio van en variables de entorno o gestor de secretos, nunca en el chat ni en la memoria.
7. Prueba: abre un chat nuevo, haz una pregunta de estrategia y comprueba que responde con tu contexto. Si no, falta algo escrito.
8. Cada pocas semanas revisa: contradicciones, páginas obsoletas, decisiones caducadas.

## Prompts de ejemplo
- "Según lo que sabes de mí, propón 6-8 categorías para organizar mi trabajo. Para cada una dame el CLAUDE.md inicial (menos de 200 líneas) y la estructura de memory/."
- "Crea un skill /wrap-up: al terminar la sesión resume lo hecho, decisiones, próximas acciones y fecha, y lo agrega al archivo de la categoría. No sobrescribe."
- "Audita mi memoria: dime qué está duplicado, obsoleto o contradictorio y qué debería ir a un índice de consulta."

## Errores comunes
- Un CLAUDE.md gigante: se paga en cada sesión.
- Más de ~8 carpetas de proyecto: nadie las mantiene.
- Guardar datos personales sensibles o credenciales.
- Confiar en el historial del chat como memoria.
- Un índice vectorial por cada tema en lugar de namespaces.
- Mezclar decisiones vigentes con borradores sin fecha.

## Checklist de cierre
- Instrucciones globales de ~200 palabras, sin datos sensibles.
- Cada categoría tiene CLAUDE.md corto y memory/.
- Prueba en chat nuevo superada.
- Fecha de la próxima revisión anotada.

## Vigencia
- Rutas de menú de ajustes y nombres de proveedores (Pinecone, Obsidian) cambian; el patrón de tres niveles es estable.
- Ahorros de coste citados por el creador para embeddings frente a leer con el modelo: no verificado.

## Variante Cowork / Agentic OS
### Memoria en 3 niveles + archivo de personalidad (soul)

## Objetivo
Que el agente te conozca y recuerde sin llenar la ventana de contexto. Principio: lo que siempre debe saber, siempre cargado y mínimo; lo demás, recuperable bajo demanda.

## Los tres niveles
1. **Núcleo (siempre cargado)**: pocos hechos estables sobre ti y el negocio, reglas de conducta y el soul. Corto: cada línea se paga en cada turno.
2. **Buffer de conversación**: últimos N mensajes (p. ej. 20) más un resumen rodante de lo anterior.
3. **Memoria semántica (bajo demanda)**: notas, documentos, transcripciones e historial indexados (vault de Obsidian, base vectorial o NotebookLM). Se consulta por significado y no consume contexto hasta que se usa.

## Pasos
1. **Escribe `soul.md`** con: identidad y rol del agente, misión y objetivos, negocio, métricas clave, voz (franco, que cuestione, sin servilismo, una pregunta a la vez, "la pregunta detrás de la pregunta").
2. **Entrevista inicial**: deja que el agente te pregunte; no vuelques un brain dump sin estructura. Si usas otro asistente, pídele un resumen de lo que sabe de ti y pégalo como material a revisar, no como verdad.
3. **Extracción de hechos**: tras cada intercambio relevante, guarda hechos clave en el núcleo o en notas, con herramienta explícita "recuerda esto".
4. **Base de conocimiento (wiki)**: carpeta con un `CLAUDE.md` que defina el flujo de ingesta: leer el archivo, discutirlo, escribir página fuente, actualizar páginas relacionadas y marcar contradicciones. Compártela entre Claude Code y tus otros agentes sin contaminar la memoria personal.
5. **Regla condicional**: en las instrucciones globales, "si preguntan X, consulta la carpeta Y" en lugar de cargar todo.
6. **Poda mensual**: revisa memorias obsoletas, duplicadas o contradictorias; mueve a cuarentena en vez de borrar.
7. **Respaldo**: versiona el soul y las notas (ver `endurecimiento-y-backup-agente`). Nunca guardes claves ni datos sensibles de terceros en la memoria.

## Prompts de ejemplo
- "Entrevístame una pregunta a la vez para escribir mi `soul.md`: quién soy, qué negocio tengo, objetivos del trimestre, métricas, y cómo quiero que me hables (franco, que me rete). Muéstrame el borrador antes de guardarlo."
- "Audita mi memoria: lista lo que siempre se carga, lo que está duplicado, lo obsoleto y lo que se podría mover a la wiki. Propón acciones pero no borres nada."
- "Ingesta este documento en mi wiki siguiendo su CLAUDE.md: resume, actualiza páginas afectadas y dime qué contradice lo que ya había."

## Errores comunes
- Meter todo en el núcleo: encarece cada mensaje y degrada la respuesta.
- Soul servil ("siempre apoya mis ideas"): el agente solo asiente.
- Confiar en la memoria como fuente de verdad sin revisarla.
- Mezclar memoria personal con base de conocimiento del mundo.
- Guardar secretos o información de terceros en notas.
- Esperar magia inmediata: la memoria útil se construye durante semanas.

## Vigencia
Basado en agentes y Cowork de feb-ago 2026. Los nombres de herramientas (Obsidian, bases vectoriales, NotebookLM no oficial) y las funciones de memoria nativa cambian; verifica qué ofrece tu entorno antes de montar lo tuyo.

## Checklist de verificación
- [ ] El núcleo cabe en pocas líneas.
- [ ] El soul exige que el agente te cuestione.
- [ ] Hay regla condicional para consultar la wiki.
- [ ] No hay secretos en la memoria.
- [ ] Programaste una poda mensual con cuarentena.

