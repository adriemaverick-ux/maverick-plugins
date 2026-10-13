---
name: registro-en-boveda
description: Usar al empezar y al terminar cualquier tarea de Maverick para registrarla en la bóveda de Obsidian "Maverick MP" sin pisar el trabajo de Codex. Triggers - "registrar en la bóveda", "bitácora", "guardar en Obsidian", "log this in the vault", "antes de terminar".
---

# Registro en la bóveda

## Objetivo
Que nada quede solo en el chat. La bóveda `/Users/adriebustos/Downloads/Maverick MP` es compartida con otro asistente (Codex); el registro evita pisarse y permite continuar.

## Pasos
1. Al empezar, leer `00 - Inicio.md` y las últimas entradas de `Bitácora IA.md`.
2. Si una nota fue tocada recientemente por Codex, leerla completa antes de editarla. Si la tarea continúa algo previo, abrir esa nota en vez de crear otra.
3. No borrar ni reescribir lo del otro asistente sin pedido del dueño; si algo parece incorrecto, señalarlo o añadir una sección con la propuesta. Si hay recomendaciones distintas, presentar ambas.
4. Guardar el resultado en la carpeta correcta (`01 - Negocio`, `02 - Mercado`, `03 - Go-to-market`), en español, fechas AAAA-MM-DD, enlaces `[[wikilinks]]`. Datos tabulares como CSV en `datos/`.
5. Frontmatter en toda nota nueva o editada: `creado_por` (Claude | Codex | Dueño) y `actualizado`. En notas de Codex que edites, no cambies `creado_por`; deja constancia en la bitácora.
6. Enlazar la nota desde `00 - Inicio.md` o la nota madre para que no quede huérfana.
7. Añadir arriba en `Bitácora IA.md`: `### AAAA-MM-DD — Claude (tema)`, qué se hizo, notas tocadas y `Pendiente:` si quedó algo.
8. Registrar antes de dar por terminado. Informar al dueño las notas creadas o editadas.
9. No tocar `.obsidian/`, no guardar contraseñas ni tokens, no registrar datos de clientes sin permiso.

## Plantillas / ejemplos
```yaml
---
creado_por: Claude
actualizado: 2026-10-11
---
```
```
### 2026-10-11 — Claude (revisión de guion Reels)
- Se revisó el guion de la semana 1 y se reescribieron 2 frases.
- Notas: [[03 - Go-to-market/Plan de contenido - Servicios recurrentes]] (sección añadida, sin borrar lo de Codex).
- Pendiente: confirmar con el dueño la frase de cierre.
```

## Errores comunes
- Dar la tarea por terminada solo en el chat.
- Sobrescribir una nota de Codex en vez de añadir sección.
- Olvidar actualizar `actualizado`.
- Dejar la nota sin enlace desde Inicio.
- Escribir en la bitácora al final del archivo en vez de arriba.

## Fuente
`AGENTS.md`, `.claude/skills/registro-obsidian/SKILL.md`, `00 - Inicio.md`.

## Vigencia
2026-10-11.
