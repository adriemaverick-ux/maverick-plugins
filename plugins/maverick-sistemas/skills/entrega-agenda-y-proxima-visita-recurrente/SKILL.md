---
name: entrega-agenda-y-proxima-visita-recurrente
description: Úsalo para programar visitas o trabajos, dejar constancia del resultado y recordar la próxima revisión o mantenimiento solo cuando el cliente lo acepta y el ciclo lo justifica. Gatillos - "próxima visita", "recordatorio de mantenimiento", "agenda de visitas", "recurring service reminder", "renovación del servicio".
---

# Agenda y próxima visita recurrente

## Objetivo
Cerrar el ciclo: servicio hecho, resultado registrado y próxima visita agendada o propuesta, con recordatorio claro al equipo y, con consentimiento, al cliente. La recurrencia es una hipótesis a medir, no una promesa de renovación.

## Pasos
1. **Definir con el dueño el ciclo de cada servicio:** qué lo dispara (tiempo, kilometraje, contrato, estación, norma) y quién decide. No inventar intervalos; un criterio por servicio, escrito.
2. **Calendario y tipos de cita:** crear los tipos (visita técnica, servicio en taller, revisión), con duración, responsable y recordatorios acordados.
3. **Registrar el resultado de la visita:** qué se hizo, qué se observó, qué se recomienda y para cuándo, y constancia o informe si corresponde (el responsable de emitirlo y dónde se guarda lo define el negocio).
4. **Campos mínimos:** fecha del último servicio, fecha de próxima visita, frecuencia acordada, consentimiento para recordatorios (sí/no, fecha, canal).
5. **Recordatorio al equipo:** tarea interna antes de la fecha ({{DIAS_ANTES_EQUIPO}}) con la lista del cliente y el servicio sugerido.
6. **Recordatorio al cliente:** solo con consentimiento; mensaje de utilidad (no promocional) en {{DIAS_ANTES_CLIENTE}} días antes, por plantilla aprobada si está fuera de la ventana. Considerar costo por mensaje de utilidad (tarifa de Perú desde 2026-10-01 [no verificado]).
7. **Si el cliente no responde:** una persona decide si llamar o reprogramar; no repetir mensajes automáticos.
8. **Probar con 2 o 3 casos reales o ficticios** antes de cargar toda la base; confirmar con el dueño antes de activar.

## Plantillas y prompts listos
**Recordatorio al cliente (plantilla de utilidad, ajustar):** "Hola [nombre], desde [Negocio]: según lo acordado, tu próxima [revisión/mantenimiento] de [equipo/vehículo] corresponde alrededor del [fecha]. ¿Quieres que reservemos un horario? Para no recibir más recordatorios, escribe BAJA."

**Tarea interna:** "[Cliente] - próxima visita [fecha] - servicio sugerido [X] - último resultado [Y] - contactar por [canal]."

**Lista semanal de próximas visitas:** cliente, servicio, fecha objetivo, estado (por contactar, contactado, agendado, no desea).

**Prompt:** "Con estas visitas registradas y este ciclo acordado, genera la lista de clientes a contactar las próximas 2 semanas y un borrador de recordatorio por servicio. No agendes ni envíes nada; deja todo para mi aprobación."

## Errores comunes
- Recordar a clientes que no dieron consentimiento o que pidieron baja.
- Fijar intervalos de mantenimiento sin criterio técnico del negocio.
- No registrar el resultado de la visita: el recordatorio pierde contexto.
- Mensajes promocionales disfrazados de recordatorio.
- Agenda duplicada entre calendario y chat; una sola fuente de verdad.
- Prometer que el recordatorio garantiza la renovación.

## Nivel de evidencia
- Programar servicio, dejar constancia y recordar la próxima revisión con aceptación del cliente: Oferta, 2026-10-10 [decisión].
- Recordatorios por fecha, calendarios, plantillas de utilidad y costos de WhatsApp: informe 02 [oficial para los disparadores y precios publicados; la tarifa de utilidad de Perú vigente es [no verificado]].
- Un agente de voz o de chat que agende con calendario: videos de Jack Roberts [video; probar solo como demo; costos de marzo 2025 y no verificado].
- Recurrencia como base de la retención: lote 4 y 5 [video; cifras no verificado].

## Fuente
Maverick MP: Oferta (puntos 4 y 5); Decisiones consolidadas 2026-10-10. Maverick Research: 02_ghl_crm_y_redes (2, 8.2, 8.3, 4.3). Jack Roberts: G_negocio_automatizacion_1 (video 6), _4 (D1), _5.

## Vigencia
2026-10-11.
