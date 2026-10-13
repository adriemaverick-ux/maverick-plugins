---
description: Diseña y construye una web o landing con design system, anti-slop y QA, orquestando las skills de Claude Design.
argument-hint: <descripción del negocio> [URL de referencia] [URL del sitio actual]
---

Usa el subagente `disenador-claude-design` para diseñar una web con este encargo: $ARGUMENTS

Flujo a seguir:
1. Aclarar negocio, público, objetivo de conversión y referencias (máximo 4 preguntas).
2. Aplicar `web-que-vende-por-secciones` (investigación de nicho, sitemap, secciones) y `design-system-desde-referencias`.
3. Si hay URL de referencia, aplicar `extraer-adn-diseno` sin copiar contenido ni assets.
4. Aplicar `anti-ai-slop-tipografia-copy-color` al copy, fuentes y color.
5. Si es una pieza grande o reutilizable, proponer `design-loop-criticos` y avisar del costo antes de lanzarlo.
6. Preparar la entrega con `handoff-claude-design-a-code` y cerrar con `checklist-qa-visual`.

Resume al final: archivos creados, decisiones tomadas y pendientes. No escribas claves ni credenciales; cifras de terceros, solo como "no verificado".
