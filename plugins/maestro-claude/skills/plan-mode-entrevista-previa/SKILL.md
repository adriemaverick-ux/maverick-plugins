---
name: plan-mode-entrevista-previa
description: Obliga a definir el problema antes de construir - plan mode más entrevista previa de Claude. Úsalo antes de cualquier app, web, automatización o tarea estratégica ambigua. Triggers - plan mode, modo plan, entrevístame, interview me, antes de codificar, ultrathink.
---

# Plan mode + entrevista previa

## Objetivo
Evitar que Claude ejecute rápido algo mal planteado. El primer prompt es el más importante: se declara la intención, Claude pregunta, se acuerda un plan y solo entonces se construye.

## Pasos
1. Entra en plan mode (Shift+Tab alterna entre modo normal con aceptación de ediciones y plan mode; comprueba el indicador en pantalla). En plan mode Claude propone sin modificar archivos.
2. Escribe el primer prompt con esta forma: "Lo que intento lograr es X (resultado y para quién). Restricciones: Y. Entrevístame, haz todas las preguntas necesarias y desafía mis supuestos antes de proponer nada."
3. Responde las preguntas (stack, librería de UI, público, qué queda fuera). Si no sabes, pide opciones con pros y contras.
4. Para problemas difíciles pide razonamiento profundo de forma explícita (por ejemplo la palabra "ultrathink" o subir el esfuerzo; ver skill enrutar-modelo-esfuerzo).
5. Exige que el plan incluya: pasos ordenados, archivos a tocar, riesgos, y cómo se verificará cada paso.
6. Revisa el plan, corrígelo y aprueba. Solo entonces pasa a ejecución.
7. Divide en hitos pequeños; tras cada uno verifica contra los criterios del CLAUDE.md.
8. Si el resultado difiere de lo esperado, vuelve a plan mode en vez de parchear a ciegas.
9. Si el objetivo es solo una idea suelta, usa meta-prompting: pide a Claude que te entreviste y devuelva un prompt mejorado; úsalo en una sesión nueva.

## Prompts de ejemplo
- "Quiero construir un panel de métricas para mi negocio. Estamos en plan mode: no escribas código. Entrevístame de una pregunta a la vez hasta tener claro público, datos, alcance y criterios de éxito."
- "Antes de ejecutar, dame el plan con riesgos y alternativas. Señala qué parte es irreversible."
- "Actúa como revisor escéptico de este plan: ¿qué se rompe primero y qué supuesto no he validado?"

## Errores comunes
- Saltarse la entrevista porque "es sencillo": el coste se paga en retrabajo.
- Responder "lo que tú veas": delegas justo las decisiones importantes.
- Plan sin verificación: no sabes cuándo has terminado.
- Sobrecargar el primer prompt con todo el producto; mejor hitos.
- Usar la orquestación paralela sobre un problema aún mal definido.

## Checklist de cierre
- Se hicieron preguntas antes del plan.
- El plan lista archivos, riesgos y verificación.
- Aprobaste el plan explícitamente.
- Hitos pequeños con comprobación al final de cada uno.

## Vigencia
- El atajo Shift+Tab y la palabra "ultrathink" pueden cambiar entre versiones; confirma con /help o la documentación.
- La idea de gastar la mayor parte del esfuerzo en definir el problema es una práctica del creador, no una cifra comprobada.
