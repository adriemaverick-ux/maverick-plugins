---
name: deduplicacion-y-emq
description: Usar cuando hay compras duplicadas, deduplicación en 0, EMQ bajo o dudas sobre event_id y parámetros de cliente. Gatillos - "deduplicar eventos", "event_id", "Event Match Quality", "EMQ bajo", "subir EMQ", "duplicate events".
---

# Deduplicación y Event Match Quality (EMQ)

## Objetivo
Evitar doble conteo entre Pixel y CAPI y aumentar la calidad de emparejamiento sin inventar datos.

## Pasos numerados
1. Método 1 (recomendado) [oficial]: el `eventID` del Pixel (4.º argumento de `fbq`) debe ser igual al `event_id` de CAPI; el `event` igual al `event_name`; mismo Pixel ID. Se descarta el segundo evento.
2. Generar el `event_id` UNA vez por acción (en el cliente) y pasarlo al servidor junto con la solicitud (p. ej. en el pedido o la sesión).
3. Método 2 (respaldo) [oficial]: mismo `event_name` + `fbp` y/o `external_id`; funciona sobre todo si el evento del navegador llega primero; no deduplica duplicados dentro de la misma fuente.
4. Ventana de deduplicación web: 48 h desde el primer evento recibido [oficial]. Si el contenido difiere poco, se prefiere el primero recibido.
5. Eventos offline: se deduplican solo contra offline (clave `dataset_id`+`event_time`+`event_name`+`item_number`+`order_id`, ventana 7 días); un evento por pedido [oficial].
6. Mensajería/WhatsApp: Meta NO deduplica; hazlo en tu sistema antes de enviar [oficial].
7. Subir EMQ [analista salvo hash]: enviar `em`, `ph`, `external_id`, `fbc`, `fbp`, IP y user agent reales; capturar email/teléfono en checkout o formularios con consentimiento; activar coincidencia avanzada automática; mantener frescura de `fbp`/`fbc`.
8. Verificar: Test Events (origen Browser/Server y marca de deduplicado), pestaña Overview (porcentaje deduplicado > 0 con ambos canales activos), EMQ y "parámetros recibidos" por evento, Dataset Quality API para monitoreo programático [oficial].

## Checklists
- [ ] Mismo `event_name` exacto y mismo `event_id` en navegador y servidor.
- [ ] `external_id` estable (hash recomendado) en todos los eventos.
- [ ] Normalización: email en minúsculas sin espacios; teléfono solo dígitos con código de país; `db` YYYYMMDD; `country` ISO alfa-2 minúscula.
- [ ] IP, user agent, `fbc`, `fbp`, `ctwa_clid`, `lead_id` sin hash.
- [ ] EMQ de Purchase con objetivo 8+ sin datos falsos o de relleno.

## Errores comunes
- `event_id` distinto en cada lado o generado por separado.
- Dos integraciones del servidor activas a la vez (nativa + tercero).
- Hash doble o hash de campos que no se hashean.
- Rellenar o inventar datos para inflar el score: no hacerlo; EMQ mide completitud y formato, no veracidad [analista].
- Dedup en 0 porque solo un canal está activo o los IDs no coinciden.

## Prueba rápida de deduplicación
- Dispara una compra de prueba con `test_event_code`.
- Debe aparecer un evento Browser y uno Server con el mismo `event_id`.
- Si aparecen sin marca de deduplicado, compara `event_name` y `event_id` carácter por carácter.

## Nivel de evidencia
- [oficial] Mecánica de dedup (event_id/event_name, 48 h, método 2, offline, mensajería sin dedup), parámetros y hash.
- [analista] Escala EMQ 0-10 solo servidor, objetivos "6 mínimo / 8+ en Purchase" (otras fuentes dicen 7+), tácticas para subirlo.
- [no verificado] Umbral oficial de EMQ (la página oficial no fue legible); mejoras porcentuales de matching por campo.

## Vigencia
2026-10-11.
