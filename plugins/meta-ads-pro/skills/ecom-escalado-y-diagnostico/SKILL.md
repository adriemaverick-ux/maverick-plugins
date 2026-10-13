---
name: ecom-escalado-y-diagnostico
description: Úsala cuando el ROAS o las ventas caen, o cuando haya que decidir cómo escalar una tienda de ticket alto. Gatillos - "cayó el ROAS", "ROAS bajo", "escalar presupuesto", "fatiga creativa", "diagnóstico", "scaling", "Black Friday".
---

# Escalado y diagnóstico cuando cae el ROAS

## Objetivo
Distinguir una caída real de un problema de medición, encontrar la causa en orden y escalar sin romper el equilibrio económico.

## Pasos de diagnóstico (orden, un cambio a la vez)
1. Confirmar que es real: 7 días vs 7 previos (14 vs 14 con poco volumen) [un experto].
2. Atribución y tracking: ¿cambió la ventana? Desde 12-ene-2026 no hay 7d view ni 28d view y desde marzo 2026 "click-through" es solo clic en enlace [oficial/Jon Loomer + secundario].
   Comparar conversiones Meta vs Shopify: si Shopify se mantiene y Meta cae, es reporting.
   Revisar Diagnósticos de Events Manager.
3. Eficiencia mezclada: MER y ventas totales de Shopify (sin Adelanto/Falabella).
4. Auditar cambios propios de los últimos 14 días: presupuestos, creativos, audiencias, eventos, precio, stock y tema.
5. Factores externos: CPM sube en toda la cuenta, estacionalidad, estado de la plataforma.
6. Fatiga: frecuencia, CTR, CPM, CVR y CPA por creativo;
   First-Time Impression Rate < 50% y frecuencia semanal > 3-4 como alarmas, con línea base propia [un experto, heurística].
7. Embudo post-clic: conversión de tienda, AOV, checkout, velocidad, stock agotado, métodos de pago, tiempo de respuesta en WhatsApp y tasa conversación -> cotización -> venta.
8. Estructura: señal por conjunto, solapamientos.

## Pasos de escalado
1. Preparación: ~50 eventos de optimización por semana por conjunto [un experto].
2. Vertical: +~20% cada 3-5 días (otras fuentes 15-25% cada 2-3 días) [un experto];
   los cambios grandes reiniciarían el aprendizaje (doc de Meta no verificada).
3. Horizontal: más piezas, familias, ángulos y zonas (distritos de Lima, provincias con envío cotizado).
   En ticket alto el techo es stock y nicho, no el algoritmo [razonamiento propio; Casa Soyer].
4. Nuevos conceptos cada 2-3 semanas con gasto alto;
   fatiga reportada en 2-3 semanas con gasto >= $200/día [benchmark vendor, no verificado].
5. Incrementalidad: con cuenta pequeña, prueba on/off por semanas o regiones mirando ventas totales, no solo Ads Manager [un experto].
   Conversion Lift y geo-holdout quedan para más volumen.
6. Q4/CyberWow: pruebas 3-4 semanas antes, rampa gradual, reglas de corte pre-aprobadas [un experto];
   CPM +3% a +11% en noviembre según Geist, +30-60% oct-dic en un agregado [benchmark].
7. Todo aumento de presupuesto requiere aprobación humana y el monto lo define el usuario.

## Plantillas / prompts
- Prompt: "Datos: periodo A vs B (gasto, conversaciones, calificadas, ventas Shopify).
   Recorre el diagnóstico 1-8, di en qué paso aparece la anomalía y propón un solo cambio."
- Reglas de corte (ilustrativas, calibrar): pausar un anuncio que gasta >= 3x el CPA de equilibrio sin conversación calificada;
   subir 20% si el CPA <= 80% del equilibrio por 3 días con eventos suficientes [ejemplos del informe, no universales].

## Errores comunes
1. Cambiar varias cosas a la vez.
2. Culpar al algoritmo sin conciliar con Shopify.
3. Escalar lo que no cubre el equilibrio.
4. Comparar periodos con ventanas de atribución distintas.
5. Iterar hooks en vez de conceptos (Andromeda favorece diversidad de conceptos [un experto, no oficial]).

## Nivel de evidencia
- Cambios de atribución: [oficial vía Jon Loomer] y varias fuentes concordantes.
   Heurísticas de escalado y fatiga: [un experto]/[benchmark vendor].
   Umbrales de "similaridad creativa" y "20+ anuncios/mes": [no verificado].

## Vigencia
2026-10-11.
