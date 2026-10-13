---
name: subagentes-vs-equipos
description: Usar para decidir cómo paralelizar trabajo en Claude Code (un agente, subagentes o agent teams) y cuándo sumar otros modelos como revisores. Gatillos - "subagentes", "agent teams", "agentes en paralelo", "context rot", "revisión con otro modelo", "multi-agente".
---

# Subagentes vs equipos de agentes

## Objetivo
Elegir la menor estructura que resuelva la tarea: más agentes significan más coste, burocracia y puntos de fallo. Cada agente debe ganarse su sitio.

## Pasos
1. **Prueba de las dos frases.** Si la tarea cabe en un par de frases, usa un solo agente.
2. **Subagentes en paralelo** cuando las tareas son independientes y solo importa el resultado (investigar 3 competidores, redactar metas, auditar secciones distintas). Cada uno tiene su propia ventana de contexto, escribe su salida en un archivo (`research/*.md`) y reporta al principal. No hablan entre sí.
3. **Agent teams (experimental)** solo si los agentes deben coordinarse y compartir una lista de tareas (por ejemplo, front, backend y pagos que dependen unos de otros). Verifica primero en la documentación vigente si la función está disponible y cómo se habilita.
4. **Roles estrechos y sin solaparse:** diseño, construcción, QA, investigación. Una tarea concreta por agente, para que no pinten la misma pared.
5. **Costes.** Modelo potente para quien lidera y razona; modelos más baratos para ejecutores y tareas rutinarias. Limita el número de miembros (en la práctica unos pocos).
6. **Contexto sano.** Una ventana, una tarea; con la ventana por la mitad, pide un resumen y abre sesión nueva. Mantén `CLAUDE.md` y `progress.md` al día para retomar.
7. **Revisión cruzada.** Quien construye no se autorevisa: usa otra sesión limpia, otro modelo o una herramienta de revisión. Regla útil: tras dos fallos seguidos en lo mismo, cambia de enfoque o de revisor.
8. **Integra y verifica.** El agente principal consolida resultados, resuelve conflictos entre archivos y ejecuta la auditoría final (`qa-seguridad-e2e`).

## Prompts de ejemplo
- "Lanza tres subagentes en paralelo: uno investiga competidores locales, otro keywords y otro estructura de páginas. Cada uno guarda su informe en research/ y tú los consolidas."
- "Antes de paralelizar, dime si esta tarea justifica subagentes o un solo agente, y por qué."
- "Revisa críticamente el trabajo anterior con una sesión sin contexto previo: busca fallos de lógica, seguridad y casos borde."

## Errores comunes
- Equipos de agentes para tareas triviales: más lento y casi igual de bueno.
- Dos agentes editando los mismos archivos sin coordinación.
- No limitar herramientas MCP activas por agente (consumen contexto).
- Usar accesos no oficiales a modelos de terceros: riesgo de términos de servicio y de cortes.

## Vigencia
Agent teams, modelos disponibles y límites cambian con cada versión; lo dicho por el creador sobre cuota y precios: no verificado. Revisa la documentación actual de Claude Code.

## Checklist de salida
- [ ] Se justificó por qué no basta un solo agente.
- [ ] Cada agente tiene una tarea estrecha y sin solaparse.
- [ ] Salidas guardadas en archivos y consolidadas por el principal.
- [ ] Modelo caro solo donde se razona; barato en ejecución.
- [ ] Revisión por un agente o modelo distinto al constructor.
- [ ] Sesión nueva abierta con resumen al llegar a media ventana.
