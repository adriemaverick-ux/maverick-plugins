---
name: pixel-y-capi-setup
description: Usar al implementar o revisar Pixel de Meta + Conversions API (CAPI) en una web o tienda Shopify, y para decidir el orden de implementación. Gatillos - "instalar pixel", "configurar CAPI", "conversions api setup", "server-side tracking", "Gateway vs GTM server".
---

# Pixel + CAPI: orden de implementación

## Objetivo
Dejar Pixel (navegador) y CAPI (servidor) activos y redundantes sobre el mismo dataset, con parámetros correctos y verificados en Test Events.

## Pasos numerados
1. Fase 0: Business Portfolio del cliente con 2 administradores reales y 2FA; verificación de negocio y de dominio; pago estable; política de privacidad, contacto y devoluciones publicadas.
2. Crear/confirmar UN solo dataset (Pixel) por negocio/dominio; evitar pixeles duplicados.
3. Elegir origen de CAPI:
   - Shopify estándar: app Facebook & Instagram con nivel de datos **Máximo** (pixel + CAPI) [oficial: Shopify Help].
   - Rápido sin servidor propio: CAPI Gateway [analista: Stape].
   - Varias plataformas y control de parámetros: GTM server-side (4-8 h de setup y 10-50 USD/mes aprox., cifras [analista] sin verificar).
   - Ventas fuera del sitio (WhatsApp/CRM): ver skill `capi-whatsapp-ventas-cerradas`.
4. Elegir UN solo origen de eventos de servidor (si hay app nativa + GTM server o tercero, hay riesgo de duplicados salvo `event_id` compartido).
5. Capturar `fbclid` -> `_fbc` en la primera visita y persistirlo; capturar `_fbp`.
6. Enviar por evento: `event_name`, `event_time` real, `action_source` correcto, `event_id`, `external_id`, `event_source_url` y `client_user_agent` (web) [oficial].
7. `user_data`: hash SHA-256 normalizado en `em`, `ph`, `fn`, `ln`, `db`, `ge`, `ct`, `st`, `zp`, `country`; SIN hash: `client_ip_address`, `client_user_agent`, `fbc`, `fbp`.
8. `Purchase` con `value` (numérico) y `currency` (ISO 4217) y `order_id`; `content_ids` alineados con el feed.
9. Validar en Test Events (ver skill `diagnostico-en-events-manager`) y revisar deduplicación (ver `deduplicacion-y-emq`).
10. Fase 2-3: catálogo (content_ids = id del feed), UTMs dinámicos, listas de compradores y exclusiones.

## Checklists
- [ ] Pixel y CAPI al mismo dataset, un solo origen de servidor.
- [ ] `event_id` generado una vez por acción y reutilizado en servidor.
- [ ] Hash correcto; IP/UA/fbc/fbp sin hash.
- [ ] `fbc`/`fbp` persistidos y refrescados.
- [ ] Purchase con value+currency+order_id.
- [ ] Dominio verificado.
- [ ] Eventos de prueba vistos como Browser y Server.

## Errores comunes
- Combinaciones inválidas de parámetros (por ejemplo `db`+`client_user_agent` solos) hacen que el evento se rechace [oficial].
- Eventos con `event_time` demasiado antiguo (más de 7 días) o futuro [analista; verificar en doc].
- Hashear IP, user agent, fbp o fbc; hashear dos veces.
- Email sin normalizar; teléfono sin código de país.
- Enviar solo la compra y no el embudo completo.
- Token expirado, permisos faltantes o dataset equivocado.
- Creer que Gateway o GTM mejoran la EMQ por sí solos: depende de los campos enviados [analista].

## Nivel de evidencia
- [oficial] Parámetros, hash/no hash, redundancia Pixel+CAPI, requisitos por evento (docs de CAPI y Shopify).
- [analista] Comparativa Gateway/GTM, costos y horas, límite de 7 días de `event_time`.
- [no verificado] Alcance exacto de eventos que Shopify "Máximo" envía por servidor en cada tienda: comprobar en Events Manager.

## Vigencia
2026-10-11. Meta cambia pantallas y versiones de API con frecuencia: validar cada paso en tu interfaz.
