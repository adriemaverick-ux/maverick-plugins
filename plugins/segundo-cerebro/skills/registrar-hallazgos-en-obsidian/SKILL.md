---
name: registrar-hallazgos-en-obsidian
description: Guarda en la bóveda de Obsidian los hallazgos, decisiones, cambios y pendientes importantes de la conversación actual. Usar al terminar cualquier trabajo con resultados, cuando el hook de cierre lo pida, o cuando Adrie diga "guarda esto", "registra", "mete esto en Obsidian". Gatillos - "registrar", "guardar en Obsidian", "wrap-up", "bitácora", "save findings".
---

# Registrar hallazgos en Obsidian

## Objetivo
Que nada importante se quede solo en el chat. Al terminar un trabajo, la bóveda queda con lo que se descubrió, se decidió, se hizo y falta hacer.

## Bóveda
Ruta por defecto: `~/Downloads/Maverick MP` (variable `MAVERICK_VAULT` si existe). Casa Soyer tiene su propia bóveda: `~/Downloads/Casa Soyer`. Usa la que corresponda al tema.

## Qué cuenta como "importante" (guardar)
- Decisiones de Adrie y su porqué.
- Hallazgos nuevos con su fuente y su nivel de confianza ([oficial], [analista], [no verificado]).
- Cambios hechos (archivos, plugins, configuraciones) y dónde quedaron.
- Pendientes, bloqueos y próximos pasos.
- Riesgos detectados y cómo se mitigan.
- Resultados de pruebas, números reales y lecciones.

## Qué NO guardar
- Claves, tokens, contraseñas ni listas de teléfonos o datos personales.
- Charla suelta, relleno, o lo que ya está igual en otra nota.
- Datos de clientes sin permiso para publicarlos (la bóveda es privada, pero sigue la regla).

## Pasos
1. **Leer primero** `00 - Inicio.md` y las últimas entradas de `Bitácora IA.md` (otro asistente, Codex, trabaja en la misma bóveda).
2. **Decidir dónde va**: usa la skill `estructura-de-boveda`. Si ya existe una nota del tema, **agrégale una sección fechada**; no crees duplicados.
3. **Escribir la nota** (nueva o sección) con frontmatter `creado_por: Claude` y `actualizado: AAAA-MM-DD`. Estructura: Qué se hizo · Hallazgos · Decisiones · Pendientes · Fuentes.
4. **No borrar ni reescribir** el trabajo de Codex o de Adrie. Si algo parece incorrecto, agrega una sección de propuesta.
5. **Enlazar** la nota desde la nota índice del área con `[[wikilink]]`.
6. **Anotar en `Bitácora IA.md`**: fecha, asistente, qué se hizo, en qué notas.
7. **Pasar el filtro de secretos**: buscar tokens o claves en lo escrito (ver `higiene-de-claves`). Si hay, quitarlos.
8. **Confirmar a Adrie** en una línea: qué notas se crearon o editaron.

## Plantilla de nota
```
---
creado_por: Claude
actualizado: AAAA-MM-DD
estado: activo
---
# Título claro
## Qué se hizo
## Hallazgos (con etiqueta de confianza)
## Decisiones
## Pendientes y próximos pasos
## Fuentes
```

## Errores comunes
- Registrar solo el resultado final y perder el porqué de las decisiones.
- Duplicar una nota en vez de ampliar la existente.
- Pegar un token "de ejemplo" real en la nota.
- Dar la tarea por terminada sin registrar.

## Vigencia
2026-10-11. Basado en AGENTS.md y `registro-obsidian` de la bóveda Maverick MP.
