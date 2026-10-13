---
name: auditoria-tokens-uso
description: Audita y reduce el consumo de tokens y límites de uso de Claude/Claude Code (conectores, MCP, CLAUDE.md, skills, sesiones largas) y fija hábitos de ahorro. Úsalo cuando llegues a límites o las sesiones vayan lentas. Triggers - tokens, límite de uso, usage limit, ahorrar tokens, context bloat, /clear, /compact.
---

# Auditoría de tokens y uso

## Objetivo
Encontrar qué se precarga en cada sesión y qué sesiones consumen más, recortar lo inútil con confirmación y establecer hábitos que alarguen el uso disponible.

## Pasos
1. Inventario de lo que se carga siempre: servidores MCP/conectores y cuántas herramientas exponen cada uno, todos los CLAUDE.md en alcance (global, proyecto, subcarpetas), skills instalados, memoria, plugins/mods.
2. Marca como sospechosos: CLAUDE.md individuales de más de ~5K caracteres o suma de más de ~10K (umbrales orientativos), MCP sin uso reciente, skills duplicados o con descripciones larguísimas.
3. Revisa sesiones abiertas o históricas largas: unas pocas sesiones olvidadas pueden concentrar casi todo el gasto. Ciérralas.
4. Propón un plan de recortes (desconectar conectores no usados, partir CLAUDE.md, mover detalle a archivos referenciados) y pide confirmación antes de aplicar. No borres nada sin respaldo.
5. Hábitos: /clear entre trabajos distintos; un modelo y un esfuerzo por sesión (cambiar a mitad reprocesa el historial); agrupar preguntas en un solo mensaje; editar el mensaje en vez de corregir con otro cuando la interfaz lo permita; texto en vez de PDF/imágenes que se reutilizan; describir con palabras en vez de pegar muchas capturas.
6. Estilo de salida: crea un skill de comunicación breve (problema, arreglo en una frase, sin relleno) y úsalo por defecto.
7. Para repos grandes, considera una herramienta de mapa de relaciones del código (por ejemplo Graphify) tras revisarla con auditoria-repos-seguridad; con repos pequeños no compensa.
8. Reparte modelos por tarea (skill enrutar-modelo-esfuerzo) y revisa el contador de uso tras los cambios.
9. Deja un informe: antes/después, qué se recortó, hábitos acordados, fecha de próxima auditoría.

## Prompts de ejemplo
- "Audita mi configuración de Claude Code: lista MCP con su número de herramientas, todos los CLAUDE.md con tamaño, skills y sesiones abiertas. Marca lo que pese más de lo que aporta. No cambies nada aún."
- "Aplica solo los recortes 1, 3 y 5 del informe y guarda copia de los archivos originales."
- "Crea un skill de estilo de respuesta corta: problema, solución en una frase, sin relleno, sin preguntas innecesarias."

## Errores comunes
- Usar /compact como solución universal en lugar de /clear entre tareas.
- Mantener conectores "por si acaso".
- Cambiar de modelo o esfuerzo a mitad de conversación.
- Subir la misma captura una y otra vez.
- Recortar a ciegas sin guardar copia.

## Checklist de cierre
- Inventario completo y guardado.
- Cada recorte tiene copia de respaldo.
- Sesiones olvidadas cerradas.
- Medición posterior comparada con la inicial.

## Vigencia
- Comandos (/clear, /compact), existencia del contador de uso y la mecánica de caché cambian por versión.
- Las cifras de ahorro y los porcentajes de desperdicio del creador: no verificado; mide los tuyos.
- Cuotas y planes varían; consulta tu plan actual.
