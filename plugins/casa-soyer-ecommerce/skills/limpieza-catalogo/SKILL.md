---
name: limpieza-catalogo
description: Ejecuta el plan de limpieza de la tienda Shopify de Casa Soyer por fases (catálogo muerto, SKUs fantasma, stock negativo, duplicados, imágenes, costos) con dry-run y confirmación explícita. Usar solo cuando se pida corregir la tienda.
---

# Limpieza de catálogo (tienda de PRODUCCIÓN)

Antes de tocar nada: correr `auditoria-catalogo` y mostrar el plan.

## Fases
0. Decisiones de Ana/Marbe: costo real de las ~48 piezas, exclusión de Adelanto/Falabella.
1. Catálogo muerto: decidir qué borrar/reactivar de 819 archivados + 201 draft.
2. Fantasmas ($0/stock 10): pasar a `draft` o colección excluida del feed.
3. Stock negativo: requiere **conteo físico real** antes de corregir.
4. Duplicados: fusionar/eliminar fichas repetidas antes de subir a Meta Catalog.
5. Imágenes: fotografiar los activos sin imagen.
6. Costo/margen: cargar costo real en las piezas priorizadas.

## Protocolo obligatorio
- Siempre **dry-run primero**: lista exacta de productos/IDs y el cambio propuesto.
- Pedir confirmación explícita por fase; ediciones masivas requieren OK de Marbe/Ana.
- Preferir reversible (draft/archivar) sobre borrar; nunca borrar definitivamente sin pedido expreso.
- Guardar un respaldo (export de IDs y estado previo) antes de aplicar y reportar al final qué se cambió y qué falló.
