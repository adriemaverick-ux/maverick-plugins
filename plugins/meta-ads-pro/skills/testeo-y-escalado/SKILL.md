---
name: testeo-y-escalado
description: Marcos concretos para testear creativos y escalar presupuesto en Meta Ads, con las discrepancias entre expertos. Usar cuando se pida "cómo testear creativos", "escalar campaña", "3-2-2", "explorar explotar amplificar", "testing framework", "scale budget", "cuántos anuncios".
---

# Testeo y escalado

## Objetivo
Dar un proceso de testeo de conceptos y de escalado gradual, mostrando dónde los expertos no coinciden para que el usuario decida con criterio.

## Pasos
1. **Marco Explorar - Explotar - Amplificar.** Explorar: validar persona y ángulo. Explotar: iterar ejecución (hooks de 3-7 s, estilo, formato). Amplificar: llevar el ángulo validado a nuevas personas/productos. [un experto: Manchi/Motion]
2. **Brief de 5 dimensiones**: etapa de consciencia, estado emocional, formato, producto/caso de uso, persona. Prueba rápida: si todos los anuncios activos se describen en una frase, hay clustering. [un experto: CTC]
3. **Testear concepto primero, variantes después.** Orden sugerido: hook (oferta fija) > formato > prueba social > oferta > escala. [un experto]
4. **Volumen según gasto** (referencia de vendors): <USD 10k/mes: 8-12 creativos nuevos al mes; 10-50k: 15-25; >50k: 25-40+. Con USD 100/día, ~4 tests/semana y 10-15 anuncios por conjunto. [un experto, vendors con interés comercial]
5. **Presupuesto de testeo**: 10-20% del gasto pasado USD 100k/mes; win rate ~1 de 10. [un experto, secundaria]
6. **Juzgar** con 2-3x el CPA objetivo por creativo y mínimo 3 días; no tocar en 48-72 h. [consenso débil / consenso]
7. **Diagnóstico**: hook <25% cambiar apertura; hook alto con hold bajo, arreglar el medio. [un experto: Motion]
8. **Escalar vertical**: 10-25% cada 2-5 días (heurística de blogs, no regla de Meta); antes, agregar 3 hooks nuevos y 2 formatos. [consenso débil, no oficial]
9. **Si el gasto se estanca** (orden de CTC): más diversidad conceptual; duplicar evergreen con otra puja (lowest cost / bid cap / cost cap); ASC de un conjunto; relajar ROAS/cost cap al final. [un experto]
10. **Validar** con holdout o prueba geográfica ante dudas de atribución o retargeting. [juicio de síntesis]

## Discrepancias entre expertos (decidir explícitamente)
| Tema | Postura A | Postura B |
|---|---|---|
| Cuántos anuncios | Loomer: no hay número mágico; Precis: 3 conceptos de inicio | Kruse/Motion: 50-100 al mes; Foxwell: 40-50 concurrentes a USD 1.000/día |
| ABO vs CBO al testear | Manchi/Motion: ABO test, CBO escala | Foxwell/Kiel: CBO primero |
| Apagar anuncios | CTC: no apagar por ROAS histórico | Motion: pausar si CTR <50% del control o CPA 25% peor tras 48-72 h |
| Exclusiones/retargeting | CTC: mantener exclusiones y retención | Charley T: sin exclusiones, solo amplio |
| 3-2-2 | Vigente para validar ángulo | Solo un piso, no estrategia |
| Causa de caídas 2025-26 | Kruse: falta de volumen/diversidad | Loomer: oferta, estacionalidad, competencia |
Lectura práctica: pausar solo por fallas duras (sin entrega, política, CTR muy bajo); el CPA malo del día 1 no es motivo.

## Plantillas / prompts
- "Genera 5 conceptos distintos (persona x ángulo x etapa x formato) para [producto]; descríbelos en una frase cada uno para comprobar que no se agrupan."
- "Con gasto diario X y CPA objetivo Y, calcula presupuesto mínimo por creativo (2-3x CPA) y cuántos tests caben por semana."

## Errores comunes
Juzgar con 2-3 conversiones; creer que 20 versiones = 20 conceptos; saltos grandes de presupuesto; probar hook, formato, oferta y audiencia a la vez; escalar con cuello de botella creativo. [consenso]

## Nivel de evidencia
Marcos: [un experto] (Manchi, CTC, Kruse, Tichenor). Cifras de volumen y "65% más ROAS con 20+ anuncios": [no verificado] (sin estudio original). Hook/hold: [un experto]. Pasos de escalado: [consenso débil]. Toda acción que cambie presupuesto requiere confirmación humana.

## Vigencia
2026-10-11. Benchmarks de hook/hold cambian rápido; compararlos con el promedio de 90 días de la propia cuenta.
