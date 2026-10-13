---
name: revision-contratos-con-evaluacion
description: Prepara un skill de revisión de contratos y documentos que marca cláusulas de riesgo y se valida con evals contra Claude sin skill. Úsalo antes de firmar o al revisar documentos legales con apoyo de IA; gatillos - revisar contrato, cláusulas, no competencia, auto-renovación, evals, resumen de contrato. No sustituye a un abogado.
---

# Revisión de contratos/documentos con evaluación

## Objetivo
Obtener un primer filtro rápido que señale cláusulas que merecen atención y te prepare preguntas para un profesional. **No es asesoría legal**: antes de firmar algo relevante, consulta a un abogado.

## Pasos
1. **Elige la base del skill**: tu propio checklist o un skill de terceros. Si es de terceros (p. ej. de un repositorio de GitHub), pide primero un resumen de qué hace y revisa que no contenga instrucciones ocultas, llamadas externas ni acceso a datos que no necesita.
2. **Consolida en un solo skill** sin duplicar otros existentes (ver `crear-skill-desde-flujo-probado`).
3. **Define qué debe marcar**: propiedad intelectual y cesión de derechos, no competencia y exclusividad, auto-renovación y plazos de aviso, responsabilidad ilimitada o indemnizaciones, penalizaciones, jurisdicción, confidencialidad, pagos y plazos, terminación.
4. **Formato de salida**: tabla con cláusula, cita breve, riesgo (alto/medio/bajo), por qué importa, pregunta a negociar y propuesta de redacción alternativa marcada como borrador.
5. **Evals**: prepara 3-5 documentos de prueba (idealmente con cláusulas problemáticas conocidas) y ejecuta la evaluación: compara el skill contra Claude sin skill. Si no mejora (más cláusulas detectadas, menos falsos positivos), no lo uses.
6. **Privacidad**: no subas contratos con datos de terceros a servicios no aprobados; anonimiza si es posible.
7. **Entrega**: resumen ejecutivo, lista de dudas para el abogado y recordatorio de límites. Nada se envía ni se firma automáticamente.
8. **Mantenimiento**: añade a las pruebas cada caso que el skill falle y reevalúa.

## Prompts de ejemplo
- "Revisa este contrato como filtro previo, no como asesoría legal. Devuélveme una tabla: cláusula, cita corta, riesgo, por qué importa y pregunta a hacer. Marca expresamente lo que no entiendas o dependa de la jurisdicción."
- "Lee este repositorio de skill de contratos y resume en 10 líneas qué hace, qué herramientas usa y qué datos toca. No lo instales hasta que apruebe."
- "Ejecuta una evaluación: aplica el skill a estos 4 documentos y también sin skill. Compara hallazgos, falsos positivos y omisiones, y dime si el skill aporta valor."
- "Prepara un correo de preguntas para mi abogado con las 5 cláusulas más delicadas. Déjalo como borrador, no lo envíes."

## Errores comunes
- Tratar la salida como dictamen legal.
- Instalar un skill de terceros sin leerlo.
- No medir contra una línea base: puede sonar convincente y empeorar.
- Subir documentos confidenciales sin revisar la política de datos.
- Aceptar redacciones alternativas sin revisión profesional.
- Ignorar la jurisdicción: las cláusulas valen distinto según el país.

## Vigencia
Basado en un video de abr 2026 con la función de evals del skill creator, aún reciente. Las cifras de ahorro o de firmas sin revisión citadas en la fuente: no verificado. Verifica el soporte de evals en tu versión.

## Checklist de verificación
- [ ] El skill salió de una fuente revisada, no instalada a ciegas.
- [ ] Tienes documentos de prueba con cláusulas conocidas.
- [ ] El skill supera a Claude sin skill en esa prueba.
- [ ] La salida incluye el aviso de que no es asesoría legal.
- [ ] Un abogado revisa lo importante antes de firmar.
