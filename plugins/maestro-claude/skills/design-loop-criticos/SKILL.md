---
name: design-loop-criticos
description: Bucle de diseño con críticos independientes (subagentes con contexto fresco) que iteran hasta cumplir una barra. Usar para "design loop", "gauntlet loop", "críticos", "iterar hasta que quede bien", "calidad en un disparo", piezas grandes o plantillas reutilizables.
---

# Design loop con críticos

## Objetivo
Evitar que Claude sea juez y parte de su propio trabajo. Un constructor genera; críticos separados, con roles fijos y contexto limpio, evalúan contra una barra explícita; se repite hasta que todos aprueban.

## Pasos
1. Prepara insumos: brief de 5 líneas, referencia "gold standard" (captura o URL), design system si existe, formato final (carrusel, hero, email, animación, póster).
2. Convierte esta técnica en una skill propia si aún no la tienes (pega el procedimiento y pide "guárdalo como skill design-loop"); invócala con `/design-loop`.
3. Pre-flight: que Claude te entreviste y escriba la barra de calidad como checklist verificable (medidas, jerarquía, contraste, copy, fidelidad al brief). El gusto se vuelve checklist.
4. Constructor genera la versión 1 con las referencias adjuntas.
5. Lanza 3 críticos en paralelo, cada uno con un solo rol: (a) brief: ¿hizo lo pedido?; (b) sistema/marca: ¿respeta tokens, fuentes, iconos?; (c) craft: mide frames renderizados, espaciado, interlineado, desbordes.
6. Cada crítico devuelve lista de fallos con severidad y evidencia (captura/medida). El constructor corrige solo eso, sin reabrir lo aprobado.
7. Repite hasta que los 3 aprueben o se agote un máximo de rondas (fíjalo: 5-8). Detente ahí.
8. Pide un segundo archivo con el registro de qué corrigió cada crítico; sirve para afinar tu checklist.
9. Trabaja una pieza por proyecto; deja que termine sola.

## Prompts de ejemplo
- "/design-loop Usa esta captura como estándar de oro y construye una versión para [mi evento]. Define primero la barra de calidad como checklist numerado y muéstramela antes de construir."
- "Crea tres críticos con contexto limpio: brief, sistema de marca y craft visual. Cada uno revisa solo lo suyo, con medidas. Máximo 6 rondas y entrega además un log de cambios por crítico."
- "Delega los críticos a un modelo más pequeño y deja el modelo principal solo para construir y corregir."

## Errores comunes
- Pedir "mejóralo" varias veces seguidas: da correcciones distintas cada vez.
- Críticos sin rol fijo o que comparten contexto con el constructor.
- Barra vaga ("que se vea premium") en lugar de criterios medibles.
- Usarlo para todo: consume muchos tokens; resérvalo para piezas grandes, plantillas o entregables de cliente (cifras de consumo reportadas: no verificado).
- Aprobar sin ver el render real en el tamaño final.

## Vigencia
Depende de que tengas la skill creada y de que tu entorno permita subagentes. El consumo de tokens y los modelos recomendados para críticos cambian por plan y fecha; mide en tu cuenta.

## Criterios de salida
- La barra de calidad está escrita y los 3 críticos aprobaron con evidencia.
- Se respetó el máximo de rondas y se guardó el log de correcciones.
- El resultado final se vio renderizado en su tamaño real.
- Queda anotado el costo aproximado para decidir si vale la pena repetirlo.
