---
name: ecom-ticket-alto-pieza-unica
description: Úsala para vender piezas únicas o de ticket alto con Meta - anuncio por pieza o familia, Click-to-WhatsApp y eventos de CRM por CAPI. Gatillos - "pieza única", "stock 1", "ticket alto", "CTWA", "lead calificado", "anuncio por pieza", "high ticket".
---

# Ticket alto y pieza única

## Objetivo
Generar conversaciones de calidad para piezas de 1 unidad, enseñar a Meta qué conversaciones se convierten en ventas y evitar que un anuncio siga vivo tras la venta.

## Pasos
1. Aceptar el problema estructural: con 5-12 órdenes/mes en toda la tienda, ningún algoritmo optimiza por "compra de esta pieza";
   hacen falta ~50 eventos/semana por conjunto [un experto, heurística; Casa Soyer].
2. Elegir el objetivo: Click-to-WhatsApp (conversaciones) y devolver eventos de CRM (lead calificado, cotización, venta) por Conversions API [un experto].
   Meta no ve lo que ocurre en WhatsApp si no se lo envías [un experto].
3. Regla de decisión: optimizar por la etapa más profunda con ~50 eventos/semana por conjunto;
   si no llega, subir una etapa (conversación calificada o cotización) [un experto; razonamiento propio].
4. Formato: anuncio por pieza para piezas ancla (historia, escala, procedencia);
   anuncio por familia/colección (3-6 piezas) para reutilizar creativo y aprendizaje y reducir desperdicio tras una venta;
   catálogo/DPA solo para retargeting [un experto + razonamiento].
5. Instrumentar CAPI de mensajería con el identificador de clic (`ctwa_clid`) [un experto;
   documentación oficial no localizada, [no verificado]].
   Ver también los skills `campana-click-to-whatsapp` y `capi-whatsapp-ventas-cerradas` del plugin.
6. Etiquetas de CRM: lead, calificado, cotización, venta, motivo de pérdida.
   Medir tiempo de primera respuesta y conversión conversación -> cotización -> venta por anuncio.
7. Operación de vendida: marcar vendida, pausar anuncio, excluir del retargeting, reponer creativos (cada venta elimina un anuncio).
8. Creativo: abordar objeciones de escala, color, calidad y "cómo se ve en casa" con vistas de habitación y referencias de tamaño [un experto].
   Probar UGC vs pulido [un experto, fuentes en conflicto].
9. Escasez solo si es real; en lujo, la urgencia agresiva puede dañar posicionamiento [un experto, sin consenso].

## Plantillas / prompts
- Prompt: "Para la pieza [PIEZA] (precio [PRECIO], stock 1, ficha adjunta), propón 3 conceptos distintos (escala, historia, en la casa), copy corto con CTA a WhatsApp y mensaje de bienvenida.
   Sin cifras inventadas."
- Mensaje de bienvenida: "Hola, te escribo por [PIEZA].
   ¿La quieres para [ESPACIO]? Te comparto medidas, fotos reales y entrega en [ZONA]."
- Eventos a enviar: lead, calificado, cotización, compra con `value` y `currency`.

## Errores comunes
1. Medir solo chats iniciados y celebrar un costo por conversación bajo.
2. No devolver calidad a Meta: optimiza por curiosos.
3. Anuncios activos de piezas vendidas.
4. Iterar hooks en vez de conceptos nuevos.
5. Atribución: con ciclos de 30-60 días se pierden conversiones;
   conciliar con Shopify/CRM y con "¿cómo nos conociste?" [un experto].

## Nivel de evidencia
- CTWA + CAPI de CRM: [un experto/vendor]; cifras de mejora de proveedores (15-20%, 2,4x): [no verificado].
- Umbral 50 eventos/semana: [un experto].
   No existe benchmark público de piezas únicas en Meta [no verificado]: probar en cuenta propia.

## Vigencia
2026-10-11.
