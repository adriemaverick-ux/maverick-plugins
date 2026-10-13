---
name: crm-pipeline-etapas-y-datos-minimos
description: Úsalo para definir o auditar las etapas del pipeline comercial de Maverick y los datos mínimos por oportunidad, o decidir en qué etapa va un contacto. Gatillos: "etapas del pipeline", "mover a Propuesta enviada", "datos mínimos", "pipeline stages", "CRM fields".
---

# Pipeline: etapas y datos mínimos

## Objetivo
Que cada oportunidad tenga una etapa honesta, datos suficientes y un siguiente paso con fecha. La definición de etapas no demuestra que estén configuradas en GHL: verificar el pipeline real antes de crear o mover algo.

## Pasos
1. Usar las cinco etapas acordadas, en orden: **Respondió** → **Propuesta enviada** → **Respondió a propuesta** → **Aceptó propuesta** → **Nuevo cliente**.
2. Respondió: una persona respondió y se identificó el asunto; guardar respuesta textual breve y próxima acción. Respuestas automáticas quedan fuera de esta etapa.
3. Propuesta enviada: se entregó una propuesta concreta con alcance, precio, costos de herramientas y siguiente paso; guardar fecha y versión. Un PDF existente no es un envío verificado.
4. Respondió a propuesta: el decisor comentó, preguntó u objetó; registrar qué falta resolver.
5. Aceptó propuesta: aprobación explícita de alcance y condiciones. "Me interesa" no es aceptación.
6. Nuevo cliente: acuerdo formalizado e inicio o primer pago según lo pactado.
7. Cierre: si no encaja o pide no contacto, cerrar con motivo; no dejarlo en una etapa activa.
8. Los estados previos (Pendiente de envío, Enviado) viven en el registro de outreach, no en el pipeline.
9. Higiene: una oportunidad abierta por contacto y servicio; revisar las estancadas (referencia del informe: más de 7 días sin actividad).
10. Opcional, tras cerrar clientes: pipeline B de servicio recurrente (onboarding, activo, próxima visita, visita realizada, renovación, en riesgo, cancelado). Es recomendación del informe, no decisión tomada.

## Plantillas
Datos mínimos por oportunidad:
```
Empresa / Sector / Responsable (cargo)
Canal / Origen
Problema concreto / Proceso actual / Capacidad operativa
Próximo paso y fecha
Propuesta: alcance, decisión pendiente, versión enviada y fecha
Cliente: resultado del piloto, permiso para usar el caso públicamente
Consentimiento: canal, fecha, propósito; opt-out
Motivo de cierre (si aplica)
```
Campos personalizados sugeridos: tipo de cliente, fuente del lead, monto y fecha de cotización, fecha de próxima visita, frecuencia, fecha de renovación.

## Errores comunes
- Mover a Respondió por un bot o un menú de bienvenida.
- Marcar Propuesta enviada sin comprobar entrega.
- Pegar conversaciones completas o datos sensibles innecesarios.
- Mantener oportunidades muertas para "inflar" el pipeline.
- Dar por configurado en GHL lo que solo está en una nota.

## Nivel de evidencia
- Cinco etapas y reglas de cierre: [decisión de Adrie, 2026-10-10].
- Pipeline A de ocho etapas y pipeline B: [recomendación del informe 02, no acordada].
- Estado de GHL real y entrega de propuestas existentes: [no verificado]; comprobar.

## Fuente
Nota "Pipeline comercial - Servicios recurrentes", decisiones consolidadas (2026-10-10) e informe 02, sección 8.

## Vigencia
2026-10-11.
