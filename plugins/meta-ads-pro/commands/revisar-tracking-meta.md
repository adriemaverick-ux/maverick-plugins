---
description: Revisa el tracking de Meta (Pixel, CAPI, deduplicación, EMQ, WhatsApp, atribución) y entrega hallazgos priorizados con acciones y verificación.
argument-hint: "[sitio/dataset/ruta de exportes o capturas] [web | shopify | whatsapp]"
---

Revisa el tracking de Meta de: $ARGUMENTS

1. Usa el agente `analista-medicion-meta` y los skills `pixel-y-capi-setup`, `deduplicacion-y-emq`, `capi-whatsapp-ventas-cerradas`, `verificacion-dominio-aem-y-eventos`, `atribucion-y-medicion` y `diagnostico-en-events-manager`.
2. Pide (si no se aportaron) datos mínimos: tipo de tienda/CRM, origen de CAPI, capturas de Test Events/Overview/EMQ, conteo de pedidos del backend, y si hay campañas CTWA.
3. Revisa: Pixel+CAPI al mismo dataset, `event_id` y dedup, parámetros y hash, EMQ de Purchase, value/currency, dominio y estado AEM, `content_ids` vs feed, `ctwa_clid` y eventos de mensajería, conectores con campos obsoletos (`7d_view`/`28d_view`).
4. Entrega: tabla de hallazgos (severidad, causa, acción, cómo verificar), checklist de salud técnica y próximos pasos.
5. Conserva etiquetas [oficial]/[analista]/[no verificado]; no inventes cifras; no propongas evadir políticas.
