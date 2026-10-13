---
name: auditoria-catalogo
description: Audita el catálogo Shopify de Casa Soyer para pauta - stock cero o negativo, duplicados, SKUs fantasma ($0 / stock 10), productos sin imagen, costos mal cargados, y clasifica piezas en Tiers 1/2/3. Usar antes de conectar o subir cualquier feed a Meta/Google, o cuando se pida "auditar la tienda".
---

# Auditoría de catálogo

Lee primero `${CLAUDE_PLUGIN_ROOT}/references/ecommerce-casa-soyer.md` (línea base del 2026-09-19).

## Pasos (solo lectura)
1. Conteo: productos totales/activos/archivados/draft.
2. Stock: activos con stock=0 (% del total) y stock negativo (lista de SKUs).
3. Duplicados: misma pieza con 2+ fichas.
4. Fantasmas: precio $0 y stock fijo 10 → no comprables, deben salir del feed.
5. Imágenes: activos con tag `missing-image` o sin imagen.
6. Costo/margen: campo costo vacío o > precio (probable error soles vs dólares).
7. High-ticket real: precio ≥ $1,000, stock > 0, precio real → lista priorizada.
8. Tiers: 1 = se vende self-served (ej. alfombras); 2 = ayuda de WhatsApp; 3 = necesita visita/showroom (ej. sofás).
9. Comparar contra la línea base y reportar qué mejoró/empeoró.

## Salida
Tabla por hallazgo con severidad, cantidad, SKUs afectados y fase del plan de limpieza que lo resuelve. Cierra con "qué NO pude verificar" (ej. Pixel/CAPI de Meta sin acceso a Events Manager).

Solo lectura: para corregir, usar `limpieza-catalogo`.
