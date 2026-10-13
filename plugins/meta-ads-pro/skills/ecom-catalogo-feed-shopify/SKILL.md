---
name: ecom-catalogo-feed-shopify
description: Úsala para conectar, auditar o arreglar el catálogo/feed de Shopify en Meta - IDs que no coinciden (variant ID), retirar piezas vendidas, sincronización y píxel+CAPI. Gatillos - "catálogo Meta", "feed Shopify", "variant ID", "content_id", "producto agotado", "Commerce Manager", "dynamic ads".
---

# Catálogo y feed Shopify -> Meta

## Objetivo
Tener un catálogo limpio y sincronizado donde los IDs del píxel coincidan con los del feed, y donde las piezas vendidas dejen de servirse lo antes posible.

## Pasos
1. Antes de conectar, limpiar la tienda (ver `ecom-plan-90-dias-casa-soyer`): stock 0 o negativo, SKUs fantasma ($0 y stock 10), duplicados, fichas sin imagen.
   Un feed sucio contamina todo [Casa Soyer, auditoría 2026-09-19].
2. Requisitos de catalog ads: píxel/App Events con vistas, add-to-cart y compras;
   el product ID del píxel debe coincidir EXACTAMENTE con la columna ID del feed; `content_type` = `product` o `product_group` según el ID enviado [oficial, Meta Developers FAQ vía resumen].
3. Problema variant ID: el canal nativo de Shopify envía el variant ID como content_id, mientras el catálogo suele necesitar item group ID/product ID [un experto/comunidad Shopify].
   Soluciones: configurar el catálogo para aceptar variant IDs, o píxel personalizado/GTM con product_id.
   Verificar con Test Events.
4. Variantes: id único por variante y mismo `item_group_id`.
   No cambiar IDs entre actualizaciones: Meta los trata como productos nuevos y se pierde historial [un experto].
5. Un solo origen de píxel (sin código antiguo hardcodeado en el tema) y deduplicación con `event_id` compartido entre navegador y servidor [un experto;
   la doc oficial manda]. EMQ de Purchase >= 8 como meta de convención [benchmark].
6. Retirar vendidos: en piezas de 1 unidad, marcar vendida en Shopify (cantidad 0), pausar manualmente el anuncio y excluir el SKU del retargeting.
   La sincronización puede tardar hasta ~1 h y deja una "ventana de vendido" [un experto, Marpipe/AdAdvisor].
7. Usar conjuntos de producto filtrados a "in stock" [comunidad Shopify].
8. Imágenes: recomendado 1024x1024; el mínimo varía entre fuentes (500 vs 600) [no verificado].
9. Conciliar semanalmente Shopify vs Ads Manager y revisar Diagnósticos de Events Manager.

## Plantillas / prompts
- Prompt: "Audita este export del catálogo (CSV): lista SKUs con stock <= 0, precio 0, duplicados por título, sin imagen, y IDs no únicos.
   Solo lectura; no modifiques la tienda."
- Checklist de señal: píxel único; nivel de datos Mejorado/Máximo (con aviso de privacidad);
   Purchase llega por navegador y servidor y se deduplica; content_ids coinciden con catálogo.
- Protocolo "vendida": 1) Shopify a 0, 2) pausar anuncio, 3) quitar de conjunto de producto, 4) registrar en el CRM.

## Errores comunes
1. Subir el feed sin limpiar (SKUs fantasma, stock negativo).
2. Doble píxel o evento de servidor sin event_id: Purchase contado dos veces.
3. Asumir que el catálogo sirve para piezas únicas: con <20-30 SKUs activos y 1 unidad por SKU suele rendir más el anuncio por pieza o familia (umbral de criterio propio [no verificado]).
4. Cambiar IDs al "arreglar" fichas.
5. Fusionar o archivar en masa sin confirmación de Marbe/Ana (tienda de producción).

## Nivel de evidencia
- Requisitos de IDs y tipos: [oficial vía resumen]. Variant ID de Shopify: [un experto/comunidad].
   Ejemplo oficial de `checkout_completed` sin content_ids: [oficial Shopify vía búsqueda];
   la implicación es inferencia.
- Ventana de sincronización: [un experto]. Tamaño mínimo de imagen: [no verificado].

## Vigencia
2026-10-11. Confirmar con Test Events en la cuenta real antes de depender de cualquier ID.
