---
name: rag-memoria-conocimiento
description: Usar para dar a una app o a Claude conocimiento propio consultable (libros, PDFs, videos, reuniones) con búsqueda vectorial, sin gastar contexto. Gatillos - "RAG", "base de conocimiento", "chatbot con mis documentos", "Pinecone", "embeddings", "memoria larga", "NotebookLM".
---

# RAG y memoria de conocimiento

## Objetivo
Trocear y vectorizar documentos para recuperar solo los fragmentos relevantes al responder, en vez de cargar todo en la ventana de contexto. Sirve para un chatbot dentro de una web o para memoria de largo plazo de un proyecto.

## Pasos
1. **Decide la capa de memoria.** Estática: archivos del proyecto (`CLAUDE.md`, `brain.md` con quién eres, negocio y reglas). Activa: Notion u otra herramienta de tareas. Histórica: base vectorial para documentos. Numérica: Supabase para métricas. No uses RAG para lo que cabe en un archivo corto.
2. **Elige embedding.** Solo texto: un modelo multilingüe de texto (por ejemplo multilingual-e5-large en Pinecone). Con imágenes y gráficos: embedding multimodal (preview, verifica disponibilidad y límites gratuitos).
3. **Prepara el índice** (Pinecone u otra BD vectorial) y define metadatos por tipo (contrato, propuesta, reunión, investigación, interno). Claves de API solo en variables de entorno, con límite de gasto en proveedores de pago.
4. **Ingesta.** Coloca los PDFs en una carpeta, pide vectorizar con metadatos (incluye imágenes solo si lo pides explícitamente). Convierte PDFs pesados a markdown si fallan. Usa IDs únicos para actualizar con upsert y no duplicar.
5. **Prueba con preguntas cuya respuesta conozcas**; revisa que cite la fuente. Limita imágenes por respuesta (2-3) en el chat.
6. **Ingesta continua.** Para fuentes que cambian (canal de videos, blog), una tarea programada que verifique qué ya existe antes de procesar; empieza con 3 elementos de prueba; reporta resultados y errores.
7. **Alternativa gestionada.** NotebookLM aporta RAG con muchas fuentes, pero no tiene API oficial y los conectores comunitarios dependen de cookies del navegador; úsalo con cautela y para material no sensible.
8. **Seguridad y privacidad.** No indexes datos personales ni de clientes sin base legal; separa índices por cliente.

## Prompts de ejemplo
- "Conecta Pinecone con el modelo de embeddings de texto indicado en la documentación. Dime qué claves necesitas y cómo configurarlas en variables de entorno; no las escribas en archivos versionados."
- "Vectoriza todos los PDFs de docs/ con metadatos de tipo y fecha, usando upsert por ID para no duplicar. Reporta cuántos fragmentos se guardaron."
- "Prueba el chatbot con estas 5 preguntas con respuesta conocida y dime cuáles fallan y por qué."

## Errores comunes
- Re-vectorizar todo en cada ejecución (coste y duplicados).
- Trozos demasiado grandes o sin metadatos: respuestas vagas.
- Confiar en una respuesta sin comprobar la fuente.
- Pegar claves de API en el chat.

## Vigencia
Modelos de embeddings, límites del plan gratuito y conectores no oficiales de NotebookLM cambian o se rompen; cifras de fuentes o costes del creador: no verificado. Verifica la documentación vigente.

## Checklist de salida
- [ ] Se justificó RAG frente a un archivo de contexto corto.
- [ ] Embedding elegido según el tipo de contenido.
- [ ] Metadatos e IDs únicos definidos antes de ingestar.
- [ ] Preguntas de prueba con respuesta conocida superadas.
- [ ] Ingesta periódica evita duplicados y reporta errores.
- [ ] Sin datos personales ni de clientes indexados sin base legal.
