---
name: piloto-diseno-y-metricas-antes-despues
description: Úsalo para diseñar el piloto de un cuello de botella con línea base obligatoria, métricas definidas con el dueño, criterio de éxito acordado antes de empezar y cierre con decisión. Gatillos - "diseñar piloto", "línea base", "métricas antes y después", "pilot baseline", "medir el piloto".
---

# Diseño del piloto y métricas antes/después

## Objetivo
Que el piloto responda una pregunta con datos del propio negocio. Sin línea base no hay piloto: hay una impresión. Todo resultado esperado es una hipótesis a medir, no una promesa.

## Pasos
1. **Formular la hipótesis** en una frase: "Si [cambio en el paso], entonces [métrica] cambia, comparado con [línea base]". Sin cifras inventadas.
2. **Elegir 2 a 4 métricas** de proceso, no de vanidad: por ejemplo, tiempo hasta la primera respuesta humana, porcentaje de consultas con responsable y siguiente paso, cotizaciones enviadas con seguimiento registrado, próximas visitas agendadas.
3. **Definir cada métrica con el dueño por escrito:** qué cuenta, qué no, de dónde sale el dato, quién lo registra y en qué período. Una métrica sin definición no se muestra.
4. **Medir la línea base antes de tocar nada:** período acordado ({{PERIODO_BASE}}) con conteo del propio equipo, historial de chats o registros existentes. Si no hay datos, el primer tramo del piloto es solo medir y registrar.
5. **Acordar el criterio de éxito antes de empezar** (qué cambio consideran valioso y qué no) y quién decide al cierre.
6. **Configurar y probar con datos de prueba o autorizados**, luego con el equipo, con un responsable nombrado. Cambios solo con aprobación humana.
7. **Seguimiento corto** semanal o quincenal: errores, casos raros, ajustes, y registrar qué se cambió y cuándo.
8. **Cerrar con tres opciones:** continuar, ajustar y repetir, o parar. Registrar aprendizajes y qué quedó fuera.

## Plantillas y prompts listos
**Ficha de métrica**
| Campo | Contenido |
|---|---|
| Nombre | |
| Definición (qué cuenta / qué no) | |
| Fuente del dato y responsable | |
| Período de línea base | {{PERIODO_BASE}} |
| Valor de línea base (hecho o estimación) | |
| Valor durante el piloto | |
| Criterio de éxito acordado | |
| Límites (muestra pequeña, cambios de estación, etc.) | |

**Registro de cambios:** fecha, qué se modificó, por qué, quién aprobó.

**Prompt:** "Con este cuello y estas notas, propone 3 métricas con definición exacta, fuente del dato y cómo medir la línea base sin herramientas nuevas. Señala qué conclusión NO se podría sacar con una muestra pequeña. Resultados como hipótesis a medir."

**Texto para el dueño:** "Antes de configurar nada, durante [período] anotamos juntos cómo está hoy. Al final comparamos con lo mismo, y usted decide si seguimos."

## Errores comunes
- Empezar a construir sin línea base y luego "recordar" cómo era antes.
- Atribuir al sistema cambios que pudo causar la temporada, un feriado o una campaña.
- Proclamar resultados con muy pocos casos; describir dirección y ejemplos, no significancia.
- Cambiar la definición de la métrica a mitad del piloto.
- Medir clics o mensajes en vez de consultas con responsable y siguiente paso.
- Extender el alcance durante el piloto sin acuerdo por escrito.

## Nivel de evidencia
- Línea base, métrica definida con el dueño y piloto de un paso: Oferta y Decisiones consolidadas 2026-10-10 [decisión].
- Separar hechos de estimaciones; evitar conclusiones estadísticas con pocos casos: metodología histórica, Obsidian 2026-10-08 [hipótesis razonable].
- Mes de resultados visibles, MVP iterativo y ronda de ajustes: videos de Jack Roberts, lotes 1 y 2 [video; resultados no verificado].
- Reglas simples y deterministas son más fiables que agentes: lote 1 (video 9) [video; porcentaje de error citado no verificado].

## Fuente
Maverick MP: Oferta (entrada a un piloto); Decisiones consolidadas 2026-10-10; 99 - Archivo/Validación de dolores, demos y conversión (2026-10-08). Jack Roberts: G_negocio_automatizacion_1 (video 5, 9), _2 (video 1), _4 (C2, E).

## Vigencia
2026-10-11. Actualizar con los aprendizajes del primer piloto real.
