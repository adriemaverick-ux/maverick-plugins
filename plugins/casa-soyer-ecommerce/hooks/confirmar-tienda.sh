#!/bin/sh
# Casa Soyer es una tienda de PRODUCCIÓN: toda escritura pide confirmación explícita.
cat <<'J'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Casa Soyer es la tienda real de Ana/Marbe. Esta acción modifica la tienda: confirma explícitamente antes de ejecutar (ediciones masivas requieren OK de Marbe/Ana, no solo de Adrie)."}}
J
