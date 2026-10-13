---
name: auto-whatsapp-api-en-ghl
description: Usar al configurar WhatsApp Business API dentro de GoHighLevel: costos, ventana de servicio, plantillas, coexistencia y consentimiento. Gatillos "WhatsApp en GHL", "plantillas de WhatsApp", "ventana de 24 horas WhatsApp", "WhatsApp API costs", "coexistencia".
---

# WhatsApp API en GHL

## Objetivo
Usar WhatsApp para continuar y cerrar conversaciones ya iniciadas, con plantillas aprobadas y consentimiento, controlando costos del wallet. Ningún mensaje saliente se envía sin aprobación humana del flujo y de la plantilla.

## Pasos
1. Elegir la ruta de onboarding embebido: coexistencia con la app WhatsApp Business (importa contactos e historial, un solo número, plantillas solo desde el CRM, perfil se edita en la app), número nuevo, o migrar desde otro BSP. [oficial]
2. Cargar el wallet con alerta de saldo mínimo; revisar costos semanalmente el primer mes.
3. Crear 3-5 plantillas y clasificarlas bien: bienvenida, recordatorio de visita (utilidad), seguimiento de cotización, confirmación de demo. Marketing y utilidad tienen tarifas distintas. [oficial]
4. Respetar la ventana de servicio de 24 h (se reinicia con cada mensaje del cliente). Fuera de ella, solo plantillas aprobadas. [oficial]
5. Entry points gratuitos (Click-to-WhatsApp o CTA de Facebook): ventana de 72 h con mensajes gratis si se responde dentro de 24 h. [oficial]
6. Registrar el consentimiento antes de mensajes promocionales y ofrecer baja ("STOP"). Ver auto-cumplimiento-peru.
7. Conversation AI puede atender WhatsApp, pero en modo borrador primero; sus respuestas dentro de la ventana también cuentan como mensajes de servicio.
8. Seguimiento de cotización: +2, +5 y +10 días; detener si el cliente responde (condición "Customer Replied").

## Costos (verificar en la cuenta)
| Concepto | Valor | Etiqueta |
|---|---|---|
| Suscripción de WhatsApp en GHL | USD 10/mes por sub-cuenta | [oficial] |
| Recargo GHL del 5% | Eliminado desde 2026-10-01; se paga la tarifa de Meta | [oficial] |
| Mensajes de servicio dentro de la ventana | Facturables desde 2026-10-01; primeros 1.000 por número/mes gratis | [oficial] |
| Perú, marketing | USD 0,0738 por mensaje (tabla vigente hasta 2026-09-30) | [oficial] |
| Perú, utilidad | USD 0,0210 hasta 2026-09-30; tarifa desde 2026-10-01 | [no verificado] |
| Llamadas por WhatsApp a Perú iniciadas por la empresa | USD 0,0127/min; las iniciadas por el usuario son gratis | [oficial] |
| Plan GHL Starter | USD 97/mes | [oficial] |

## Plantillas/ejemplos
Recordatorio (utilidad): "Hola {{nombre}}, te recordamos tu visita técnica el {{fecha}}. Responde 1 para confirmar o 2 para reprogramar."
Seguimiento de cotización: "Hola {{nombre}}, ¿pudiste revisar la propuesta que te enviamos? Estamos para resolver tus dudas. Para no recibir más mensajes responde STOP."

## Errores comunes
- Enviar promoción fuera de la ventana sin plantilla o sin consentimiento: bloqueos y baja calidad del número. [oficial general]
- Olvidar que ahora los mensajes de servicio se cobran: un bot muy conversador cuesta más.
- En coexistencia, intentar enviar plantillas desde la app.
- Prometer "chat desde Google": Google Business Messages cerró el 2024-07-31.
- Chatbots de IA de propósito general en WhatsApp prohibidos desde 2026-01-15; los bots de negocio acotados siguen permitidos. [vendor/comunidad]
- Suponer SMS en Perú: tarifa y cobertura no verificadas.

## Nivel de evidencia
Costos y ventana: [oficial] (help center y changelog de GHL, Meta). Tarifa de utilidad en Perú desde octubre 2026, pasarelas de pago en Perú y SMS a Perú: [no verificado]. Simulación de costos de IA con tráfico real pendiente.

## Fuente
Informe 02_ghl_crm_y_redes.md (secciones 4.3, 7, 8.3, 9).

## Vigencia
2026-10-11. HighLevel y Meta cambian tarifas con frecuencia.
