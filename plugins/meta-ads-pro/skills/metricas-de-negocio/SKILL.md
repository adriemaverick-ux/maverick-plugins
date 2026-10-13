---
name: metricas-de-negocio
description: Calcula MER, nCAC, margen de contribución y ROAS de equilibrio con fórmulas y ejemplo numérico. Usar antes de fijar presupuesto o metas, o cuando pregunten "cuál es mi ROAS de equilibrio", "MER", "nCAC máximo", "break-even ROAS", "margen de contribución", "estoy ganando dinero con Meta".
---

# Métricas de negocio

## Objetivo
Decidir presupuesto con economía real del negocio, no con el ROAS de plataforma. Calcular el techo de costo antes de tocar la cuenta.

## Pasos
1. **Pedir datos al usuario** (no suponerlos): AOV, margen bruto %, otros costos variables por pedido, margen de contribución objetivo, ingresos totales y gasto total de marketing del periodo.
2. **Fórmulas** [consenso las de MER y equilibrio; nCAC y payback: un experto, Eightx, vendor]:
   - MER = ingreso total / gasto total de marketing.
   - MER de equilibrio = 1 / margen de contribución.
   - ROAS de equilibrio (por plataforma) = 1 / margen de contribución sobre ingreso, con el mismo criterio.
   - nCAC máximo = AOV x margen bruto x margen de contribución objetivo.
   - Payback = CAC / (AOV x margen bruto).
   - LTV mínimo de referencia: al menos 3x CAC combinado (regla de pulgar).
3. **Ejemplo numérico del informe**: AOV 80, margen bruto 0,6, margen de contribución objetivo 0,5 → nCAC máximo = 80 x 0,6 x 0,5 = USD 24. Con 30% de margen de contribución el MER de equilibrio es 3,3; con 40%, 2,5.
4. **Calcular el techo de CPA** que el usuario puede pagar y usarlo como base para presupuesto de test (2-3x CPA por creativo) y reglas de pausa.
5. **Usar ROAS de plataforma solo para tácticas diarias**; decisiones de presupuesto con MER + nCAC + margen. [consenso]
6. **Comparar con la ventana correcta**: desde 2026 reportes con 7d_click/1d_view; no contra cifras antiguas con view-through largo. [analista]
7. **Contrastar con ventas reales**; para dudas de incrementalidad, holdout o prueba geográfica. CTC usa aMER e iROAS en vez de ROAS por anuncio. [un experto]
8. **Registrar supuestos** y marcar con [no verificado] cualquier benchmark externo usado.

## Plantillas / prompts
```
Entradas: AOV=__  margen bruto=__%  margen de contribución objetivo=__%
nCAC máx = AOV x margen bruto x margen contrib. objetivo
MER equilibrio = 1 / margen de contribución
Payback = CAC / (AOV x margen bruto)
```
Prompt: "Calcula nCAC máximo, MER de equilibrio y payback con estos datos, muestra cada paso y señala qué supuestos son míos y cuáles del usuario."

## Errores comunes
- Optimizar a ROAS de plataforma sin calcular el equilibrio. [consenso]
- Confundir ROAS de equilibrio de plataforma con MER (denominadores distintos).
- Tomar rangos de MER "3-5x" o ROAS de prospecting "1,8-3,0x" como metas universales: varían por categoría. [no verificado]
- Ignorar costos variables distintos al producto (envío, comisiones, devoluciones).
- Culpar a Meta por la caída de cifras tras el cambio de atribución 2026. [analista]

## Nivel de evidencia
Fórmulas MER y MER de equilibrio: [consenso]. nCAC, payback, LTV 3x: [un experto] (vendor Eightx). Benchmarks de MER/ROAS en frío: [no verificado]. Ejemplo numérico: ilustrativo, tomado del informe.

## Vigencia
2026-10-11. Las fórmulas son estables; los benchmarks no. Recalcular al cambiar precios, márgenes o costos de envío.
