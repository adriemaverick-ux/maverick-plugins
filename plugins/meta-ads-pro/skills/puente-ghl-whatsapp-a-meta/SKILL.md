---
name: puente-ghl-whatsapp-a-meta
description: 'Cómo hacer que las ventas cerradas por WhatsApp en GoHighLevel (GHL) le lleguen a Meta con el ctwa_clid, usando un puente propio en Vercel, porque GHL no envía eventos de mensajería a la API de conversiones. Usar al conectar GHL con Meta Ads, al medir anuncios Click-to-WhatsApp vendidos en GHL o con "GHL Meta", "puente", "ctwa_clid GHL", "QualifiedLead desde GHL", "Compró en el pipeline".'
---

# Puente GHL → Meta para ventas por WhatsApp

## Objetivo
Que cada `QualifiedLead` y `Purchase` de un chat que nació en un anuncio Click-to-WhatsApp llegue **una sola vez** a Meta con su `ctwa_clid`, para que Meta aprenda a traer compradores y no solo gente que chatea.

## Lo que GHL hace y lo que no (verificado el 2026-11-13)
- **Sí:** lee el `ctwa_clid` para atribuir el origen como Paid Social [oficial: help.gohighlevel.com/support/solutions/articles/48001219997]; el disparador «Click to WhatsApp Ads & Facebook Page CTA» guarda el ID del anuncio y la campaña [oficial: …/155000005602].
- **No:** su acción de Conversions API solo trabaja con `fbclid` (web). Soporte lo llama «limitación conocida, sin fecha». Los pedidos para cambiarlo (abr-2025 y oct-2025) siguen abiertos [comunidad: ideas.gohighlevel.com].
- Un usuario reporta que el valor existe en `contact.attributionSource.ctwaClid` [no verificado]. Verificarlo con un contacto real antes de construir.

## Arquitectura
1. **Captura del `ctwa_clid`** (una de dos formas):
   - A) Un workflow de GHL con el disparador CTWA manda un webhook a `/api/ctwa` (Vercel) con `contactId`, teléfono y `{{contact.attributionSource.ctwaClid}}`, si existe.
   - B) Una app propia suscrita a la misma WABA, solo para escuchar el webhook `messages`. Lee `referral.ctwa_clid` del primer mensaje. Meta permite varias apps suscritas a una WABA (`/{WABA}/subscribed_apps`) [oficial]. La app **nunca responde mensajes** y deduplica, porque los reintentos llegan a todas las apps.
2. **Guardado:** se escribe en campos personalizados del contacto en GHL (`ctwa_clid`, `ctwa_fecha`, `ad_id`) por la API de GHL.
3. **Disparo:** en el pipeline, la etapa «Calificado» manda `QualifiedLead` y la etapa «Compró» manda `Purchase` con su monto. Cada uno es un webhook de workflow a `/api/evento-meta`.
4. **Envío:** `POST https://graph.facebook.com/v27.0/{DATASET_ID}/events` [oficial: developers.facebook.com/documentation/ads-commerce/conversions-api/business-messaging]:
   - `event_name` y `event_time` (la hora real del hito).
   - `action_source: "business_messaging"` y `messaging_channel: "whatsapp"`.
   - `user_data`: `{ ctwa_clid, whatsapp_business_account_id }`.
   - `custom_data`: `{ currency: "USD", value }` (obligatorio en Purchase).
   - El dataset se obtiene con `GET/POST /{WABA_ID}/dataset`.
5. **Deduplicación propia:** Meta no deduplica este canal. Guarda `evento + contacto + enviado_en` y no reenvíes.

## Datos mínimos por contacto
`ctwa_clid`, fecha del primer mensaje, `ad_id`, teléfono en E.164, etapa, valor de venta, `event_id` propio y estado de envío de cada evento.

## Pruebas
- Revisar que el evento aparezca en el dataset de la WABA (Events Manager) y leer la respuesta de Graph (`events_received`, `fbtrace_id`).
- La página oficial no menciona `test_event_code` para este canal [no verificado].
- Probar con un chat real nacido de un anuncio de prueba con presupuesto mínimo, con la aprobación de Adrie.

## Errores comunes
- Usar la app de WhatsApp Business del celular: no expone el `ctwa_clid`. Hace falta la API (Cloud API).
- Mandar los eventos tarde. Un proveedor dice que se descartan después de 7 días; Meta no lo confirma. Envía en el momento.
- Mandar un `value` inventado o inflado.
- Mezclar eventos web (píxel) y de mensajería en el mismo canal.
- Guardar el token en el código: va en variables de entorno de Vercel, con un usuario del sistema y permisos mínimos.

## Sin verificar
Si `attributionSource.ctwaClid` se puede usar en workflows o en la API; si una segunda app suscrita afecta a GHL; si en coexistencia (app + API) llega el `ctwa_clid`; si `whatsapp_business_manage_events` pide Advanced Access para uso propio (la documentación se contradice).

## Vigencia
2026-11-13. Revisar el changelog de GHL: si agrega soporte nativo para `ctwa_clid`, el puente sobra.

## Relacionados y aprobación humana
`capi-whatsapp-ventas-cerradas`, `calificacion-de-leads-whatsapp`, `campana-click-to-whatsapp`. Nada se activa ni se gasta sin la aprobación escrita de Adrie. Nota de la bóveda: `03 - Go-to-market/Meta Ads - medición y operación (cinturón negro) - 2026-11-13`.
