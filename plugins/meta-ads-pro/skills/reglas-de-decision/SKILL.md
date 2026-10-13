---
name: reglas-de-decision
description: Reglas para decidir cuándo pausar, mantener o escalar anuncios y conjuntos de Meta Ads, con advertencias. Usar cuando pregunten "pausar o no este anuncio", "cuándo escalar", "kill rules", "scale rules", "el CPA subió", "frecuencia alta".
---

# Reglas de decisión

## Objetivo
Dar reglas explícitas, con su fuente y contradicciones, para pausar o escalar sin reaccionar al ruido. Ninguna acción de gasto se ejecuta sin confirmación humana.

## Pasos
1. **Ventana mínima**: no decidir en las primeras 48-72 h; una compra puede mover el CPA 50% o más. [consenso]
2. **Muestra mínima antes de juzgar**: 3 días y ~2.000 impresiones, o 50-100 clics, o 3-5 compras por creativo; gasto 2-3x CPA objetivo. [un experto: Motion / consenso débil]
3. **Pausar (fallas duras)**: sin entrega, rechazo de política, CTR muy bajo, landing rota, tracking caído. Acordado en ambas posturas. [juicio de síntesis sobre dos posturas de expertos]
4. **Pausar (regla de Motion)**: 48-72 h con CTR <50% del control, o CPA >25% peor que el objetivo. [un experto] **Advertencia**: CTC afirma no apagar por ROAS histórico porque el sistema ya redujo su asignación. [un experto] Discrepancia abierta: preferir pausar solo ante falla dura o evidencia sostenida, y documentar.
5. **Fatiga**: frecuencia 3-4 en pocas semanas como alarma [un experto, secundaria]; la solución es rotar conceptos, no subir puja. Ciclo de refresco 2-3 semanas. [consenso]
6. **Diagnóstico antes de actuar**: hook <25% cambiar apertura; hook alto y hold bajo, arreglar el medio; cruzar hold con duración media de visualización. [un experto]
7. **Escalar** solo si: CPA estable (referencia 5-7 días), nCAC marginal bajo el techo de `metricas-de-negocio`, y sin cuello de botella creativo. Condiciones numéricas de vendors (50+ conv./semana, frecuencia <2,5): [no verificado].
8. **Paso de escala**: 10-20% cada 3 días (rango de blogs 10-25%). [consenso débil, no oficial] Agrupar ediciones en una sola por semana. Cambios grandes pueden reiniciar el aprendizaje.
9. **Si el gasto se estanca**: más diversidad conceptual, luego duplicar evergreen con otra puja, y solo al final relajar ROAS/cost cap. [un experto: CTC]
10. **Registrar** cada decisión (fecha, métrica, regla, resultado) y pedir al usuario aprobación explícita del cambio de presupuesto o pausa.

## Plantillas / prompts
```
Decisión: [pausar|mantener|escalar]  Objeto: __  Datos: gasto=__ conv.=__ CPA=__ frec.=__
Regla aplicada: __ (fuente/etiqueta)   Riesgo: __   Requiere confirmación humana: SÍ
```
Prompt: "Evalúa este anuncio con las reglas, di cuál aplica, qué advertencia contradice y recomienda sin ejecutar."

## Errores comunes
Apagar en 24 h por 2-3 conversiones; editar a diario; escalar con saltos grandes; apagar anuncios que gastan poco porque el sistema los relegó, sin evaluar concepto; ignorar el cambio de atribución al comparar semanas.

## Nivel de evidencia
Ventanas de espera: [consenso]. Umbrales de Motion: [un experto]. No apagar por ROAS histórico: [un experto: CTC]. Pasos de escalado y condiciones numéricas: [consenso débil] y [no verificado]. No son reglas oficiales de Meta.

## Vigencia
2026-10-11. Ajustar umbrales con el historial de la propia cuenta.

## Notas de uso
- Ante duda entre pausar y mantener, mantener y recolectar más datos salvo falla dura.
- Reportar siempre qué regla se aplicó y su etiqueta de evidencia.
- Revisar los umbrales con el historial propio de la cuenta tras 90 días.
- Las acciones sobre gasto solo con aprobación humana explícita.
- No usar estas reglas en cuentas con restricciones o avisos de política sin resolver antes ese tema por los canales oficiales.
- Registrar cada decisión con fecha para poder revisar la regla aplicada.
- Si los datos son contradictorios, pedir aclaración antes de recomendar.
