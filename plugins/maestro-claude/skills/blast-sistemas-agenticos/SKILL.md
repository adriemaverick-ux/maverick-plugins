---
name: blast-sistemas-agenticos
description: Usar al construir una app, dashboard o automatización que une varios servicios con Claude Code, en vez de armar workflows nodo a nodo. Gatillos - "BLAST", "blueprint", "sistema agéntico", "automatización con IA", "SOP antes del código", "build system".
---

# Método BLAST (Blueprint, Links, Architect, Stylize, Trigger)

## Objetivo
Construir sistemas fiables donde el modelo razona y orquesta, pero la lógica de negocio vive en scripts deterministas y SOPs en markdown. Evita improvisar y reduce el "pegar errores a ciegas".

## Pasos
1. **Protocolo cero.** En carpeta nueva y modo plan, crea `CLAUDE.md` (constitución: esquemas de datos, reglas de comportamiento), `task_plan.md`, `findings.md` y `progress.md`.
2. **Blueprint.** Responde cinco preguntas: Norte (resultado deseado en lenguaje llano), integraciones, fuente de verdad (dónde viven los datos), payload de entrega (qué recibe el usuario y dónde) y reglas de comportamiento. No avances sin aprobar el blueprint.
3. **Links.** Para cada servicio pregunta primero "¿tiene MCP o API?". Configura con `claude mcp add` o `.mcp.json`, claves en variables de entorno, tokens con caducidad corta y permisos mínimos. Haz un "handshake" de solo lectura por cada conexión antes de construir. Mantén pocas herramientas MCP activas (cerca de 50 como tope práctico).
4. **Architect en 3 capas.** (a) SOPs en markdown: objetivo, entradas, herramientas, lógica, casos borde; si cambia la lógica, se actualiza el SOP antes que el código. (b) Capa de navegación que enruta entre SOPs y tools sin hacer el trabajo pesado. (c) Tools: scripts atómicos y testeables, configuración en `.env`, intermedios en `.tmp/`.
5. **Probar con datos reales o de prueba** una unidad pequeña; ante un error, copia el log completo al agente.
6. **Stylize.** Solo cuando funcione: diseño, formato de salida, feedback visual; registra las reglas en el SOP.
7. **Trigger.** Programa la ejecución (cron, Modal, Railway o tareas programadas) con idempotencia (sin duplicados), destino claro y una tabla de salud de ejecuciones.
8. Cierra el proyecto actualizando `CLAUDE.md` y `progress.md`; abre ventana nueva por tarea grande (context rot).

## Prompts de ejemplo
- "Modo plan. Inicializa el proyecto con CLAUDE.md, task_plan.md, findings.md y progress.md y hazme las 5 preguntas de Blueprint una por una."
- "Para cada integración de la tabla dime si hay MCP; si no, propón la API mínima. Antes de construir haz una lectura de prueba en cada una y repórtala."
- "Escribe el SOP de esta automatización (objetivo, entradas, lógica, casos borde) y no toques código hasta que lo apruebe."

## Errores comunes
- Dejar que el modelo decida la lógica de negocio en cada ejecución: es probabilístico; codifícala.
- Saltarse los handshakes y descubrir en la mitad que una clave estaba mal.
- Guardar claves en el repo o en el chat; rota cualquier clave que hayas pegado.
- Seguir usando n8n/Make no es un error: sirve para conectores simples, flujos muy deterministas y depuración visual.

## Vigencia
Menús de MCP y proveedores de scheduling (Modal, Railway) cambian. Las ideas de ahorro de costes o tiempo del creador: no verificado. El patrón SOP, scripts, handshake y probar por partes es estable.

## Checklist de salida
- [ ] Blueprint aprobado (Norte, integraciones, fuente de verdad, entrega, reglas).
- [ ] Handshake de lectura exitoso en cada integración.
- [ ] SOP actualizado antes de cada cambio de lógica.
- [ ] Scripts con `.env`, sin valores sensibles versionados.
- [ ] Ejecución programada idempotente y con registro de salud.
- [ ] `progress.md` y `CLAUDE.md` al día al cerrar.
