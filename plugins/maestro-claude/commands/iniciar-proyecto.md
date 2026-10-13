---
description: Inicia un proyecto de Claude Code - entrevista, CLAUDE.md, memoria, política de modelos y permisos mínimos.
argument-hint: "[ruta-del-proyecto] [objetivo en una frase]"
---

Inicia o reconfigura el proyecto indicado en: $ARGUMENTS

Si no se indicó ruta, usa el directorio actual. Sigue estos pasos con el agente arquitecto-claude-code y los skills del módulo:

1. Plan mode y entrevista previa (plan-mode-entrevista-previa): explora la carpeta sin modificar nada y hazme las preguntas necesarias sobre objetivo, público, stack, restricciones y qué NO debe tocarse. Una pregunta a la vez.
2. CLAUDE.md (claude-md-proyecto): propón el contenido (propósito, stack, comandos, reglas, decisiones, criterios de éxito verificables). Si ya existe, propón cambios en vez de sobrescribir y guarda copia.
3. Memoria (memoria-tres-niveles): crea la carpeta memory/ con archivos de decisiones y próximas acciones, y define el skill de cierre de sesión si procede.
4. Modelo y esfuerzo (enrutar-modelo-esfuerzo): propón una política por tipo de tarea y regístrala en CLAUDE.md.
5. Integraciones (conectar-mcp-minimo-acceso): lista las que haga falta con alcance mínimo. No pidas ni escribas claves; solo nombres de variables de entorno y comprobar que .env está en .gitignore.
6. Permisos: sugiere reglas de permiso concretas (lectura permitida, acciones de envío, borrado o publicación con aprobación). No desactives confirmaciones.
7. Muestra un resumen de todo lo que vas a crear o editar y espera mi confirmación antes de escribir archivos. Tras aplicar, verifica y entrega el resumen con cómo revertir.
