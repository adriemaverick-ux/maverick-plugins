---
description: Registra la respuesta de un negocio (clasifica humana, bot u opt-out), actualiza el estado en el registro y sugiere la etapa del pipeline.
argument-hint: "<negocio> | <texto de la respuesta o resumen>"
---

Usa el agente `prospector-maverick` con: $ARGUMENTS

Pasos:
1. Ubica el negocio en el registro de outreach. Si no existe o es ambiguo, pregúntame.
2. Clasifica con `prosp-separar-respuestas-humanas-de-bots`: humana relevante, no relevante, respuesta automática, opt-out. Si hay duda, déjala "por confirmar".
3. Actualiza el estado y anota la respuesta textual breve, el problema mencionado y el siguiente paso con fecha. Sin datos personales ni conversaciones completas.
4. Sugiere etapa según `crm-pipeline-etapas-y-datos-minimos`: solo una respuesta humana relevante pasa a "Respondió"; una automática no crea oportunidad; un opt-out se marca No contactar.
5. Si corresponde, redacta (sin enviar) la siguiente pregunta, una sola, o la respuesta transparente al bot.

No envíes nada ni modifiques GHL; propón el cambio y espera mi confirmación.
