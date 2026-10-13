---
name: entrega-seguimiento-de-cotizaciones
description: Úsalo para armar el registro de cotizaciones con estado, responsable, fecha de envío y próximo paso, y recordatorios al equipo sin insistencia automática indiscriminada. Gatillos - "seguimiento de cotizaciones", "cotizaciones sin respuesta", "quote follow-up", "pipeline de cotizaciones", "recordatorio al equipo".
---

# Seguimiento de cotizaciones

## Objetivo
Que el dueño y el equipo sepan qué cotizaciones siguen abiertas, quién las tiene y cuál es el siguiente paso. El sistema recuerda al equipo; el contacto con el cliente lo decide una persona o una regla aprobada por el dueño.

## Pasos
1. **Definir etapas con el dueño** (ejemplo): Consulta calificada, Cotización enviada, Respondió, Aceptó, Servicio programado, Perdida. Una oportunidad abierta por servicio.
2. **Campos mínimos:** monto, fecha de envío, responsable, canal, próxima acción con fecha, motivo de pérdida (obligatorio al cerrar como perdida), consentimiento.
3. **Regla de recordatorio interno:** al pasar a "Cotización enviada", crear tarea para el responsable en {{DIAS_1}} días; si no hay respuesta, segunda tarea en {{DIAS_2}} días. Los plazos los acuerda el dueño según el ciclo de decisión de su servicio; no hay plazo estándar.
4. **Detener al responder el cliente:** usar el evento de respuesta del cliente para cancelar tareas pendientes.
5. **Mensaje al cliente:** borrador preparado para que el responsable lo revise y envíe, o regla automática solo si el dueño la aprueba por escrito, con una sola insistencia dentro de la ventana y opción de baja. Nunca ráfagas.
6. **Vista semanal:** lista de cotizaciones abiertas por responsable y antigüedad, y lista de estancadas (sin actividad por {{DIAS_ESTANCADA}} días).
7. **Cotizaciones y comprobantes:** las cotizaciones de GHL no son comprobantes SUNAT; la facturación electrónica va por un facturador peruano y se enlaza por webhook, con revisión humana al inicio [oficial / comunidad].
8. **Revisión humana y prueba** con casos ficticios antes de activar.

## Plantillas y prompts listos
**Borrador de seguimiento (ajustar tono del negocio, sin signos de exclamación):** "Hola [nombre], te escribo por la cotización de [servicio] que te enviamos el [fecha]. ¿Te quedó alguna duda o necesitas ajustar algo? Si ya no la necesitas, dime y la cerramos. Para dejar de recibir mensajes, escribe BAJA."

**Mensaje de cierre sin respuesta:** "Cerramos esta cotización por ahora. Si más adelante la necesitas, escríbenos y la retomamos."

**Prompt:** "Con esta lista de cotizaciones abiertas, ordénalas por antigüedad y propón para cada una el siguiente paso humano. No redactes mensajes para enviar sin que yo los revise. Marca las que superaron {{DIAS_ESTANCADA}} días sin actividad."

**Ejemplo de reporte semanal:** abiertas, enviadas esta semana, con respuesta, estancadas, cerradas con motivo.

## Errores comunes
- Insistencia automática a todos los contactos sin criterio.
- Seguimientos promocionales fuera de la ventana de 24 h.
- Varias oportunidades abiertas por el mismo servicio.
- Perder el motivo de pérdida: es lo que más enseña.
- Confundir "cotización preparada" con "enviada".
- Usar IA para fijar o negociar precios.

## Nivel de evidencia
- Registrar estado, responsable, fecha de envío y próximo paso; recordar al equipo sin insistencia indiscriminada: Oferta, 2026-10-10 [decisión].
- Disparadores de GHL (cambio de etapa, cliente respondió, estimaciones, recordatorios de fecha) y secuencia de seguimiento a +2, +5 y +10 días como ejemplo: informe 02 [oficial para los disparadores; los días son sugerencia de comunidad, [no verificado]; usar marcadores].
- GHL no emite comprobantes SUNAT: informe 02 [oficial/comunidad].
- Ritmo de seguimiento (5 o más toques) y porcentajes de respuesta: videos de Jack Roberts [video; no verificado, medir en el piloto].

## Fuente
Maverick MP: Oferta; Decisiones consolidadas 2026-10-10 (sección 4, etapas del pipeline). Maverick Research: 02_ghl_crm_y_redes (6.5, 8.3, 10.1). Jack Roberts: G_negocio_automatizacion_3 (módulo 5), _4 (A1, D3).

## Vigencia
2026-10-11.
