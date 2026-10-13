---
name: cierre-ticket-alto-por-chat
description: Úsala para redactar guiones, mensajes de bienvenida, seguimientos y manejo de objeciones al cerrar ventas de ticket alto por WhatsApp (mueble, decoración, inmobiliario). Gatillos - "cerrar venta por WhatsApp", "seguimiento de cotización", "objeción de precio", "mensaje de bienvenida", "follow-up", "responder lead".
---

# Cierre de ticket alto por chat

## Objetivo
Convertir conversaciones calificadas en ventas con velocidad, poca fricción y seguimiento con valor. Todo texto se entrega como borrador: nunca se envía nada al cliente sin confirmación humana.

## Pasos
1. Velocidad: auto-respuesta inmediata con expectativa clara; humano en menos de 5 min en horario comercial y menos de 15 min fuera de pico. Fuera de horario, decir la hora exacta de respuesta. Responder dentro de 24 h mantiene la ventana gratuita de 72 h [oficial].
2. Bienvenida: hasta 4 ice breakers, máx. 80 caracteres, sin emojis (confirmar en WhatsApp Manager). Ejemplos: "Ver disponibilidad", "Medidas y materiales", "Agendar visita al showroom", "Entrega a mi distrito".
3. Guion de 6 pasos: (1) saludo y contexto de la pieza; (2) 2-3 preguntas de calificación, una por mensaje; (3) valor: foto o video real, medidas, materiales, disponibilidad, entrega; (4) precio con contexto, formas de pago y garantía; (5) cierre suave con alternativa; (6) postventa: confirmar datos, registrar Purchase, pedir reseña.
4. Pago de ticket alto: transferencia/CCI, link de pago con tarjeta, cuotas o reserva con adelanto. No asumir Yape.
5. Seguimiento: días 3 y 7 y antes del vencimiento de la cotización, aportando valor (foto real, disponibilidad). Tope 3-4 toques; luego pasa a retargeting.
6. Fuera de 24 h (o 72 h FEP) solo plantillas aprobadas y cobradas (ver skill `costos-whatsapp-business`).
7. Objeciones: precio, confianza, plazo (ver plantillas). Registrar el motivo de pérdida en CRM.

## Plantillas / prompts listos
- Bienvenida automática: "Hola, soy [nombre] de [marca]. Te ayudo con la [pieza]. ¿Para qué distrito sería la entrega y en qué fecha la necesitas? Respondo en minutos de [horario]."
- Cierre suave: "¿Prefieres reservarla hoy con adelanto o pasar a verla al showroom el [día/hora]?"
- Precio: "La [pieza] está en S/[precio]. Se puede pagar con tarjeta, transferencia o cuotas, e incluye [garantía]. Entrega en [distrito]: [plazo]."
- Objeción de confianza: "Si prefieres, hacemos una videollamada y te la muestro en vivo, o la ves en el showroom."
- Objeción de plazo: "Es una pieza de stock casi único; hoy está disponible. Puedo reservarla hasta el [fecha] con un adelanto." Usar solo si el stock es real.
- Seguimiento día 3: "Hola [nombre], te comparto una foto real de la [pieza] en ambiente. Sigue disponible; ¿te resuelvo alguna duda de medidas?"
- Prompt: "Redacta 3 variantes de respuesta a este mensaje del cliente [pegar], tono cercano y breve, con una sola pregunta. No inventes stock ni precios; usa [DATO FALTANTE]. Solo borrador, no enviar."

## Errores comunes
1. Mensaje de bienvenida genérico que rompe la promesa del anuncio.
2. "Te paso la cotización" sin dar rango de precio.
3. Seguimientos que solo dicen "¿ya decidiste?".
4. Urgencia falsa; Meta puede rechazarla y se pierde confianza.
5. Responder tarde y perder la ventana gratuita.

## Nivel de evidencia
- [oficial] Ventana FEP de 72 h y reglas de plantillas; ice breakers (80 caracteres, confirmar en WhatsApp Manager).
- [benchmark] "21x" proviene de InsideSales 2007 con datos de proveedor, mal atribuido a MIT; HBR 2011: respuesta media 42 h, 37% responde en la primera hora. La dirección es sólida, el multiplicador no.
- [no verificado] El guion de 6 pasos y la cadencia día 3/día 7 son propuestas basadas en guías de proveedores, no un método validado.

## Checklist antes de enviar (lo hace Adrie)
- [ ] Precio, stock y plazo confirmados; sin [DATO FALTANTE].
- [ ] Una sola pregunta por mensaje.
- [ ] Ventana de 24 h/72 h vigente, o plantilla aprobada elegida a propósito.
- [ ] Ningún mensaje se envía sin confirmación humana.
- [ ] Etapa y motivo de pérdida anotados en CRM.

## Vigencia
2026-10-11.
