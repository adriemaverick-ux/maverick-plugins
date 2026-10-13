---
name: saas-escala-y-techos
description: Explica cuánto gasto absorbe Meta para un SaaS antes de saturar: los 4 limitantes en orden y el techo en Perú con supuestos explícitos. Usar con "cuánto puedo escalar", "techo de mercado Perú", "scale Meta ads SaaS", "saturación de audiencia", "cuándo subir presupuesto".
---

# SaaS: escala y techos

## Objetivo
Estimar el techo de gasto y saber qué límite se rompe primero. Honestidad obligatoria: no encontré ningún caso público verificable de SaaS B2B a USD 100k+/mes con CAC y LTV publicados; lo cercano son apps de consumo y DTC.

## Pasos
1. **Los 4 limitantes, en este orden** (el primero que se rompe fija el techo):
   1. Económico: el CAC marginal sube con el gasto; si el último dólar no cumple el CAC objetivo, ese es el techo.
   2. Señal: ~50 eventos/semana/conjunto en el evento de optimización [un experto].
   3. Creativo: la saturación creativa llega antes que la de audiencia en cuentas amplias [un experto].
   4. Audiencia: ICP accionable por geografía/idioma/profesión; dominante en B2B de nicho y en Perú.
2. **Medir rendimientos decrecientes**: CPA por escalón. Ejemplo heurístico de Benly: +20% de gasto con CPA 25→27 es aceptable; si el siguiente escalón llega a 33, cerca del techo [un experto]. Aumentos ~20% cada 3-4 días; saltos grandes reinician aprendizaje [un experto, [no verificado] el 15-25%].
3. **Techo de audiencia**: gasto de saturación ≈ alcance accionable x frecuencia x CPM / 1.000, con frecuencia fría objetivo 2-4 [un experto]. Audiencia < 50.000 muy estrecha; < 100.000 satura rápido [un experto].
4. **Ejemplo con supuestos explícitos** [cálculo propio, no es dato de mercado]: ICP hipotético = 100.000 decisores; Meta alcanza 50%; frecuencia 3 → 150.000 impresiones. Con CPM USD 3,70 (Perú, [no verificado]) ≈ USD 555/mes; con CPM USD 12 (tope LatAm) ≈ USD 1.800/mes. Conclusión: un nicho B2B estrecho en Perú se agota en cientos o pocos miles de dólares de prospección fría. Rehacer con el ICP real y el alcance que muestre Ads Manager.
5. **SaaS masivo** (millones de pymes/creadores/estudiantes): techo mucho mayor, limitado por creatividad y LTV. Datos de contexto: Facebook ~29,5 M y Instagram ~12,4 M de usuarios en Perú (sep 2026) [benchmark/PE]; 2.346.592 empresas formales al cierre de 2024, 99,1% mypes [oficial/PE].
6. **Referencias de escala (ajenas a Perú)**: B2B early-stage prueba USD 3-5k/mes, techo "antes de unit economics claras" USD 30-50k/mes [un experto, EE. UU.]; apps con USD 100k+/mes con LTV ≈ 2-3:1 del gasto [un experto, consumo]; Videa cayó de USD 1M/mes a ~USD 300k/mes por saturación creativa [caso].
7. **Cómo escalan otros**: validar economía pequeña, creativos diversos, pasos de 10-20%, expandir geografía (México, Colombia, Chile para un SaaS peruano), financiar el payback antes de escalar [un experto].
8. **Validar incrementalidad** con holdout o test geográfico si hay dudas.
9. Todo aumento de presupuesto requiere aprobación humana explícita.

## Plantillas / prompts
```
ICP (personas): __  % alcanzable en Meta: __  Frecuencia: __  CPM: __ (fuente: propia)
Gasto de saturación/mes = alcance x frecuencia x CPM / 1000 = __
Limitante que se rompe primero: [economico | señal | creativo | audiencia]
```

## Errores comunes
- Subir presupuesto de golpe (caso SaaSrise: CAC USD 166 a 350-400).
- Mirar el promedio de cuenta mientras el costo marginal ya no paga.
- Usar el CPM de Perú como dato firme.
- Confundir "Meta puede gastar más" con "conviene gastar más".

## Nivel de evidencia
Débil. Mecanismos: [un experto]. Ejemplo de techo: [cálculo propio] con CPM [no verificado]. Casos: [caso] autorreportados. Perú: sin cifras de CAC de SaaS.

## Vigencia
2026-10-11.

## Skills relacionados
- `saas-economia-cac-ltv-payback`: define el CAC objetivo que marca el límite económico.
- `saas-creativos`: capacidad de producir conceptos distintos (límite creativo).
- `saas-plan-de-validacion`: prueba pequeña antes de pensar en escala.
