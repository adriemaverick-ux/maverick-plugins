---
name: costos-whatsapp-business
description: Úsala para entender y presupuestar costos de WhatsApp Business Platform - ventana de 24 h, ventana gratuita de 72 h de anuncios CTWA, plantillas y categorías. Gatillos - "cuánto cobra WhatsApp", "ventana 24 horas", "plantilla de WhatsApp", "free entry point", "WhatsApp pricing".
---

# Costos de WhatsApp Business (ventanas y plantillas)

## Objetivo
Presupuestar el costo de mensajería y diseñar seguimientos que no generen cargos innecesarios.

## Pasos
1. Modelo vigente: desde 2025-07-01 se cobra por mensaje de plantilla, no por conversación [oficial]. Mensajes que no son plantilla son gratis dentro de una ventana de servicio abierta (CSW).
2. CSW: 24 h desde el último mensaje del usuario. Dentro: mensajes de servicio y plantillas utility gratis. Fuera: solo plantillas, cobradas [oficial].
3. Free Entry Point (FEP): 72 h gratis si el usuario entró por anuncio CTWA o botón de Página de Facebook, desde app móvil (no desktop/web), y se responde dentro de las primeras 24 h; en esa ventana cualquier tipo de mensaje es gratis [oficial].
4. Categorías: Marketing (siempre cobrada), Utility (cobrada fuera de CSW), Authentication (cobrada). Meta decide la categoría; revisar antes de enviar [oficial].
5. Perú tiene tarifa propia y facturación en PEN desde 2026-04-01 [oficial]. Bajar la tabla oficial en PEN antes de presupuestar.
6. Desde 2026-10-01 los mensajes de servicio dentro de la CSW pasarían a ser cobrables con 1.000 gratis por mes por número, según terceros [no verificado contra Meta]. No aplica a la app gratuita.
7. Diseñar seguimientos: dentro de 24/72 h sin plantilla; después, plantillas con valor real (disponibilidad, vencimiento de cotización), con moderación y opt-in para marketing.
8. Con la app gratuita no se paga mensajería, pero no hay CAPI-BM ni webhooks.

## Plantillas / prompts listos
- Plantilla utility (borrador): "Hola {{1}}, tu reserva de la {{2}} vence el {{3}}. ¿Confirmamos?"
- Prompt: "Con el volumen estimado de plantillas al mes y la tarifa oficial en PEN que te paso, calcula el costo mensual por categoría. Si falta la tarifa, escribe [FALTA TARIFA] y no uses cifras de memoria."
- Regla práctica: responder rápido tiene ahorro directo (mantiene la FEP).

## Errores comunes
1. Responder tras 24 h: se pierde la FEP y se paga plantilla.
2. Usar tarifas de blogs sin contrastar con la tabla oficial.
3. Escribir plantillas de seguimiento con tono promocional y que Meta las reclasifique como Marketing.
4. Asumir que la ventana gratuita aplica desde desktop/web.
5. Operar con app gratuita y esperar optimización por compra.

## Nivel de evidencia
- [oficial] Modelo por plantilla, CSW 24 h, FEP 72 h, categorías, tarifa propia de Perú, PEN desde 2026-04-01.
- [no verificado] Tarifas de Perú: un post de LinkedIn da S/0.2339 marketing y S/0.0998 resto; Mercately da US$0.0703 y US$0.0300. Discrepan; no presupuestar con ellas.
- [no verificado] Cobro de servicio desde 2026-10-01 (fuentes de terceros coinciden).

## Checklist de presupuesto
- [ ] Tabla oficial de tarifas en PEN descargada y fechada.
- [ ] Volumen estimado de plantillas por categoría.
- [ ] Porcentaje de chats respondidos dentro de 24 h.
- [ ] Opt-in verificado para plantillas de marketing.
- [ ] Cambio del 2026-10-01 revisado contra la página oficial.

## Vigencia
2026-10-11. Las tarifas cambian por trimestre; verificar la página oficial de precios.
