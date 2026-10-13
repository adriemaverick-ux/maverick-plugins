---
name: casa-soyer-ecommerce
description: Contexto base del negocio de ecommerce/pauta de Casa Soyer (casasoyer.com, marca de PRODUCTOS de Ana Teresa Vega Soyer, distinta de Studio Soyer que es servicios). Adrie corre pauta paga por comisión sobre margen bruto y cierra personalmente ventas de ticket alto. Usar siempre que se hable de ads, Meta/Google, tienda Shopify casasoyer-5595, comisión, Tiers de catálogo, importación o escalar Casa Soyer. NO usar para Studio Soyer (servicios).
---

# Casa Soyer — Ecommerce (negocio paralelo de Adrie)

La fuente de verdad detallada es `${CLAUDE_PLUGIN_ROOT}/references/ecommerce-casa-soyer.md`. Léela antes de auditar, planear o gastar en pauta; al terminar, actualízala (no crear notas sueltas).

## Hechos clave
- **Casa Soyer** = productos (casasoyer.com, Shopify, plan Basic, Perú, USD). **Studio Soyer** = servicios de diseño; NO es parte de este trabajo.
- Adrie gana por **comisión sobre margen bruto (~67%, markup x3)**, NO sobre el EBITDA (40% es salud del negocio, no base de comisión).
- Corre pauta paga y cierra él mismo las ventas de **ticket alto** por WhatsApp/CRM, tagueando sus cierres.
- Excluidos de la base de comisión (dejarlo por escrito): los **"Adelanto"** (adelantos de proyectos de Studio Soyer cobrados por Shopify; 84% de las ventas de los últimos 90 días) y el canal **Falabella**.
- Catálogo: 1,728 productos (708 activos, 819 archivados, 201 draft). ~48 piezas high-ticket vendibles, casi todas stock=1: es una "galería curada + venta consultiva", no ecommerce escalable linealmente.
- Tráfico 90d: 4,683 sesiones 100% orgánicas; cero pauta histórica. 2,241 clientes en base.
- **Meta/IG primero**, optimizando por **mensaje/lead iniciado (WhatsApp)**, no por compra (stock=1 impide que el algoritmo aprenda). Google Shopping/PMax solo tras limpiar el feed.
- **Bloqueante:** el costo por producto en Shopify está vacío (87%) o mal cargado. Pedir costo real de importación+logística a Ana/Marbe antes de firmar % o gastar fuerte.
- Pregunta abierta: ¿el "costo" del x3 incluye flete/aduana hasta Lima?
- Plan presentado a los dueños: Claude Doc https://claude.ai/code/artifact/f424a135-bcab-4a63-99d5-e1f66a2c6e68 (actualizar ahí, no crear otro).

## Reglas de trabajo
1. Tienda de producción real: toda escritura (archivar, editar, inventario) pide confirmación explícita; ediciones masivas necesitan OK de Marbe/Ana.
2. Advertir siempre riesgos técnicos: nombrar qué se rompe, qué queda sin resolver y límites de escala. Nunca vender algo como perfecto.
3. No mencionar a Casa Soyer/Ana como cliente único en copy público de otros negocios de Adrie.
4. Todo en español. Setup manual de cuentas lo hace Adrie; tú preparas research y copy listo para pegar.

## A quién delegar
- Auditoría de catálogo/feed → subagente `auditor-catalogo`.
- Estrategia y estructura de campañas → `estratega-pauta`.
- Anuncios y copy por pieza → `creativo-pieza`.
- Comisión y números → `analista-comision`.
