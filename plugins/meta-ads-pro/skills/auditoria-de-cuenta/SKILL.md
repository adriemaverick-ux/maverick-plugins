---
name: auditoria-de-cuenta
description: Audita una cuenta de Meta Ads con checklist completa, puntaje y plan priorizado. Usar cuando se pida "auditar la cuenta", "audit my Meta Ads account", "revisión de cuenta", "por qué no rinde", "health check" o antes de reestructurar.
---

# Auditoría de cuenta

## Objetivo
Evaluar la cuenta en 8 bloques, puntuar y entregar un plan priorizado. Solo lectura: no se modifica nada sin aprobación humana.

## Pasos
1. **Recolectar** (export o capturas del usuario; si falta, marcar "sin dato"): estructura, gasto 30/90 días, ventas reales, margen, eventos/EMQ, creativos activos, atribución usada.
2. **Puntuar cada ítem** 0 = incumple, 1 = parcial, 2 = cumple, N/D = sin dato (excluir del total). Esquema de puntaje de este plugin (criterio propio, no de Meta).
3. **Checklist** (etiqueta de la fuente del criterio):
   - **A. Economía** (peso x3): nCAC máx y MER de equilibrio calculados [consenso]; decisiones por MER/margen y no solo ROAS [consenso]; LTV/payback conocido [un experto].
   - **B. Señales** (x3): Pixel + CAPI [consenso]; EMQ 7/10+ [un experto]; ~80% de compras reales capturadas o más [un experto]; en CTWA, eventos devueltos con `ctwa_clid` [analista].
   - **C. Estructura** (x2): una campaña por objetivo [analista]; consolidada (si >3-4 campañas sin 20+ conv./semana, consolidar) [un experto]; test separado de escala [consenso]; sin conjuntos con intereses retirados [no verificado].
   - **D. Entrega** (x2): conjuntos fuera de "aprendizaje limitado" o con causa identificada [analista]; evento alineado al negocio; Advantage+ audience/placements activos salvo razón [analista].
   - **E. Creatividad** (x3): conceptos realmente distintos (persona, ángulo, etapa, formato) [consenso]; cadencia de nuevos según gasto [un experto]; fatiga controlada (frecuencia 3-4 en pocas semanas, alarma) [un experto]; revisar columna Creative diversity como guía, no verdad [analista].
   - **F. Medición** (x2): ventana 7d_click/1d_view entendida; sin comparar con reportes pre-2026 [analista]; validación con holdout si hay duda [juicio de síntesis].
   - **G. Landing y oferta** (x2): coherencia promesa-landing [consenso débil].
   - **H. Cumplimiento** (x2): sin avisos de políticas; categoría especial bien declarada; pago y verificación de negocio al día [analista].
4. **Calcular puntaje** = suma(puntos x peso) / suma(2 x peso de ítems con dato) x 100. Bandas orientativas (propias): <50 crítico, 50-75 mejorable, >75 sólido.
5. **Plan priorizado**: P0 (bloquea medición o entrega: señales, economía), P1 (estructura, creatividad), P2 (optimización). Cada acción con esfuerzo, impacto esperado cualitativo y etiqueta de evidencia.
6. **Entregar** informe y pedir confirmación antes de cualquier cambio que afecte gasto.

## Plantillas / prompts
Formato de hallazgo: `ID | bloque | estado 0/1/2/N-D | evidencia observada | recomendación | etiqueta | prioridad`.
Prompt: "Audita con esta checklist usando solo los datos entregados; marca N/D donde falte y lista qué dato pedir."

## Errores comunes
Puntuar sin datos reales; recomendar apagar anuncios por ROAS histórico; tratar benchmarks de vendors como ley; proponer cuentas nuevas para evadir restricciones (no hacerlo).

## Nivel de evidencia
Cada ítem lleva la etiqueta de su fuente. El puntaje y los pesos son criterio del plugin, no una métrica de Meta ni de los expertos. Benchmarks de vendors: [no verificado].

## Vigencia
2026-10-11. Revisar la checklist tras cambios de placements, atribución o términos (30-oct-2026).

## Notas de uso
- Si la cuenta tiene pocos datos, entregar una auditoría parcial indicando qué ítems quedaron N/D.
- El plan priorizado es una propuesta: ninguna acción de gasto se ejecuta sin confirmación humana.
- Reauditar tras aplicar los cambios P0 para medir el avance con el mismo puntaje.
- Guardar el informe solo en la ruta que indique el usuario.
- Separar hallazgos por severidad si el usuario lo pide.
- Incluir siempre la fecha del análisis en el informe.
