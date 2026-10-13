---
name: auto-escalado-a-humano-y-calificacion
description: Usar al definir cuándo el bot debe pasar la conversación a una persona y cómo calificar leads por DM o WhatsApp. Gatillos "escalar a humano", "handoff", "calificar leads", "lead calificado", "pausar bot", "human takeover".
---

# Escalado a humano y calificación de leads

## Objetivo
Que el bot califique con preguntas simples y entregue el lead caliente a una persona a tiempo, sin doble respuesta bot-humano y sin salirse de la ventana de 24 h.

## Pasos
1. Definir 3-5 preguntas con botones: tipo de negocio (taller / saneamiento / mantenimiento / otro), tamaño (técnicos, vehículos o equipos), principal problema, urgencia, rol (decisor o no). Guardar cada respuesta en un campo.
2. Puntuar con reglas simples (no con el LLM): urgencia alta + decisor = calificado.
3. Disparadores de escalado inmediato: la persona pide hablar con alguien; menciona precio, contrato o cotización; tono negativo o queja; dos fallos seguidos del bot; tema fuera de alcance; lead calificado; baja confianza del modelo.
4. Mecanismo en ManyChat: etiqueta `humano` + "Pause Automations" + aviso interno (Slack, WhatsApp o correo) con resumen; al terminar el vendedor, quitar la etiqueta. No hay auto-pausa nativa documentada cuando un humano escribe. [comunidad]
5. Mecanismo con API directa: Conversation Routing (pass_thread_control a la bandeja de Instagram; extend hasta 7 días). Sin routing, todas las apps conectadas pueden responder y duplicar. [oficial]
6. Mecanismo en GHL: mover la oportunidad a "Calificado", crear tarea y notificación al usuario asignado; desactivar Conversation AI en ese contacto.
7. SLA interno: primera respuesta humana en menos de 1 hora hábil. Si pasaron más de 24 h desde el último mensaje del usuario, responder con Human Agent (hasta 7 días), mensaje escrito por una persona y no promocional. [oficial]
8. Aplicar opt-out: si la persona pide no recibir más mensajes, etiqueta `optout` y excluir de todos los flujos.
9. Tras cerrar o agendar: reactivar automatizaciones o marcar `cliente`.

## Plantillas/ejemplos
Mensaje de derivación: "Gracias. Te paso con una persona del equipo para que te ayude mejor. Responderá en horario hábil."
Resumen al vendedor: negocio, tamaño, problema, urgencia, origen (comentario/story/anuncio), campaña, consentimiento (sí/no y fecha), último mensaje.
Campos mínimos: tipo de cliente, tamaño, problema, urgencia, origen, consentimiento, etapa.

Métricas: finalización de calificación (>50% hipótesis), tasa de derivación, tiempo a primera respuesta humana (<1 h hábil), opt-out (<2% hipótesis), reuniones agendadas por fuente. Son objetivos iniciales, no benchmarks. [no verificado]

## Errores comunes
- Dejar que el LLM decida solo si un lead es caliente.
- Bot y humano respondiendo a la vez (falta pausa o routing).
- Responder a las 30 h con un mensaje automático: ventana cerrada (error 1545041).
- Usar Human Agent con texto promocional o redactado por el bot.
- No registrar el consentimiento ni el origen del lead.
- Derivar demasiado (flujo débil) o demasiado poco (LLM negociando).

## Nivel de evidencia
- Ventana, Human Agent y Conversation Routing: [oficial]. Patrón de etiqueta + pausa en ManyChat: [comunidad]. Umbrales de métricas: [no verificado].

## Fuente
Informe 01_manychat_dms_instagram.md (secciones 2.3, 2.7, 4.4, 6.3 Flujo E, 7) y 02_ghl_crm_y_redes.md (sección 8).

## Vigencia
2026-10-11.
