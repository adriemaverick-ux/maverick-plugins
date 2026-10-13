---
name: calificacion-de-leads-whatsapp
description: Úsala para definir cómo calificar chats que llegan de anuncios de WhatsApp, qué preguntas hacer y qué marcar como QualifiedLead. Gatillos - "calificar leads", "lead calificado", "preguntas de calificación", "qualified lead", "costo por conversación calificada".
---

# Calificación de leads de WhatsApp

## Objetivo
Separar curiosos de compradores sin espantar a nadie, y devolver a Meta (CAPI-BM) la señal de calidad. Mide costo por conversación calificada, no solo por conversación.

## Pasos
1. Definir qué es "calificado" por escrito antes de lanzar. Mínimo 3 datos: (1) pieza o uso concreto, (2) plazo, (3) distrito o ciudad de entrega.
2. Preguntar el presupuesto después de que la persona vio precio o valor, para no perder gente [benchmark, guías de proveedores].
3. Una pregunta por mensaje; usar botones cuando sea posible. Máximo 3-4 preguntas que realmente decidan si se agenda.
4. Marcar etapas en el CRM: conversación iniciada, respondió 2 turnos, calificado, cita/videollamada, cotización, venta.
5. Al pasar a "calificado", enviar `QualifiedLead` por CAPI-BM con el `ctwa_clid` guardado; al vender, `Purchase` [oficial].
6. Registrar motivo de pérdida en CRM (precio, confianza, plazo, stock) para enriquecer audiencias y exclusiones.
7. Revisar semanalmente: costo por conversación calificada por conjunto y por creativo.

## Plantillas / prompts listos
- Primera pregunta: "Hola, soy [nombre] de [marca]. Te ayudo con [pieza]. ¿Para qué distrito sería la entrega y en qué fecha la necesitas?"
- Segunda: "¿La pieza es para sala, comedor u otro ambiente? Te envío fotos reales y medidas."
- Tercera (con precio ya visto): "¿Te sirve pagarla con tarjeta, transferencia o en cuotas?"
- Prompt para Claude: "Clasifica estas conversaciones exportadas (sin datos personales) en no calificado, calificado o cita agendada según criterios: pieza concreta, plazo, distrito. Dame la tabla y la razón de cada clasificación; no inventes datos que falten."
- Fórmula: costo por conversación calificada = gasto / conversaciones calificadas.

## Errores comunes
1. Preguntar presupuesto antes de mostrar precio o valor.
2. Hacer muchas preguntas seguidas.
3. No guardar `ctwa_clid`: sin eso no hay QualifiedLead útil.
4. Marcar calificado sin criterio escrito, y así cambiar de semana en semana.
5. Pegar teléfonos y datos de clientes en un LLM sin base legal.

## Nivel de evidencia
- [oficial] Eventos QualifiedLead y Purchase en CAPI-BM; Meta recomienda 6 preguntas o menos en lead ads.
- [benchmark] Recomendaciones de 3-4 preguntas, botones y una pregunta por mensaje (360dialog, Clickatell).
- [no verificado] No existe dato público de costo por conversación calificada en Perú: derivarlo de la propia cuenta.

## Checklist de calidad semanal
- [ ] Criterio de calificado sin cambios durante la semana.
- [ ] QualifiedLead enviado el mismo día, sin duplicados.
- [ ] Motivos de pérdida registrados en CRM.
- [ ] Costo por conversación calificada por conjunto y por creativo.
- [ ] Conversaciones exportadas sin datos personales si se analizan con IA.

## Vigencia
2026-10-11.
