---
name: verificacion-dominio-aem-y-eventos
description: Usar para verificar el dominio, decidir si aún aplica la priorización de eventos AEM y configurar eventos de valor y conversiones personalizadas. Gatillos - "verificar dominio", "AEM", "Aggregated Event Measurement", "priorizar 8 eventos", "domain verification", "optimización por valor".
---

# Verificación de dominio, AEM y eventos

## Objetivo
Dejar el dominio verificado y los eventos (con valor) correctamente definidos, sin depender de reglas de AEM que pueden haber cambiado.

## Pasos numerados
1. Verificar el dominio de la tienda en Business Settings (DNS TXT o meta-tag). Aunque ya no sería obligatorio para configurar eventos web, sigue recomendado por control de propiedad de enlaces y compatibilidad [analista: Jon Loomer]; [no verificado oficial].
2. Revisar en TU Events Manager si todavía aparece la pestaña AEM.
3. Si aparece: mantener priorización por orden de valor (Purchase, InitiateCheckout, AddToCart, ViewContent, Lead) hasta confirmar el cambio.
4. Si no aparece: reportes [analista] indican que ya no hace falta priorizar 8 eventos por dominio para optimización web ni value sets. El modelo de 8 eventos para apps iOS: [no verificado].
5. Eventos de valor: Purchase con `currency` (ISO 4217) y `value` numérico; en Shopify el valor es el total con impuestos, envíos y descuentos [oficial].
6. Optimización por valor y value rules: ajustan valor por audiencia/ubicación/dispositivo; no admiten ciertos objetivos previos (ROAS objetivo, bid cap) ni categorías especiales (vivienda, empleo, financiero); útiles solo con tracking estable [analista].
7. Conversiones personalizadas: definirlas por URL/regla sobre eventos estándar para reporte o audiencias; no sustituyen al evento estándar para optimizar [analista].
8. Catálogo: `content_ids` del pixel = columna `id` del feed (variante vs producto según corresponda); `content_type` product o product_group; conectar el dataset en Commerce Manager > Eventos > Administrar conexiones [oficial].

## Checklists
- [ ] Dominio verificado.
- [ ] Estado de la pestaña AEM comprobado en la cuenta real.
- [ ] Purchase con value+currency; valores coherentes con el backend.
- [ ] content_ids alineados al feed (objetivo de coincidencia cercano a 100 %).
- [ ] Un solo dataset conectado al catálogo.

## Errores comunes
- Asumir que AEM desapareció (o que sigue igual) sin mirar la cuenta.
- `value` como texto, moneda faltante, o impuestos/descuentos mal tratados.
- IDs de variante en el pixel y de producto en el feed (catálogo "0 matched").
- Usar conversión personalizada como si fuese evento de optimización.

## Registro recomendado
- Anota fecha de verificación del dominio y quién la hizo.
- Captura de la pantalla de AEM (o su ausencia) con fecha.
- Lista de eventos activos y su valor en moneda.

## Nivel de evidencia
- [oficial] Requisitos de value/currency y alineación content_ids con feed (Omni Setup Guide, Shopify).
- [analista] Cambios de AEM, value rules, conversiones personalizadas. Tasa de coincidencia: Omni dice más de 90 % [oficial]; otra fuente dice 75 % [analista, conflicto].
- [no verificado] Alcance exacto del cambio AEM (iOS/apps); confirmación oficial pendiente.

## Vigencia
2026-10-11.
