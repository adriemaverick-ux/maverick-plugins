---
name: enrutar-modelo-esfuerzo
description: Decide qué modelo y nivel de esfuerzo usar por tarea, cuándo usar fan-out paralelo y cuándo pedir una segunda opinión de otro modelo. Úsalo al empezar una tarea o si el gasto es alto. Triggers - /model, effort, esfuerzo, Opus, Sonnet, Haiku, ultra code, subagentes, revisión cruzada.
---

# Enrutar modelo y esfuerzo por tarea

## Objetivo
Gastar capacidad cara solo donde hace falta: planificar con modelo fuerte, ejecutar con uno más barato y verificar lo crítico con una segunda mirada.

## Pasos
1. Clasifica la tarea: trivial (typos, renombres, CSS de una línea), rutinaria (construcción, síntesis, análisis), difícil (depuración, diseño, arquitectura), irreversible (decisión de arquitectura, plan que no se repetirá).
2. Elige modelo con la regla general: pequeño o barato para trivial y volumen; intermedio para construir y uso diario; el más capaz para sesión principal, decisiones grandes y criterio creativo. Comprueba con /model qué tienes disponible, porque los nombres cambian.
3. Elige esfuerzo: bajo para trivial, medio para el día a día, alto para depuración o diseño difícil, muy alto para ejecuciones autónomas largas, máximo solo para decisiones de una sola vía. Patrón útil: abrir alto con mucho contexto y bajar a medio para construir.
4. Un modelo y un esfuerzo por sesión; si debes cambiar, abre sesión nueva. Los subagentes heredan modelo y esfuerzo: ajústalos antes de lanzarlos.
5. Fan-out paralelo (modo multiagente): úsalo solo en investigación, auditorías, revisión con varias perspectivas o sistemas separables, y en tareas de más de unos minutos. No lo uses para refactors de un archivo, bugs, dependencias secuenciales A->B->C ni cambios pequeños. Antes, da contexto y haz la entrevista previa; asigna a cada agente una lente distinta (escéptico, coste, marca, seguridad).
6. Verificación cruzada: en trabajo importante, pide a otro modelo/herramienta (por ejemplo una CLI de otro proveedor) que revise buscando puntos débiles, y reconcilia. Úsalo en una minoría de tareas, las críticas.
7. Al terminar: /compact o sesión nueva para no arrastrar contexto.
8. Anota en CLAUDE.md la política elegida para que el equipo la repita.

## Prompts de ejemplo
- "Clasifica esta tarea (trivial, rutinaria, difícil o irreversible) y recomiéndame modelo y esfuerzo con una línea de justificación."
- "Lanza 3 subagentes con lentes distintas (seguridad, coste, mantenibilidad) para auditar este módulo y dame un veredicto conjunto. Confirma el coste estimado antes."
- "Revisa este plan como un segundo modelo escéptico: lista los 5 puntos más débiles."

## Errores comunes
- Usar el esfuerzo máximo para todo.
- Multiagente para tareas pequeñas: la orquestación cuesta más de lo que ahorra.
- Cambiar de modelo en mitad de la sesión.
- Fiarse de que el modelo "diga" quién es: verifica la configuración real.
- Delegar a un modelo barato diseño desde cero o verificación de hechos.

## Checklist de cierre
- Tarea clasificada antes de elegir.
- Un modelo y un esfuerzo por sesión.
- Multiagente solo si compensa.
- Lo crítico revisado por una segunda mirada.

## Vigencia
- Nombres de modelos, niveles de esfuerzo, modo multiagente y precios cambian cada pocas semanas; releer /model y la documentación.
- Comparativas de calidad y costo del creador entre modelos: no verificado. Haz tu propia prueba con tu tarea.
