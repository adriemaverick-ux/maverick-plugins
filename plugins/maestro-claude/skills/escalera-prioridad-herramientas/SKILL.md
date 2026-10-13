---
name: escalera-prioridad-herramientas
description: Decide cómo automatizar una acción eligiendo el método más fiable disponible - conector/MCP, luego plugin o API, luego navegador, y computer use como último recurso. Úsalo antes de automatizar algo o cuando una tarea sale lenta o frágil; gatillos - conector vs navegador, computer use, MCP, API, scraping, Claude in Chrome.
---

# Escalera de prioridad de herramientas

## Objetivo
Elegir siempre el método más rápido, estable y barato en tokens. Cuanto más abajo en la escalera, más lento y frágil: usa el escalón más alto que cubra la tarea.

## La escalera (de mejor a peor)
1. **Conector / MCP** oficial o personalizado (con OAuth). Más rápido y fiable; el MCP funciona como "manual de instrucciones" del servicio y gasta menos tokens que una API cruda.
2. **Archivos locales** de la carpeta de trabajo (lectura/escritura directa).
3. **Plugin o skill** ya instalado que empaqueta comandos + conectores.
4. **API directa con clave** (cuando no hay conector): más fiable que scraping de terceros. La clave va en variable de entorno (ver `gestion-claves-entorno`).
5. **Navegador (extensión de Chrome)** con tu sesión iniciada: sirve para webs sin API; más lento; descargas caen en la carpeta de Descargas.
6. **Computer use** (ver y controlar la pantalla): último recurso, para apps nativas sin integración.
7. **Claude Code** para pipelines pesados, scraping masivo o scripts propios (Cowork es más lento con scripts a medida).

## Pasos
1. Describe la tarea y qué sistema toca (correo, CRM, web, app de escritorio).
2. Recorre la escalera de arriba abajo: ¿hay conector? ¿API? ¿solo web? ¿solo app nativa?
3. Si no hay conector, busca uno personalizado (URL del servidor MCP + OAuth) antes de bajar. Valida el repositorio y su popularidad antes de instalar; lee qué permisos pide.
4. Concede el mínimo acceso (ver `conectar-herramientas-minimo-acceso`).
5. Prueba con una tarea real pequeña; si falla, baja un escalón, no insistas.
6. Documenta en el proyecto qué método usa cada tarea para no repetir la decisión.

## Prompts de ejemplo
- "Quiero [tarea]. Recorre esta escalera: conector, API, navegador, computer use. Dime qué opción existe en cada escalón, cuál recomiendas y qué permisos necesitaría. No ejecutes nada todavía."
- "No hay conector para [servicio]. Busca si existe un servidor MCP oficial, dime la fuente, su actividad y los permisos que solicita, y solo entonces propón añadirlo como conector personalizado."
- "Haz esta tarea con el navegador en una pestaña nueva para no contaminar el contexto; pide mi aprobación antes de cualquier acción que publique, envíe o pague."

## Errores comunes
- Usar computer use por defecto porque "funciona con todo": es lento y consume mucho.
- Scraping de terceros cuando existe API oficial.
- Instalar un MCP sin revisar quién lo mantiene ni qué permisos pide.
- Conectar decenas de servidores "por si acaso": inflan el contexto base.
- Pedir descarga a un sitio concreto estando en modo navegador: caerá en Descargas.
- Sitios como X restringen accesos automáticos y sus términos pueden bloquearlo: no construyas un proceso crítico sobre eso.

## Vigencia
Basado en Cowork y agentes de feb-sep 2026. La lista de conectores, el soporte de computer use por sistema operativo y las políticas de los sitios cambian; reverifica antes de depender de un escalón.
