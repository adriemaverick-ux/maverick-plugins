---
name: info-economia
description: Calcula la economía de un infoproducto: margen neto, CPA máximo, ROAS de equilibrio, reembolsos y comisiones de plataforma o afiliados. Usar cuando se pregunte "cuánto puedo pagar por venta", "CAC aceptable", "ROAS de equilibrio", "break-even ROAS course".
---

# Economía del infoproducto

## Objetivo
Fijar el CPA máximo y el ROAS de equilibrio desde el margen neto real, antes de gastar. Todas las fórmulas son [cálculo propio] con parámetros que mides tú.

## Pasos
1. Reúne: precio bruto `<PRECIO>`, IGV si aplica `<IGV>`, comisión de plataforma `<COM_PLAT>`, comisión de pasarela `<COM_PAS>`, afiliado `<COM_AFIL>`, costo de entrega por alumno `<ENTREGA>`, tasa de reembolso `<REEMB>`.
2. Ingreso neto = PRECIO − IGV − COM_PLAT − COM_PAS − COM_AFIL − ENTREGA.
3. Venta neta esperada = Ingreso neto × (1 − REEMB).
4. CPA de equilibrio = Venta neta esperada (solo primer pedido). Si cuentas recompra: + (LTV esperado − ingreso del primer pedido).
5. ROAS de equilibrio = PRECIO / CPA de equilibrio.
6. CPA máximo = CPA de equilibrio × (1 − margen de seguridad `<MARGEN_SEG>`), decidido por ti.
7. CAC aceptable por precio: no hay tabla de mercado fiable; el aceptable sale del paso 6 para tu precio. Si el CPA frío observado lo supera, cambia de embudo (skill `info-embudo-segun-precio`), no el volumen.
8. LTV a 90 días = ingreso neto 1er pedido + (aceptación bump × neto bump) + (tasa upsell × neto) + (renovación × meses × cuota neta) − reembolsos. Mídelo por cohorte; la prueba es el flujo de caja a 30-60 días.

## Ejemplo ilustrativo [cálculo propio, no benchmark]
Supuestos inventados para mostrar la fórmula: precio 100; plataforma 9.9% + 0.50 (tarifa publicada por terceros para Hotmart [benchmark]); sin afiliado; entrega 3; reembolso 10%.
- Comisión = 10.4; neto antes de reembolso = 100 − 10.4 − 3 = 86.6.
- Venta neta esperada ≈ 86.6 × 0.9 = 77.9 (simplificado: la comisión no siempre se devuelve).
- ROAS de equilibrio ≈ 100 / 77.9 = 1.28x en el primer pedido.
- Con afiliado, el margen cae y el ROAS de equilibrio sube: recalcula con tus números.

## Plantillas / prompts
- "Calcula CPA de equilibrio y ROAS de equilibrio con PRECIO=<x>, COM_PLAT=<y>, REEMB=<z>, ENTREGA=<w>; muestra cada paso y marca qué supuestos son míos."
- Tabla de control: `precio | neto | reembolso | CPA equilibrio | CPA real | decisión`.

## Errores comunes
- Usar el precio bruto como margen.
- Ignorar reembolsos, IGV y comisiones de afiliados.
- Medir por ROAS del día 1 en lugar de flujo de caja a 30-60 días.
- Copiar CPA de blogs como meta.

## Nivel de evidencia
- Fórmulas: [cálculo propio].
- Tarifas Hotmart (9.9% + USD 0.50; USD 0.10 si el producto cuesta USD 15 o menos): [benchmark] de pandavideo; verificar en el sitio de Hotmart. Otras cifras de Hotmart/Lemon Squeezy: [no verificado].
- Reembolsos: Udemy ~1-1.5% mensual y trading caro 20-30% son [un experto], anecdóticos.
- Benchmarks de CPA/ROAS del informe: [benchmark], no de Perú; no hay benchmark público de LTV de infoproductos.

## Vigencia
2026-10-11. Confirma tarifas por escrito; ningún gasto sin aprobación humana.

## Relacionados y aprobación humana
- Skills relacionados: `info-embudo-segun-precio`, `info-peru-pagos-y-legal`.
- Ningún gasto, lanzamiento ni cambio de presupuesto sin aprobación humana explícita.
- Si un dato falta, usa marcadores `<...>` y márcalo [no verificado]; no inventes cifras.
- Este skill no contiene promesas de ingresos ni técnicas de evasión de políticas.
