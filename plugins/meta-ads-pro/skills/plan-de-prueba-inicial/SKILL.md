---
name: plan-de-prueba-inicial
description: Diseña un plan de prueba inicial de Meta Ads con presupuesto pequeño por fases. Usar cuando el usuario empiece desde cero o con poco presupuesto: "primera campaña", "plan de prueba", "test budget", "cuánto gastar para validar", "lanzar con poco dinero".
---

# Plan de prueba inicial (presupuesto pequeño)

## Objetivo
Validar con poco gasto qué conceptos y ofertas funcionan, antes de escalar. El plan se expresa en múltiplos del CPA objetivo; el usuario fija los montos y aprueba cada fase.

## Pasos
1. **Fase 0, Preparación (sin gasto)**: calcular nCAC máximo y MER de equilibrio con `metricas-de-negocio`; verificar Pixel + CAPI (EMQ 7/10+); landing coherente con la promesa; evento de optimización alineado (compra, o mensaje/lead de calidad si el volumen es bajo). [un experto / consenso débil]
2. **Fase 1, Exploración de conceptos**: 3 conceptos realmente distintos (persona x ángulo x etapa) de punto de partida [un experto: Precis]; con USD 100/día la referencia es ~4 tests/semana y 10-15 anuncios por conjunto. [un experto, secundaria; vendor]
   - Una campaña de test, conjunto amplio con Advantage+ audience, ventana 7 días clic.
   - Presupuesto mínimo por creativo: 2-3x CPA objetivo. [consenso débil]
3. **Fase 2, Lectura (mínimo 3 días, sin tocar 48-72 h)**: usar hook/hold como diagnóstico; decidir con `reglas-de-decision`. No juzgar con 2-3 conversiones. [consenso]
4. **Fase 3, Explotar**: sobre el concepto ganador, iterar hooks (primeros 3-7 s), formato y prueba social; cadencia mínima de 2-3 creativos nuevos distintos por semana. [un experto: CTC / Manchi]
5. **Fase 4, Consolidar y escalar con cautela**: mover lo validado a una campaña de escala; subir presupuesto 10-20% cada ~3 días solo si el nCAC marginal sigue bajo el techo. [consenso débil]
6. **Punto de decisión por fase**: al cerrar cada una, presentar resultados y pedir al usuario aprobación explícita (continuar, ajustar, detener). Si hay dudas de atribución, plantear holdout. [juicio de síntesis]
7. **Criterio de parada**: si tras la Fase 2 ningún concepto se acerca al nCAC máximo, revisar oferta, landing y señales antes de gastar más. [juicio de síntesis]

## Plantillas / prompts
```
Fase | Duración | Presupuesto (múltiplos de CPA obj.) | Qué se prueba | Criterio de paso | Aprobación humana
```
Prompt: "Con CPA objetivo X y presupuesto total Y, arma las fases, cuántos creativos caben (2-3x CPA cada uno) y define el criterio de paso. No lances nada: entrega el plan para aprobar."

## Errores comunes
Lanzar muchos conjuntos con poco presupuesto; probar hook, formato, oferta y audiencia a la vez; apagar en 24 h; optimizar a un evento demasiado raro y quedar en "aprendizaje limitado"; no tener CAPI. [consenso]

## Nivel de evidencia
Estructura de fases: síntesis de este plugin sobre [consenso] y [un experto]. Tabla USD 100/día: [un experto] vía vendor secundario. Presupuesto 2-3x CPA: [consenso débil]. Montos concretos: no provistos por las fuentes; los define el usuario.

## Vigencia
2026-10-11. Verificar en la interfaz el nombre actual de las metas de rendimiento (mensajes, leads) antes de lanzar. [no verificado]

## Notas de uso
- Antes de la Fase 1, pedir al usuario que fije el presupuesto total y lo apruebe por escrito en el chat.
- Documentar al cierre de cada fase: gasto, conversiones, CPA, conceptos ganadores y aprendizajes.
- Si el negocio opera por WhatsApp, pasar de conversaciones a eventos de calidad por CAPI cuando haya volumen. [analista]
- Nunca ampliar presupuesto de una fase sin confirmación humana.
- Reutilizar `reglas-de-decision` para cada lectura de resultados.
- Entregar el plan en una tabla simple por fase para facilitar la aprobación.
- Mantener las etiquetas de confianza visibles en el plan.
- Revisar la vigencia antes de reutilizar el plan en otra fecha.
- No inventar montos: los fija el usuario.
