---
name: entrega-recepcion-de-consultas-whatsapp
description: Úsalo para construir la recepción de consultas por WhatsApp con registro compartido, respuesta inicial fuera de horario, captura de datos y derivación a una persona, usando GHL y n8n/Make con canal oficial. Gatillos - "recepción de consultas", "respuesta fuera de horario", "WhatsApp con GHL", "inbound WhatsApp intake", "capturar datos para cotizar".
---

# Recepción de consultas por WhatsApp

## Objetivo
Que cada consulta quede registrada con responsable, estado y siguiente paso, y que quien escribe fuera de horario reciba una respuesta inicial clara. Reglas fijas primero; IA solo si aporta algo comprobable (por ejemplo, resumir para el responsable).

## Pasos
1. **Confirmar el canal oficial.** Usar la API oficial de WhatsApp Business vía GHL (ruta de coexistencia si ya usan la app, número nuevo o migración). No usar vías no oficiales como sesión de WhatsApp Web (riesgo de bloqueo del número y de términos de Meta) [oficial / video con riesgo señalado].
2. **Verificar costos antes de activar:** USD 10 al mes por sub-cuenta más tarifas de Meta por mensaje; desde 2026-10-01 los mensajes de servicio dentro de la ventana son facturables con un tramo gratis [oficial, reverificar en la cuenta]. Configurar alerta de saldo de la billetera.
3. **Crear el registro:** contacto, oportunidad en etapa "Nuevo", responsable, canal, fecha y hora, datos mínimos para cotizar (según sector, ver prop-adaptacion-por-sector), campo de consentimiento (sí/no, fecha, canal).
4. **Redactar la respuesta inicial por reglas:** identifica a la empresa, indica que es un asistente automático y que una persona continuará, pide los datos mínimos y enlaza el aviso de privacidad. Máximo 3 preguntas por mensaje.
5. **Respetar la ventana de 24 h:** cada mensaje del cliente la reabre; fuera de ventana, solo plantillas aprobadas. Un seguimiento humano a las 24 h o más requiere cuidado: la etiqueta Human Agent (7 días) aplica a Instagram y Messenger, no a WhatsApp [oficial]; verificar la regla de WhatsApp en la cuenta.
6. **Derivar a una persona** cuando el cliente pide hablar con alguien, menciona precio, contrato, queja o urgencia. Etiquetar, notificar al responsable y pausar la respuesta automática.
7. **Probar con datos de prueba**, luego con el equipo, usando URL de prueba y de producción por separado y datos fijados (pin) en n8n para no reenviar mensajes.
8. **Pedir confirmación humana** antes de activar en producción y registrar la versión de mensajes aprobada.

## Plantillas y prompts listos
**Mensaje inicial (ejemplo, ajustar al negocio):** "Hola, escribiste a [Negocio]. Soy el asistente automático: recibo tu consulta y una persona de nuestro equipo te responde [en horario X]. Para cotizar, ¿me indicas [dato 1], [dato 2] y [dato 3]? Tus datos se usan solo para atenderte; aviso: [enlace]. Si no quieres más mensajes, escribe BAJA."

**Reglas de derivación:** palabras de precio, contrato, queja, urgencia, o dos mensajes sin entender, derivan a una persona.

**Patrón técnico n8n:** Webhook (método correcto, POST) -> guardar mensaje e id de chat -> reglas -> Respond to Webhook; fijar datos de prueba; una espera aleatoria corta para no responder en milisegundos; memoria por id de chat solo si hay IA.

**Prompt para resumir (si se usa IA):** "Resume esta conversación en 3 líneas para el responsable: qué pide, datos faltantes, urgencia. No inventes precios ni plazos."

## Errores comunes
- Activar sin aviso de asistente automático ni consentimiento.
- Dejar que la IA responda precios, plazos o garantías.
- Prometer "respuesta en 60 segundos" como resultado sin medirlo.
- Mensajes promocionales fuera de ventana o sin plantilla aprobada.
- Dos herramientas respondiendo el mismo chat.
- Ofrecer a quien ya tiene menú automático lo mismo sin atender qué pasa después.

## Nivel de evidencia
- Recepción, respuesta fuera de horario, derivación a persona: Oferta, 2026-10-10 [decisión].
- Ventana de 24 h, Human Agent y costos de WhatsApp en GHL: informes 01 y 02 [oficial, con tarifa de utilidad de Perú [no verificado]].
- Patrón webhook + respond y pin de datos: videos de Jack Roberts, lotes 1 y 2 [video; la UI cambia].
- Agente de WhatsApp con Unipile: video, riesgo de bloqueo señalado en la extracción [no apto para producción].
- Reglas de la plataforma: canal oficial de WhatsApp, ventana de 24 h y plantillas aprobadas; los reportes de spam limitan el número [oficial]. Leyes peruanas de mensajería: decisión de Adrie de no tratarlas como bloqueo.

## Fuente
Maverick MP: Oferta; Decisiones consolidadas 2026-10-10. Maverick Research: 01_manychat_dms_instagram (2.2, 2.3, 5.3); 02_ghl_crm_y_redes (4.3, 9, 10.2). Jack Roberts: G_negocio_automatizacion_1 (video 4, 6, 9), _4 (D1, D3).

## Vigencia
2026-10-11. Reverificar precios, ventana y plantillas antes de cada despliegue.
