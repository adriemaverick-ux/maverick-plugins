---
tags: [casa-soyer, ecommerce, shopify, ads]
actualizado: 2026-09-19
---

# Ecommerce Shopify — Casa Soyer

## El plan presentado a los dueños

Este contenido se convirtió en un Claude Doc, hablando en primera persona
de Adrie hacia Ana/Marbe ("vamos a...", "voy a..."), para presentarlo como
propuesta de escalar Casa Soyer con ecommerce:
`https://claude.ai/code/artifact/f424a135-bcab-4a63-99d5-e1f66a2c6e68`.
Si piden "el plan" o "la propuesta", es ese doc — actualizarlo ahí en vez
de crear uno nuevo. Hay un skill corto `ecommerce-casa-soyer` que apunta a
esta nota y a ese doc.

## El hecho de negocio nuevo (2026-09-19)

Adrie va a trabajar con Casa Soyer (la marca de **productos**, `casasoyer.com`
— distinta de Studio Soyer, que vende servicios) por **comisión
sobre margen bruto**, corriendo pauta pagada y cerrando él mismo las ventas
de **ticket alto** por WhatsApp/CRM (tagueando los cierres él mismo). No es
su rol tocar Studio Soyer (servicios) — eso sigue siendo 100% de Ana/Gina.

Casa Soyer ecommerce corre en **Shopify**
(`casasoyer.com`, tienda `CasaSoyer`, plan Basic, Perú, USD)

## Auditoría del catálogo (vía MCP de Shopify, 2026-09-19)

**Catálogo:** 1,728 productos totales — 708 activos, 819 archivados, 201
draft. Mucha basura muerta que ensucia cualquier sync a Meta/Google.

**Inventario roto:**
- 388 de los 708 activos (55%) tienen stock = 0.
- Al menos 12 SKUs con **stock negativo** (tracking roto o vendido de más):
  Alfombra Yute (-1), Alfombra Telar (-1), Butaca negra con piel (-3),
  Coastal Juju (-1), FUNDA LIN GREY (-4), CAJA DE METAL (-1), Lámpara Bidar
  (-2), Vasija Nudo (-1), Cesta Efecto (-1), NAUJI (-1), FLORES MAGNOLIA
  (-1), Cubiertos de cobre (-1).
- Productos duplicados (misma pieza publicada 2-4 veces con precio
  distinto): Alfombra Atmosphere, Mesa Chimay, Alfombra Revive, Contenedor
  High (x3), Coastal Juju (x4), Sweeping Brush (x3), Mantel Bambú pack 4
  (x2).
- 9 productos activos con tag `missing-image`.

**~40 SKUs "fantasma":** precio $0.00 y stock fijo en "10" (mobiliario tipo
Poliform/Twils — Sillón Malvasia, Sofá Brezza Exterior, Aparador Self Up,
Mesa Manta Mármol Emperador, etc.). Son referencia de catálogo para
cotización/diseño, **no son comprables por checkout**. No deben estar
`active` ni sincronizarse al feed de ads.

**Inventario high-ticket real y vendible hoy (≥$1,000, stock > 0, precio
real):** ~48 piezas, casi todas con **stock = 1 unidad** — sofás
($2,800–$11,315, la más cara: "Sofá Marechiaro XIII — Configuración 6
Módulos" a $11,315), butacas/sillones ($1,050–$5,700), consolas
($1,950–$3,000), mesas ($1,200–$3,810), alfombras ($1,000–$6,000), obras de
arte ($1,000–$4,135). Ojo: al ser stock=1 por pieza, cada venta mata esa
campaña — no es catálogo replenishable, es más "galería curada" que
ecommerce tradicional.

**✅ Base de comisión resuelta (2026-09-20).** Margen bruto implícito por
el markup x3 (precio = 3×costo) es ~67% del precio de venta. El 40% que
mencionó Adrie es el **EBITDA del negocio completo** de Casa Soyer (después
de todos los gastos operativos) — un número de salud del negocio, NO la
base de la comisión. **La comisión de Adrie se calcula sobre el margen
bruto (~67%)**, no sobre el EBITDA. Tabla de ejemplo y el detalle en el
Google Doc del plan (sección "Cómo vamos a trabajar").

**Pregunta abierta, no bloqueante:** el "costo" usado para el x3, ¿incluye
flete/aduana hasta Lima o es solo costo de fábrica? Si es solo fábrica, la
comisión de Adrie sobre margen bruto podría ser una porción mayor de lo
que a Ana realmente le queda en piezas pesadas de importar (sofás, donde
el flete pesa más como % del precio) — no cambia el cálculo de Adrie, pero
vale la pena confirmarlo para que no haya fricción después.

**Costo/margen — bloqueante ORIGINAL para calcular la comisión (parcialmente resuelto arriba):** el campo de costo
por producto en Shopify está **vacío en 87% de la muestra**, y donde existe
aparece **más alto que el precio de venta** (ej. Lámpara RL1: precio
$1,912.50, costo cargado $3,465; Mesa Fosco: precio $725, costo cargado
$1,560) — probablemente error de moneda (costo en soles sin convertir,
precio en dólares), pero el punto es que **hoy es imposible calcular el
margen bruto real desde Shopify**. Antes de firmar % de comisión, pedir a
Ana/Marbe el costo real de importación+logística por pieza, no confiar en
este campo.

## Ventas — el "Adelanto" no es venta de catálogo

12 meses: $125,793.71 en ventas, muy irregular (5-12 órdenes/mes). Pero en
los últimos 90 días, **$42,708 de $51,058 (84%) no son ventas de
catálogo** — son line items manuales sin producto real, título en blanco,
tipo *"Adelanto rimadesio"* ($24,072) o *"Adelanto productos Ferm y HK
Living"* ($17,575), tags `EB01-2XX` — son **adelantos de proyectos de
Studio Soyer** cobrados por Shopify como atajo administrativo, no compras
generadas por tráfico/pauta.

**Importante para el contrato de comisión:** definir por escrito que estos
"Adelanto" quedan excluidos de la base de comisión de Adrie, y probablemente
también las ventas del canal Falabella (marketplace conectado, que Adrie no
maneja).

## Canales y tráfico

Ya conectados a Shopify: Online Store, POS, Buy Button, **Facebook &
Instagram**, **Google & YouTube**, Shop, **Falabella**. Infraestructura de
feed lista, pero:
- Tráfico últimos 90 días: 4,683 sesiones, **100% orgánico** (direct 3,277,
  search 1,054, social 302, unknown 50) — cero pauta paga histórica en
  ningún canal. Lienzo limpio, sin CAC/ROAS previo que comparar.
- 2,241 clientes en la base — suficiente para lookalikes/retargeting en
  Meta una vez conectado Pixel/CAPI (no auditado, requiere acceso directo a
  Meta Events Manager).
- Descuentos activos son casi todos el flow automático de carrito
  abandonado de Shopify — no hay oferta pensada para tráfico pago todavía.

## Meta vs. Google Ads — conclusión

**Meta gana para este catálogo específico**, no por default sino por la
naturaleza del producto:
- Comprar mueble de diseño es decisión visual/aspiracional, no búsqueda de
  necesidad puntual — nadie tipea el nombre de estas piezas en Google.
- Search genérico ("comprar sofá de diseño Lima") compite contra
  Sodimac/Promart/Maderart, que dominan esos términos con presupuestos de
  ticket bajo/medio.
- Meta permite lookalike de los 2,241 clientes reales + targeting por
  interés (diseño de interiores, decoración de lujo) — mejor motor de
  descubrimiento para una marca sin awareness instalada.
- Google Shopping/Performance Max no se debe prender hasta limpiar el feed
  (Google es más estricto que Meta con calidad de catálogo).

**Orden recomendado:** Meta/IG primero (barato de testear, formato visual) →
limpiar feed → Search en Google solo para tráfico de marca/alta intención
una vez validado → Performance Max/YouTube al final, si el volumen lo
justifica.

## El problema estructural del algoritmo con stock=1

Con inventario único (1 unidad por pieza) y bajo volumen de órdenes
(5-12/mes en TODA la tienda), **ningún algoritmo (Meta o Google) puede
optimizar sobre el evento "compra de esta pieza específica"** — ambos
necesitan volumen de conversiones por semana para salir de aprendizaje
(Meta: ~50/semana por conjunto de anuncios), y una pieza de stock=1 nunca
lo alcanza.

**La solución no es cambiar de plataforma, es cambiar el objetivo de
campaña:** optimizar por **mensaje/lead iniciado** (WhatsApp/Messenger), no
por compra. Eso sí acumula volumen suficiente para que el algoritmo
aprenda, y encaja con el modelo de Adrie: el algoritmo encuentra al lead
con perfil de comprador, Adrie cierra manualmente. En ticket bajo
tradicional es al revés — ahí SÍ hay volumen para optimizar directo por
compra y dejar que el algoritmo haga el embudo completo.

Esto también implica **carga de creativos alta y recurrente**: cada pieza
nueva necesita foto/copy propio (no hay "anuncio evergreen" reusable meses,
como en catálogo replenishable), y el creativo muere apenas se vende la
única unidad.

## Plan de limpieza profunda (pendiente de ejecutar)

**Fase 0 — decisiones de Ana/Marbe, no técnicas:**
- Costo real por pieza de las ~48 SKUs high-ticket.
- Definir exclusión de "Adelanto" y Falabella de la comisión de Adrie.

**Fase 1 — catálogo muerto:** decidir con Marbe qué borrar/reactivar de los
819 archivados + 201 draft.

**Fase 2 — SKUs fantasma:** pasar los ~40 productos $0/stock-10 a `draft` o
a una colección excluida del feed de ads.

**Fase 3 — inventario negativo:** conteo físico real de los 12 SKUs
listados arriba, corregir en Shopify.

**Fase 4 — duplicados:** fusionar o eliminar las fichas repetidas antes de
subir a Meta Catalog.

**Fase 5 — imágenes:** fotografiar los 9 SKUs activos sin imagen.

**Fase 6 — costo/margen:** cargar costo real en las 48 piezas priorizadas
para poder calcular comisión antes de gastar en pauta, no después.

**Ojo:** esto toca la tienda de producción real de Casa Soyer — cualquier
archivado/edición masiva se ejecuta con confirmación explícita de Marbe/Ana,
no solo de Adrie.

## Veredicto honesto sobre el potencial

Hay demanda real comprobada (ventas orgánicas sin pauta previa) y ~48
piezas genuinamente vendibles de ticket alto, con canales ya conectados. No
es un ecommerce tradicional escalable linealmente con presupuesto — es más
cercano a un modelo de "galería curada + venta consultiva": pocas ventas,
cada una grande, techo de escala limitado por cuánta pieza única tenga Ana
en stock, no por cuánto se gaste en ads. El único punto que puede tumbar el
negocio es el margen real (Fase 0) — la demanda y el modelo de venta
consultiva sí están validados.
