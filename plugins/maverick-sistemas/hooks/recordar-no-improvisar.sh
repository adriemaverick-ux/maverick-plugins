#!/bin/bash
# Recordatorio permanente de Adrie: nunca improvisar. Se inyecta como contexto al iniciar la sesión y en cada mensaje.
EVENTO="${1:-SessionStart}"
python3 - "$EVENTO" <<'PY'
import json,sys
ev=sys.argv[1]
txt=("REGLA PERMANENTE DE ADRIE (nunca improvisar): antes de responder, escribir o construir algo, busca y lee lo que ya existe en los plugins "
     "(skills, comandos, agentes) y en las bóvedas de Obsidian (Maverick MP y Casa Soyer). Usa plantillas y frases fijas tal cual (p. ej. la plantilla de 9 bloques), "
     "respeta sus decisiones vigentes (nicho, mercado hispano + latinos en EE. UU., USD, sin IA, formato C, modo claro), no inventes cifras ni funciones de herramientas, "
     "y si falta información investiga con fuentes o pregunta una cosa corta. Lee la skill no-improvisar.")
print(json.dumps({"hookSpecificOutput":{"hookEventName":ev,"additionalContext":txt}}))
PY
