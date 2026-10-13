---
name: filtro-decision-plugins
description: Decide si un proceso debe ser un skill, un comando o un plugin completo mediante tres pruebas (repetición, cadena, traspaso). Úsalo antes de empaquetar algo para compartir; gatillos - ¿plugin o skill?, crear plugin, compartir con el equipo, empaquetar flujo, plugin.json.
---

# Filtro de decisión: skill, comando o plugin

## Objetivo
Evitar plugins innecesarios. Un plugin empaqueta comandos + skills + conectores + referencias + README para compartir; solo vale la pena si el proceso pasa el filtro. Muchos "equipos de agentes con organigrama" son solo archivos `.md` sobreingenierizados: la mejor herramienta es la que realmente usas.

## Las tres pruebas
1. **Repetición**: ¿lo ejecutas más de una vez por semana?
2. **Cadena**: ¿tiene 3 o más pasos y toca 2 o más herramientas (p. ej. vídeo -> transcripción -> Notion)?
3. **Traspaso**: ¿otra persona podría ejecutarlo sin preguntarte nada?

## Pasos
1. Describe el proceso y responde las tres pruebas con sí/no.
2. Resultado:
   - 0-1 síes: no es plugin. Si se repite, es un **skill**; si es una instrucción única, déjalo en el proyecto.
   - Falla traspaso: primero documenta el proceso (pasos, reglas, ejemplos) y vuelve a evaluar.
   - 3 síes: crea el **plugin**.
3. Estructura mínima: `plugin.json` (nombre, versión, descripción), `commands/*.md` (acciones con "/"), `skills/` (conocimiento), referencias, lista de conectores requeridos y `README` con instalación y prueba.
4. Declara los permisos y conectores necesarios y los mínimos: nada de enviar/publicar sin confirmación humana.
5. Prueba la instalación en limpio (otro perfil o equipo) y confirma que un tercero lo ejecuta solo con el README.
6. Versiona los cambios y anota una fecha de revisión.
7. Si lo vas a compartir, revisa que no lleve claves, datos de clientes ni rutas personales.

## Prompts de ejemplo
- "Aplica el filtro repetición / cadena / traspaso a este proceso: [describe]. Responde sí/no a cada prueba y recomienda skill, comando o plugin, con una frase de justificación."
- "El proceso falla el test de traspaso. Redacta la documentación paso a paso, con entradas, salidas y casos de error, para que otra persona lo ejecute sin mí."
- "Genera la estructura del plugin (plugin.json, commands, skills, README) para este flujo, sin incluir credenciales y marcando qué acciones requieren mi confirmación."

## Errores comunes
- Empaquetar como plugin algo que haces una vez al mes.
- Plugins gigantes con 20 skills sin uso: engordan el contexto.
- Compartir con claves o ids personales incrustados.
- No probar la instalación desde cero.
- Confiar en plugins prediseñados sin leer qué hacen; en la práctica el valor real de un plugin propio es compartir con equipo o comunidad.

## Vigencia
Basado en Cowork (mar 2026), donde los plugins aparecían con "/" en la interfaz. La estructura exacta de plugins y la gestión desde la app pueden haber cambiado; revisa la documentación actual de tu versión.
