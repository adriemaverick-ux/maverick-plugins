---
name: cowork-cerebro-y-proyectos
description: Configura Cowork como "cerebro del negocio" y organiza tu trabajo en proyectos con memoria, instrucciones y tareas programadas. Úsalo al empezar con Cowork o cuando repites contexto a la IA; gatillos - business brain, proyectos de Cowork, sandbox, global instructions, "siempre tengo que explicarle lo mismo".
---

# Cowork como cerebro del negocio + sistema de proyectos

## Objetivo
Dar a Claude el contexto de tu negocio una sola vez, sin gastar tokens en cada mensaje, y repartir tu trabajo recurrente en pocos proyectos con memoria propia. Carpeta, proyecto y skill NO son lo mismo: la carpeta solo da acceso a archivos; el proyecto suma instrucciones, contexto, memoria y tareas programadas; el skill es un procedimiento portable.

## Pasos
1. **Sandbox**: crea una carpeta dedicada (p. ej. `sandbox`) y apunta Cowork solo ahí. Nunca des acceso a todo el disco. Al organizar archivos, pide que ordene pero que NO borre de forma permanente.
2. **Archivo `business-brain.md`** dentro del sandbox. Contenido: qué es el negocio, a quién sirve, cómo gana dinero, creencias/principios, cliente objetivo, recorrido del cliente (del primer clic al cierre), los 3 mayores dolores que resuelves, canales y aspiraciones.
3. **Global instructions con una sola regla condicional**: "si pregunto por negocio, estrategia o crecimiento, lee primero `business-brain.md` en la carpeta X". Cargarlo siempre en memoria global gasta tokens en cada turno; así solo se lee cuando hace falta.
4. **Preferencias personales cortas** (tono, idioma, nivel de detalle). Pocas líneas.
5. **Decide los proyectos**: en un chat normal pregunta qué buckets crearías según lo que sabe de ti. Reglas: máximo 7-8 proyectos; elige lo que repites cada semana, lo que re-explicas siempre y lo que tiene varias partes móviles (archivos + correos + investigación). Siempre existe un proyecto "business" general.
6. **Crea cada proyecto** con: instrucciones (rol + "cuestiona mis supuestos, razona desde primeros principios, no seas adulador, basa todo en datos"), contexto (archivos, URLs, capturas) y un `core-context.md` que Claude redacte a partir de ese material.
7. **Conecta solo ~5 conectores de uso real** (calendario, correo, notas de reuniones, almacenamiento, notas). Cada conector activo consume contexto.
8. **Trabaja siempre dentro de chats del proyecto** y añade tareas programadas con moderación (ver skill `brief-matutino-y-triage-correo`).

## Prompts de ejemplo
- "Según todo lo que sabes de mí, ¿qué 6-7 proyectos de Cowork me conviene crear? Para cada uno dime qué repito, qué re-explico y qué fuentes necesitaría."
- "Entrevístame de a una pregunta sobre mi negocio (cliente, oferta, cómo cobro, 3 dolores, canales) y con las respuestas escribe `business-brain.md` en la carpeta sandbox."
- "Crea el proyecto 'Contenido' con estas instrucciones: eres especialista en contenido; cuestiona mis supuestos; no halagues; si falta un dato, dilo. Luego propón qué archivos debo cargarle."
- "Resume en `core-context.md` (máx. 1 página) lo esencial de estos archivos y enlaces, separando hechos de suposiciones."

## Errores comunes
- Cargar todo el contexto como memoria global: infla cada mensaje.
- Crear 15 proyectos: consolida, salvo clientes que deban estar separados.
- Dejar que un chat largo acumule temas: abre ventana nueva por tema (sesiones de 30-45 min); el contexto viejo se sigue cargando.
- Dar acceso a carpetas personales o permitir borrado permanente.
- Tareas programadas muy frecuentes: gastan tokens; 1-2 al día suele bastar.
- Cowork consume límite más rápido que Claude Code: si se agota, pasa el trabajo pesado a Claude Code.

## Vigencia
Basado en Cowork de feb-abr 2026 (Projects, memoria por proyecto, tareas programadas). La interfaz, los límites de uso y los planes cambian rápido; verifica en la app. Las cifras de coste o ahorro citadas en la fuente: no verificado.

## Checklist de verificación
- [ ] El sandbox es una carpeta dedicada y el borrado permanente está denegado.
- [ ] El business-brain solo se lee por regla condicional.
- [ ] No hay más de 7-8 proyectos.
- [ ] Cada proyecto tiene instrucciones y un core-context.md.
- [ ] Solo hay conectores que usas de verdad.
