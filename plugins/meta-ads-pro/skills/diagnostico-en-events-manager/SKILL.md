---
name: diagnostico-en-events-manager
description: Usar para diagnosticar problemas de tracking en Events Manager y para correr el checklist de salud técnica de una cuenta. Gatillos - "revisar tracking", "Test Events", "eventos duplicados", "catálogo 0 matched", "checklist de salud técnica", "events manager diagnostics".
---

# Diagnóstico en Events Manager y checklist de salud técnica

## Objetivo
Detectar rápido fallos típicos (duplicados, EMQ bajo, eventos rechazados, desajustes con el backend) y cerrar con un checklist de salud.

## Pasos numerados
1. Events Manager > Dataset > Test Events: generar `test_event_code`; confirmar origen (Browser/Server) y marca de deduplicación. Usar tus propios datos, pues eventos de prueba no emparejados pueden descartarse [oficial].
2. Pestaña Overview: eventos por fuente; el mismo evento debe verse en Browser y Server; % deduplicado > 0 con ambos activos.
3. Revisar EMQ, "parámetros recibidos", Diagnostics, frescura, cobertura de eventos y Conversiones adicionales reportadas (ACR) [oficial].
4. Cotejar conteo del dataset vs pedidos reales de Shopify/CRM; una desviación sostenida indica fallo [analista].
5. Meta Pixel Helper para ver `content_ids`, `value`, `event_id`; logs del servidor con `events_received` y `fbtrace_id`.
6. Para CTWA: evento visible en el dataset del WABA y en Resultados.
7. Aplicar la tabla de síntomas.

## Síntomas y causas
| Síntoma | Causa probable | Solución |
|---|---|---|
| Compras duplicadas | event_id distinto/ausente; dos integraciones | Un solo origen o event_id compartido; mismo event_name |
| Dedup = 0 | Un solo canal activo o IDs no coinciden | Verificar en Test Events |
| EMQ bajo | Faltan email/teléfono, IP/UA, fbp/fbc | Capturar y enviar con hash correcto |
| Eventos rechazados | Combinación inválida de parámetros | Añadir user agent + identificador fuerte |
| Catálogo "0 matched" | content_ids distinto del id del feed | Alinear variante/producto |
| WhatsApp no atribuye | Falta `ctwa_clid` o ventana vencida | Guardar al primer mensaje, enviar pronto |
| Server events de Shopify no llegan | Conexión app/dataset | Revisar conexión y probar |
| Throttling API | Ráfagas | Backoff y menos escrituras |
| Valores de compra raros | Impuestos/descuentos/moneda | Alinear `value` y `currency` |

## Checklist de salud técnica
- [ ] Portafolio verificado, admins con 2FA, Account Quality sin restricciones, pago vigente y de respaldo.
- [ ] Pixel disparando en páginas clave; CAPI activo; deduplicación > 0; EMQ Purchase con objetivo 8+.
- [ ] Dominio verificado; estado AEM comprobado en la cuenta.
- [ ] Purchase con value/currency; `content_ids` alineados al feed.
- [ ] WhatsApp: `ctwa_clid` guardado, eventos enviados una vez, dataset enlazado.
- [ ] Conteo backend vs Meta; UTMs consistentes; conectores sin `7d_view`/`28d_view`.
- [ ] Alerta si eventos caen a 0 o divergen del backend.

## Errores comunes
- Diagnosticar solo con el ROAS de Meta sin contrastar con backend.
- Probar sin datos de cliente reales y concluir que "no empareja".
- Dos orígenes de servidor activos.

## Nivel de evidencia
- [oficial] Test Events, Diagnostics, Dataset Quality API, alineación de IDs de catálogo.
- [analista] Tolerancia de desviación vs backend, objetivo EMQ 8+, comportamiento de Shopify en comunidad.
- [no verificado] Umbrales exactos de alerta; texto de la ayuda oficial de EMQ (no legible).

## Vigencia
2026-10-11.
