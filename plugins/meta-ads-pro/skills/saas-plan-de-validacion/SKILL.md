---
name: saas-plan-de-validacion
description: Diseña una prueba pequeña de 60-90 días para validar si Meta sirve a un SaaS antes de invertir en serio, sin montos fijos y con criterios de corte. Usar con "validar SaaS en Meta", "plan de prueba SaaS", "cómo empiezo sin casos", "test before scaling", "primer presupuesto de prueba".
---

# SaaS: plan de validación

## Objetivo
Responder con datos propios, gastando lo mínimo necesario, si Meta puede traer clientes pagadores a un SaaS sin casos validados. No se fijan montos: el presupuesto sale de la fórmula y lo aprueba el dueño.

## Pasos
1. **Economía primero**: ARPA, margen, churn, CAC objetivo y payback máximo con `saas-economia-cac-ltv-payback`. Sin CAC objetivo no se lanza.
2. **Hipótesis y veredicto previo** con `saas-cuando-meta-funciona`: ¿Meta principal, complemento o descarte? Escribir qué resultado la refutaría.
3. **Oferta y destino** con `saas-embudos`: autoservicio → trial/freemium; venta asistida → demo calificada o WhatsApp con bot.
4. **Medición antes del gasto**: pixel + CAPI con event_id, UTMs hasta cierre, estados del CRM de vuelta (`saas-eventos-y-optimizacion`). Sin esto no hay prueba válida.
5. **Presupuesto mínimo calculado, no inventado**: (50 / tasa trial→pago) x costo por trial / 7 por conjunto [un experto: RocketShip]. Referencias externas (B2B EE. UU. USD 3-5k/mes de prueba; < USD 3.000/mes "no sale de aprendizaje") [un experto] sirven de contraste, no de monto. Proponer el monto al dueño con los supuestos y esperar su aprobación.
6. **Estructura simple**: máximo 2-3 conjuntos, segmentación amplia, 8-12 conceptos creativos con 2-3 variantes (`saas-creativos`) [un experto].
7. **Duración**: 60-90 días antes de concluir; evento inicial en trial/lead calificado y migración al pago tras 3 semanas con ≥ 50 eventos/semana [un experto].
8. **Operación de leads**: respuesta en minutos, calificación, registro de cada lead en el CRM.
9. **Criterios de decisión escritos de antemano**: pasar a escala solo si payback < 12 meses y LTV:CAC > 3 [un experto]; pausar si el costo marginal supera el CAC objetivo por 2 semanas. Si no se alcanza el volumen de eventos, bajar un escalón de evento o declarar la prueba no concluyente (no "Meta no funciona").
10. **Techo**: calcular gasto de saturación (`saas-escala-y-techos`) y decidir si hace falta otro canal o mercado.
11. **Aprobaciones humanas**: lanzamiento, presupuesto, cambio de evento y escala requieren confirmación explícita.

## Plantillas / prompts
```
Hipótesis: "Con __ (oferta) a __ (ICP) logro CAC <= __ en 60-90 días."
Refutada si: __ (p. ej. < 50 eventos/sem tras 3 sem; CAC > objetivo)
Medición lista: [pixel] [CAPI] [UTMs] [CRM->Meta]
Presupuesto propuesto: __ (fórmula + supuestos) -> APROBADO POR: __ fecha __
Revisión: semana 3, 6, 9; decisión: escalar | iterar | parar
```

## Errores comunes
- Probar con poco presupuesto y poco tiempo, y concluir "Meta no sirve".
- Optimizar a registro y medir por CPL.
- Lanzar sin CAC objetivo ni CAPI.
- Dar por válidos casos ajenos: no hay casos públicos verificables de SaaS B2B, y el dueño hoy no tiene casos propios validados.

## Nivel de evidencia
Débil. Marco: [un experto] (agencias con interés comercial). Fórmula de presupuesto: [un experto]. Sin benchmark de Perú; el resultado de la prueba propia será el único dato fiable.

## Vigencia
2026-10-11.

## Skills relacionados
- `saas-eventos-y-optimizacion`: medición y regla de ~50 eventos/semana.
- `saas-peru-pagos-y-mercado`: medios de cobro antes de lanzar.
- `saas-creativos`: set inicial de conceptos.
