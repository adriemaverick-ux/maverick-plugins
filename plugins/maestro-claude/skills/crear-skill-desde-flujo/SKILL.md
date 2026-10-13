---
name: crear-skill-desde-flujo
description: Convierte un flujo que ya funcionó en un skill reutilizable usando skill-creator, con pruebas y bucle de mejora. Úsalo cuando repitas una tarea o termines algo bien hecho. Triggers - crear skill, skill creator, conviértelo en skill, SKILL.md, automatizar flujo, super skill.
---

# Crear un skill desde un flujo probado

## Objetivo
Capturar un proceso que ya dio buen resultado en un skill con disparador claro, pasos, formato de salida y comprobaciones, para repetirlo igual sin volver a explicarlo.

## Pasos
1. Haz primero el flujo a mano al menos una vez hasta obtener un resultado bueno. No crees el skill de una idea abstracta.
2. Decide el tipo: "mejora de capacidad" (rellena una carencia actual del modelo; puede caducar) o "preferencias codificadas" (tu forma de trabajar; durable). Anótalo en el skill.
3. Usa el plugin skill-creator (instálalo desde /plugin si no lo tienes) y declara intención y resultado deseado; deja que te entreviste (alcance, cuándo se dispara, entradas, formato de salida, memoria, fuentes de datos).
4. Redacta el frontmatter: name en kebab-case igual al directorio y una description con cuándo usarlo y palabras gatillo.
5. Escribe el cuerpo: objetivo, pasos numerados, ejemplos de prompt, errores comunes, vigencia. Mantenlo breve; detalle largo a archivos aparte.
6. Añade condiciones verificables ("máximo una página; comprueba que no se excede") y un paso de revisión final.
7. Prueba con una muestra real y con un caso límite; da feedback y pide que actualice el skill. Compara si el modelo lo hace igual de bien sin el skill; si sí, quizá no lo necesitas.
8. Dale "ojos" y memoria solo si aporta: conectores/MCP con mínimo acceso (skill conectar-mcp-minimo-acceso) y archivo de contexto actualizable.
9. Guarda en el directorio de skills del usuario (global) o del proyecto, según el alcance, y revisa que no contenga claves.
10. Tras cada uso, califica la salida y pide que el skill incorpore la lección.

## Prompts de ejemplo
- "Convierte lo que acabamos de hacer en un skill. Usa skill-creator. Intención: producir X cada semana a partir de Y. Entrevístame antes de escribirlo."
- "Añade al skill una comprobación final: si el resultado supera una página, recórtalo y vuelve a verificar."
- "El resultado de hoy fue flojo en esto: [problema]. Actualiza el skill para evitarlo y explica qué cambiaste."

## Errores comunes
- Descripción vaga: el skill nunca se activa o se activa siempre.
- Skill enorme que consume contexto en cada sesión.
- Meter claves o datos personales en el archivo.
- No probar con casos reales ni límite.
- Crear skills para lo que el modelo ya hace bien sin ayuda.

## Checklist de cierre
- Flujo probado manualmente antes.
- Descripción con cuándo y palabras gatillo.
- Probado con caso real y caso límite.
- Sin claves ni datos personales.

## Vigencia
- Instalación del plugin skill-creator, evals y ruta de skills dependen de la versión de Claude Code; confirma en la documentación.
- Los skills de tipo "mejora de capacidad" pueden quedar obsoletos al mejorar el modelo: revisa trimestralmente.

## Variante Cowork / Agentic OS
### Crear un skill desde un flujo probado

## Objetivo
Guardar procedimientos repetibles solo cuando ya demostraron funcionar. Regla práctica: si lo haces 2 veces por semana, merece skill; si aún no sale bien a mano, no lo codifiques.

## Pasos
1. **Hazlo a mano con Claude** hasta que el resultado te guste. Divide el trabajo en pasos pequeños (cuantas más tareas juntas, peor rinde).
2. **Da reglas y ejemplos propios**: formato, longitud, tono, "haz/no hagas". Pasa 2-3 muestras reales de tu escritura y pide que derive reglas de estilo.
3. **Pregunta qué necesita**: "¿qué herramientas, APIs o archivos necesitas para hacerlo siempre igual?". Claude te guía; guarda las claves como variables de entorno, nunca dentro del skill.
4. **Pide crear el skill** con el skill creator y revisa el flujo propuesto antes de guardar. Pide que haga preguntas de aclaración si hay ramas (p. ej. "¿texto o imagen?").
5. **Prueba con casos reales**: lanza 2-3 casos de prueba (en paralelo si se puede), mira salidas y da feedback. Itera.
6. **Evalúa**: compara contra Claude sin el skill; si no mejora, no lo uses.
7. **Evita duplicados**: antes de guardar, lista los skills existentes y fusiona si hay solapamiento.
8. **Descripción corta y con gatillos** (cuándo usarlo, palabras que lo activan): la descripción se carga en cada turno, cada palabra cuesta.
9. **Estructura**: `SKILL.md` + `references/` (guías, config) + `scripts/` + `assets/` (logos, plantillas). El skill debe leer assets de forma dinámica, no copiarlos.
10. **Pruébalo en un chat nuevo** y anota en una línea "última revisión".

## Prompts de ejemplo
- "Acabamos de hacer [proceso] y quedó bien. Crea un skill que lo repita. Primero muéstrame el flujo en pasos, las reglas que dedujiste y las preguntas que te faltan. No lo guardes aún."
- "Antes de crear el skill, revisa mis skills actuales y dime si alguno ya cubre esto. Si sí, propón fusionarlo en vez de crear uno nuevo."
- "Ejecuta 3 casos de prueba con el skill y compáralos con la salida sin el skill. Dime si mejora y en qué."
- "Recorta la descripción a 2 frases con cuándo usarlo y 6 palabras gatillo."

## Errores comunes
- Codificar un proceso mediocre: automatizas el error.
- Skills enormes con descripciones largas: encarecen cada turno.
- Duplicar skills casi iguales con nombres distintos.
- Guardar secretos o datos personales dentro del skill.
- Instalar skills de terceros sin leer qué hacen: pide un resumen y revisa posibles instrucciones ocultas antes de aceptar.
- Olvidar que en algunas apps el skill se pide en lenguaje natural y en Claude Code se invoca con `/`.

## Vigencia
Basado en Cowork y Claude Code (mar-ago 2026). Las funciones de evals y `/learn` son recientes y pueden cambiar de nombre o comportamiento; confirma en tu versión.

## Checklist de verificación
- [ ] El proceso funcionó bien a mano al menos una vez.
- [ ] No existe ya un skill que lo cubra.
- [ ] La descripción tiene cuándo usarlo y palabras gatillo.
- [ ] No hay claves ni datos personales en el skill.
- [ ] Lo probaste en un chat nuevo.

