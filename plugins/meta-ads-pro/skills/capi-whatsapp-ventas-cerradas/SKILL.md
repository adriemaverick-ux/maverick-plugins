---
name: capi-whatsapp-ventas-cerradas
description: Usar para medir y optimizar anuncios Click-to-WhatsApp (CTWA) enviando a Meta las conversiones reales (QualifiedLead, Purchase) desde tu CRM con ctwa_clid. Gatillos - "ctwa_clid", "CAPI WhatsApp", "ventas cerradas por WhatsApp", "business messaging", "enviar compra desde CRM".
---

# CAPI para WhatsApp: ventas cerradas

## Objetivo
Cerrar el ciclo: que Meta reciba una vez cada evento (calificación y venta) de conversaciones nacidas en un anuncio CTWA, para optimizar por calidad y no solo por conversaciones.

## Pasos numerados
1. Obtener/crear el dataset desde el WABA ID (`/{WABA_ID}/dataset`); un dataset por Page [oficial].
2. Token con permisos `whatsapp_business_management` y `whatsapp_business_manage_events` (Advanced Access); Cloud API recomendada. Con On-Premises API, `ctwa_clid` solo desde Biz API 2.45.1 [oficial].
3. Al primer mensaje entrante, leer el objeto `referral` del webhook y GUARDAR `ctwa_clid` (y `source_id`, `source_type`, ID del anuncio) junto a la conversación en el CRM. Los mensajes siguientes pueden no repetirlo [analista].
4. Definir el pipeline en CRM: Conversación -> QualifiedLead -> (opcional InitiateCheckout/OrderCreated) -> Purchase.
5. Enviar `POST https://graph.facebook.com/v16.0/{DATASET_ID}/events` (la doc muestra v16: verificar versión vigente) con: `event_name`, `event_time` real, `action_source: business_messaging`, `messaging_channel: whatsapp`, `user_data` {`whatsapp_business_account_id`, `ctwa_clid`}, `custom_data` {`currency`, `value`} en Purchase, y `partner_agent` si eres partner [oficial].
6. Pagos fuera del chat (transferencia, tienda): registrar en CRM/ERP y enviar Purchase con el `ctwa_clid` guardado [oficial].
7. Deduplicar tú mismo: llevar un registro (conversación + evento + estado de envío) para enviar cada evento una sola vez; Meta no deduplica este canal [oficial].
8. Enviar rápido: guardar el ID y reportar etapas sin demora. Ventana de 7 días tras el clic para enviar eventos con ese ID: [analista] [no verificado oficial].
9. Comprobar que el evento aparece en el dataset del WABA y en Resultados/columnas personalizadas; revisar respuesta de Graph (`events_received`, `fbtrace_id`).
10. Calcular métricas de negocio: costo por conversación, por conversación calificada y por venta cerrada = gasto / ventas cerradas; comparar con margen bruto por venta.

## Checklists
- [ ] `ctwa_clid` guardado por conversación desde el primer mensaje.
- [ ] Un evento por hito, sin reenvíos.
- [ ] Purchase con `value` y `currency` reales.
- [ ] Eventos de sitio web por CAPI web, no por este canal.
- [ ] Opt-in claro y webhook `account_update` suscrito.
- [ ] Token en gestor de secretos, permisos mínimos.

## Errores comunes
- No guardar `ctwa_clid` o mandar eventos sin él.
- Reenviar el mismo evento (sin dedup).
- Mezclar eventos web y de mensajería en el mismo canal.
- Optimizar por Purchase en Instagram Direct (no soportado; sí en WhatsApp y Messenger) [oficial].
- Enviar valores de venta no reales o inflados.

## Datos mínimos a guardar por conversación
- `ctwa_clid`, fecha del primer mensaje, ID de anuncio, etapa y valor de venta.

## Nivel de evidencia
- [oficial] Endpoint, permisos, parámetros, lista de eventos (Purchase, LeadSubmitted, InitiateCheckout, AddToCart, ViewContent, OrderCreated, OrderShipped, OrderDelivered, OrderCanceled, OrderReturned, CartAbandoned, QualifiedLead, RatingProvided, ReviewProvided), no deduplicación.
- [analista] Que `ctwa_clid` no se repita en mensajes posteriores; ventana de 7 días.
- [no verificado] Umbral de ~10 compras en 7 días para optimizar CTWA por compra; Advanced Access 500 vs 1.500 llamadas (la doc se contradice).

## Vigencia
2026-10-11.
