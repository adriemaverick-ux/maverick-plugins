---
name: claude-md-proyecto
description: Crea o mejora el CLAUDE.md de un proyecto (stack, comandos, reglas, criterios de éxito verificables). Úsalo al iniciar un proyecto o cuando Claude repite errores. Triggers - CLAUDE.md, project rules, reglas del proyecto, setup, init, criterios de éxito.
---

# CLAUDE.md de proyecto

## Objetivo
Dejar por escrito lo que Claude debe saber en CADA sesión: qué es el proyecto, cómo se corre, qué reglas no se negocian y cómo se comprueba que una tarea está bien hecha. Es un documento vivo y corto: se precarga siempre, así que cada línea cuesta tokens.

## Pasos
1. Explora el repo (estructura, package.json/pyproject, scripts) antes de escribir nada. Si ya existe un CLAUDE.md, léelo y propón cambios en vez de sobrescribirlo.
2. Redacta estas secciones, en este orden: Propósito (2-3 líneas), Stack, Directorios clave, Comandos (instalar, correr, test, lint, build), Reglas de estilo, Decisiones ya tomadas (para no re-discutirlas), Criterios de éxito.
3. En "Criterios de éxito" escribe una checklist verificable: corre sin errores, tests pasan, lint sin warnings, la funcionalidad pedida funciona, resumen de cambios. Añade la instrucción de revisar el propio trabajo con actitud de desarrollador senior escéptico.
4. Pide a Claude que te entreviste para rellenar lo que no pudo deducir (público, restricciones, qué NO tocar). No inventes datos del negocio.
5. Mantén el archivo por debajo de unas 200 líneas. Lo largo va a archivos referenciados (docs/, memory/) y se enlaza desde aquí.
6. Crea un changelog corto (qué cambió y por qué) y referencia su ruta en CLAUDE.md.
7. Cada vez que Claude cometa un error repetido, añade una regla concreta (una línea, en positivo) en vez de re-explicarlo en el chat.
8. Secretos: documenta SOLO los nombres de variables de entorno (.env, ignorado por git), nunca sus valores.

## Prompts de ejemplo
- "Explora este repositorio y propón un CLAUDE.md con propósito, stack, comandos, reglas y criterios de éxito verificables. No lo escribas aún: primero hazme las preguntas que necesites."
- "Amplía el CLAUDE.md con esta decisión: usamos X y no Y porque Z. Añade una regla para que no vuelvas a proponer Y."
- "Revisa el CLAUDE.md actual: dime qué líneas están obsoletas, cuáles son redundantes y qué falta. Propón la versión recortada."

## Errores comunes
- Volcar documentación entera: infla el contexto en todas las sesiones.
- Reglas vagas ("escribe buen código"). Mejor: "funciones de máximo 40 líneas; tests con vitest".
- No definir cómo verificar: Claude declara terminado sin probar.
- Guardar claves o URLs privadas en el archivo.
- Dejar que se pudra: si Claude falla, la causa suele ser una regla ausente o contradictoria.

## Checklist de cierre
- Archivo existe, menos de ~200 líneas y sin secretos.
- Comandos de test/lint/build probados una vez.
- Criterios de éxito comprobables por Claude sin ti.
- Changelog referenciado.

## Vigencia
- Nombre del archivo y carga automática por carpeta son comportamiento de Claude Code actual; verifica con la documentación vigente si cambia la jerarquía (usuario/proyecto/subcarpeta).
- La longitud recomendada (~200 líneas) es heurística, no límite técnico.
