---
description: Audita el consumo de tokens y la configuración precargada de Claude Code y propone recortes con confirmación.
argument-hint: "[ruta-del-proyecto opcional] [--aplicar para ejecutar recortes aprobados]"
---

Audita el consumo de tokens con el skill auditoria-tokens-uso. Argumentos: $ARGUMENTS

Pasos:
1. Inventario en solo lectura: servidores MCP/conectores y número de herramientas de cada uno, todos los CLAUDE.md en alcance con su tamaño, skills instalados, plugins o mods y sesiones largas o abiertas que puedas detectar.
2. Marca lo sospechoso (CLAUDE.md de más de ~5K caracteres o suma de más de ~10K, conectores sin uso, skills duplicados o con descripciones enormes).
3. Presenta un informe numerado: hallazgo, peso estimado, recorte propuesto, riesgo. Indica qué datos no pudiste medir.
4. Sin la opción --aplicar, termina aquí. Con --aplicar, ejecuta solo los recortes que yo apruebe uno por uno, guardando copia de cada archivo antes de editarlo y detallando cómo revertir. No desconectes nada ni borres sin mi confirmación.
5. Cierra con hábitos recomendados (/clear entre tareas, un modelo y esfuerzo por sesión, agrupar preguntas, texto en vez de capturas repetidas) y fecha sugerida de próxima auditoría.

No muestres ni copies credenciales que veas en la configuración; avisa de su existencia y recomienda revocarlas. Las cifras de ahorro son estimaciones no verificadas: mide antes y después.
