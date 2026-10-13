---
name: diag-mapa-del-flujo-actual
description: Úsalo después de la entrevista para dibujar cómo viaja hoy una consulta hasta la próxima visita (canal, responsable, registro, fuga) y contar dónde se pierde. Gatillos - "mapa del flujo", "cómo funciona hoy su proceso", "map current workflow", "recorrido consulta cotización visita".
---

# Mapa del flujo actual

## Objetivo
Documentar el proceso manual tal como es, antes de automatizar nada, y ubicar en qué paso se pierde o se detiene una solicitud. El mapa es una hoja visual que el dueño pueda corregir.

## Pasos
1. **Definir el recorrido de referencia:** consulta, datos para cotizar, cotización enviada, respuesta del cliente, servicio o visita, constancia/registro, próxima visita. Adaptar nombres al sector (ver prop-adaptacion-por-sector).
2. **Reconstruir 3 casos reales** (uno bien resuelto, uno perdido, uno estancado) pidiendo ver el chat, la libreta o la hoja con datos privados ocultados.
3. **Por cada paso, anotar:** canal (WhatsApp, llamada, Google, web, papel, Excel), quién lo hace, dónde queda registrado, cuánto tarda (observado o estimado, rotulado), qué pasa si nadie actúa.
4. **Contar el embudo con hechos.** Pedir al equipo el conteo de un período corto: consultas recibidas, cotizaciones enviadas, cotizaciones respondidas, servicios confirmados, próximas visitas agendadas. Si no existe registro, rotular "estimación del dueño" y planear la línea base (ver piloto-diseno-y-metricas-antes-despues).
5. **Marcar fugas:** consulta sin responsable, cotización sin siguiente paso, servicio sin fecha de retorno, información que vive en la cabeza de una persona.
6. **Devolver el mapa al dueño** en una sola página y pedirle que corrija. Cerrar con la siguiente acción agendada.

## Plantillas y prompts listos
| Paso | Canal | Responsable | Dónde queda registrado | Tiempo | Qué pasa si nadie actúa | Dato: hecho o estimación |
|---|---|---|---|---|---|---|
| Consulta | | | | | | |
| Datos para cotizar | | | | | | |
| Cotización enviada | | | | | | |
| Respuesta | | | | | | |
| Servicio/visita | | | | | | |
| Próxima visita | | | | | | |

**Prompt para Claude:** "Convierte estas notas en un diagrama simple de 6 pasos en lenguaje de dueño, sin jerga. Marca con un icono rojo los pasos donde el cliente queda sin responsable o sin siguiente paso. Lista aparte lo que es dato medido y lo que es estimación."

**Conteo del embudo (rotular cada cifra):** consultas, cotizaciones enviadas, cotizaciones con respuesta, servicios confirmados, próximas visitas agendadas, por período definido con el dueño.

## Errores comunes
- Dibujar el proceso ideal en vez del real.
- Hablar con una sola persona; incluir también a quien responde el chat o agenda.
- Mezclar cifras estimadas con cifras medidas en la misma tabla.
- Mapear todo el negocio: basta el recorrido que conecta con el cuello a elegir.
- Proponer herramientas antes de terminar el mapa.
- Pegar capturas con datos de clientes en el documento: ocultar nombres, teléfonos y placas.

## Nivel de evidencia
- Documentar el proceso manual antes de automatizar: video de Jack Roberts (caso de manufactura) [video; cifras no verificado].
- Contar consultas, cotizaciones, visitas y cierres como un embudo (adaptación del marco LAPS): videos de Jack Roberts, lote 3 [video; las proporciones de ejemplo son no verificado, medir con datos propios].
- Recorrido consulta a próxima visita: nota de Oferta, Obsidian 2026-10-10 [decisión].

## Fuente
Maverick MP: Oferta - Sistemas para servicios recurrentes; Decisiones consolidadas 2026-10-10. Jack Roberts, extracciones G_negocio_automatizacion_1, _2 y _3.

## Vigencia
2026-10-11. Revisar al completar los primeros mapas reales por sector.
