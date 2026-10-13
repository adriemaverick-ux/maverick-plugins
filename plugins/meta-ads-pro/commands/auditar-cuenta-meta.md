---
description: Audita una cuenta de Meta Ads con checklist, puntaje y plan priorizado (solo lectura)
argument-hint: [ruta a exports/capturas de la cuenta o breve descripción del negocio]
---

Delega en el agente `auditor-cuenta-meta` una auditoría de cuenta de Meta Ads con este insumo: $ARGUMENTS

Pasos:
1. Aplica el skill `auditoria-de-cuenta` (checklist de 8 bloques, puntaje ponderado, plan P0/P1/P2).
2. Si faltan datos (AOV, márgenes, estructura, gasto, ventas reales, EMQ), pídelos antes de puntuar; marca N/D lo que siga sin dato.
3. Calcula la economía con `metricas-de-negocio` cuando haya datos suficientes.
4. Mantén las etiquetas [oficial], [analista], [consenso], [un experto], [no verificado] en cada hallazgo.
5. Entrega el informe en el chat y, si el usuario lo pide, guárdalo en la ruta que indique.

Restricciones: solo lectura; no modificar la cuenta ni proponer cambios de gasto sin aprobación humana explícita; no inventar cifras; sin técnicas para evadir políticas de Meta.
