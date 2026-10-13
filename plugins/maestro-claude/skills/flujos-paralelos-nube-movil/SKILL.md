---
name: flujos-paralelos-nube-movil
description: Organiza trabajo en paralelo con varias sesiones y subagentes, y en la nube o desde el móvil con tareas programadas, rutinas y canales. Úsalo para tareas recurrentes, nocturnas o cuando quieras trabajar sin el portátil. Triggers - paralelo, subagentes, routines, rutinas, scheduled tasks, cron, Telegram, móvil, Claude Code web.
---

# Flujos paralelos, nube y móvil

## Objetivo
Multiplicar el rendimiento sin perder control: varias sesiones independientes, subagentes especializados, tareas en la nube y acceso desde el móvil, cada uno con límites claros.

## Pasos
1. Paralelo local: abre varias pestañas de terminal o paneles, cada una con su sesión en la misma carpeta o en ramas/worktrees distintos para no pisar archivos. Renómbralas por tarea. Terminal es más ligero que un IDE.
2. Subagentes: crea con /agents uno por función (investigador, revisor, redactor) con herramientas mínimas y modelo adecuado. Cada uno tiene su propio contexto. Pide "usa el agente X para...".
3. Para limpiar contexto abre sesión nueva; si necesitas preguntar algo sin interrumpir una tarea larga, usa el comando de pregunta lateral que ofrezca tu versión (por ejemplo /btw).
4. Nube: usa la versión web de Claude Code con tu repositorio de GitHub para tareas que no requieren tu máquina. Las rutinas/tareas programadas corren sin portátil encendido; crea una con nombre, repo, disparador (horario, API o evento de GitHub) y prompt explícito.
5. Redacta el prompt de la rutina como instrucciones, no como conversación: "No respondas; ejecuta A, B, C y guarda el resultado en X". Conecta solo los conectores necesarios.
6. Cada ejecución en la nube parte sin estado, sin archivos locales ni cookies del navegador y sin aprobaciones a mitad: guarda el estado fuera (Notion, base de datos, commit o PR). Prueba con "run now" y revisa los runs.
7. No determinista: úsalo para juicio difuso (resúmenes, triaje); para "haz X siempre igual" usa un automatizador clásico o un script.
8. Móvil: opciones oficiales son la app/web de Claude Code y el control remoto de sesiones. Si usas un canal de mensajería (Telegram, Discord), restringe a tu usuario con lista blanca, evita dos sesiones del mismo bot, deja el equipo sin suspender (o acepta que no responde) y guarda un archivo de memoria aparte porque no hay historial entre sesiones.
9. Mantén los permisos normales de ejecución y aprobaciones: no desactives las confirmaciones para que "no se atasque"; define en su lugar permisos permitidos concretos.

## Prompts de ejemplo
- "Crea una rutina diaria a las 8:00: resume las novedades de [fuente], crea una página en Notion con máximo 8 puntos. No me respondas en chat; ejecuta los pasos y registra errores."
- "Define 3 subagentes: investigador (solo lectura), redactor y revisor escéptico. Herramientas mínimas para cada uno."
- "Divide esta migración en 3 tareas independientes y dime cuáles pueden ir en paralelo sin tocar los mismos archivos."

## Errores comunes
- Dos sesiones sobre los mismos archivos sin ramas separadas.
- Rutinas con prompts conversacionales que se quedan esperando respuesta.
- Dar a la rutina conectores de más.
- Suponer persistencia de estado entre ejecuciones.
- Desactivar aprobaciones para ganar comodidad.

## Checklist de cierre
- Tareas paralelas sin archivos compartidos.
- Prompts de rutinas en modo instrucción.
- Estado persistido fuera de la ejecución.
- Permisos y aprobaciones intactos.

## Vigencia
- Rutinas, canales y control remoto eran funciones en vista previa; nombres, comandos, límites diarios y planes cambian. Los límites citados por el creador: no verificado.
- Revisa la documentación antes de copiar comandos de instalación de canales.
