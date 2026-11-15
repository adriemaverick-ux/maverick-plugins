---
name: tablero-costo-por-venta
description: Diseño del tablero propio que junta el gasto de Meta por anuncio con las ventas reales (pasarela y GHL) para ver costo por venta, por lead calificado y por concepto, y decidir qué cortar o escalar. Usar al armar reportes de pauta, al decidir pausar o escalar, o con "tablero", "dashboard", "costo por venta por anuncio", "qué anuncio vende".
---

# Tablero de costo por venta

## Objetivo
Saber **qué anuncio trae plata**, no cuál trae clics. Meta reporta conversiones atribuidas; el tablero cruza eso con las ventas que de verdad entraron.

## Fuentes de datos
1. **Gasto por anuncio y día:** Meta Insights por `ad_id` (gasto, impresiones, clics en el enlace, ThruPlay y retención a 3 s si existe). Se lee en **solo lectura** con el MCP oficial de Meta Ads o con la Marketing API (`/insights?level=ad&time_increment=1`).
2. **Ventas web (kit):** webhook de la pasarela. El `ad_id` llega porque la URL del anuncio usa los parámetros dinámicos de Meta: `?utm_source=meta&utm_campaign={{campaign.name}}&utm_content={{ad.id}}`. La página lo guarda y lo pasa a la metadata del checkout.
3. **Ventas por WhatsApp (web):** GHL. El disparador CTWA guarda el `ad_id` en el contacto, y el pipeline marca Calificado y Compró con su monto.
4. **Reembolsos:** webhook de la pasarela.

## Almacenamiento (simple)
Una base chica (por ejemplo Supabase, plan gratis) con dos tablas:
- `gasto(fecha, ad_id, ad_nombre, concepto, hook, gasto, impresiones, clics, thruplay)`.
- `resultados(fecha, ad_id, tipo[lead|calificado|compra|reembolso], valor, oferta[kit|web], origen[web|whatsapp])`.

Una función programada en Vercel (cron diario) trae el gasto del día anterior. Las ventas entran solas desde los webhooks.

## Lo que muestra
- Por **anuncio** y por **concepto** (nombre del anuncio: `concepto_hook_formato`, por ejemplo `desglose_hookB_9x16`):
  - Gasto.
  - Costo por lead.
  - Costo por lead calificado.
  - **Costo por venta**.
  - Ingresos y ROAS real (ingreso / gasto).
- Semáforo contra el **CPA máximo** (kit ≈ US$70; web: según margen).
  - Verde: por debajo del CPA máximo.
  - Amarillo: hasta 1,5×.
  - Rojo: más de 2× sin ventas.
- Tendencia de 7 días frente a los 7 anteriores y la frecuencia (fatiga).
- Puede publicarse como Artifact privado de tipo tablero o como página propia.

## Métricas personalizadas y lectura [un experto: Adrián Sáenz y Roger Viladrosa, tutorial de jul-2024; bóveda `04 - Conocimiento/02 - Hallazgos/Meta Ads - aprendizajes del tutorial de Adrián Sáenz (2024-07)`]
- **Visitas a la página de destino ÷ clics en el enlace:** si la diferencia es grande, hay clics falsos o la web carga lento.
- **Leads ÷ vistas de página** en la calculadora (referencia del autor: 29–30 % es bueno en captación).
- **Evento propio en el botón «Háblame por WhatsApp»** después de la calculadora (referencia del autor: ~61 % de los registrados hace clic).
- **Leer la ventana de «7 días menos los 3 últimos»:** los últimos 3 días aún no tienen toda la atribución, y las ventas por WhatsApp llegan tarde.
- **Una métrica estrella por oferta:**
  - Kit: costo por compra y ROAS.
  - Web: costo por conversación calificada o por venta devuelta por la API, no el ROAS que muestra Meta.
- **ROAS blended** (todo lo vendido ÷ lo gastado) como respaldo cuando falla la atribución del chat.
- **Columnas propias por embudo**, desde la métrica estrella hacia arriba del embudo, guardadas como predeterminadas.

## Reglas
- No declarar ganador con pocos eventos: menos de unas 10 conversiones por anuncio es ruido.
- Antes de explicar una caída, revisar el registro de cambios: campañas terminadas o presupuestos modificados (ver `workflows-claude-meta-ads`).
- El tablero **propone**; Adrie decide y aprueba cualquier cambio de gasto.

## Errores comunes
- No poner `{{ad.id}}` en la URL: las ventas web quedan sin anuncio.
- Contar la conversación como venta.
- Usar la atribución de 7 días de clic + 1 de vista para premiar el retargeting.

## Vigencia
2026-11-13. Diseño, todavía no construido.

## Relacionados y aprobación humana
`reglas-de-decision`, `metricas-de-negocio`, `mcp-meta-ads-solo-lectura`, `puente-ghl-whatsapp-a-meta`. Solo lectura sobre Meta; ningún cambio sin aprobación escrita.
