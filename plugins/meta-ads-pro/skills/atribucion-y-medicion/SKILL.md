---
name: atribucion-y-medicion
description: Usar para interpretar atribución de Meta tras los cambios de 2026, reconciliar Meta vs GA4 vs Shopify, calcular ROAS de equilibrio/MER y planear incrementalidad. Gatillos - "ventana de atribución", "7d_view", "Meta vs GA4", "ROAS de equilibrio", "incrementalidad", "conversion lift", "MER".
---

# Atribución, métricas de negocio e incrementalidad

## Objetivo
Tomar decisiones con margen y no solo con el ROAS de Meta, entendiendo qué cambió en la atribución y cómo contrastar fuentes.

## Pasos numerados
1. Conocer el cambio vigente [oficial vía ppc.land citando a Meta]: desde el 12-ene-2026 la API de Insights ya no devuelve `7d_view` ni `28d_view`; quedan 1d_click, 7d_click, 28d_click, 1d_engaged_view, 1d_view. Retención: 13 meses para desgloses de campos únicos y por hora, 6 meses para frecuencia, totales hasta 37 meses; `breakdowns=mmm` solo por trabajos asíncronos.
2. Auditar conectores y dashboards: los que piden `7d_view`/`28d_view` pueden devolver vacío sin error [analista].
3. Reconciliar Meta vs GA4 vs Shopify [analista]: misma ventana, solo clic (1d/7d click), rango cerrado, excluir pedidos no web (POS, borradores, suscripciones); usar Shopify como ancla de ingresos.
4. Calcular con margen de contribución (CM) [analista]: CM = ingreso neto - COGS - envío - comisiones de pago - devoluciones - descuentos (antes de publicidad). ROAS de equilibrio = 1 / CM %. ROAS objetivo = 1 / (CM % - % utilidad deseada). CPA máximo = CM por pedido.
5. Vigilar MER = ingresos totales / gasto total de marketing; si MER baja y el ROAS de Meta se sostiene, hay sobreatribución. Seguir nCAC (clientes nuevos), payback y LTV:CAC (3:1 como referencia [analista]).
6. Ticket alto por WhatsApp: costo por conversación -> por conversación calificada -> por venta cerrada; tasa de cierre = ventas / conversaciones.
7. Incrementalidad: Conversion Lift de Meta aleatoriza test y control (un A/B test no mide incrementalidad por no haber holdout) [oficial]; o geo holdout de diseño propio [analista]. iROAS = ingresos incrementales / gasto; úsalo para calibrar el ROAS reportado.
8. MMM: Robyn (Meta, open source, MIT) solo si hay presupuesto y varios canales; con una cuenta pequeña, MER + lift/holdout aportan más [analista].

## Checklists
- [ ] CM % por producto/familia, no solo promedio.
- [ ] ROAS de equilibrio y objetivo publicados por campaña.
- [ ] MER semanal y nCAC mensual.
- [ ] Reglas de corte con margen de seguridad por atribución inflada.
- [ ] Prueba de incrementalidad planificada (ej. trimestral si el gasto lo permite).

## Errores comunes
- Usar margen bruto en vez de CM (puede duplicar el ROAS necesario) o restar la publicidad dentro del CM y luego usar 1/CM.
- Ignorar devoluciones; evaluar solo con ROAS de Meta (es bruto).
- Comparar fuentes con ventanas y fechas distintas.
- Atribuir a la baja de 15-40 % en conversiones reportadas un deterioro real: el rendimiento real no cambió [analista].

## Cuándo escalar a una prueba formal
- Si MER y ROAS de Meta divergen de forma sostenida.
- Antes de subir presupuesto de forma importante.
- Documenta ventana, fechas y fuente usadas en cada reporte.

## Nivel de evidencia
- [oficial] Cambio de ventanas ene-2026 y retenciones (vía ppc.land); mecánica de Conversion Lift.
- [analista] Fórmulas, razones de discrepancia, MER/nCAC, Robyn, geo holdout, rango 15-40 %.
- [no verificado] "1d engage-through" desde 2026 y "clic = solo clics de enlace" (una sola fuente); requisitos mínimos de elegibilidad de Conversion Lift; fecha del anuncio según blogs (oct-2024 vs oct-2025; la oficial citada es oct-2025).

## Vigencia
2026-10-11.
