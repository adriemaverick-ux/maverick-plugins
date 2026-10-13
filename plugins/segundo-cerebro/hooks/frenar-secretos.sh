#!/bin/sh
# Pide confirmación si lo que se va a escribir parece un token o clave (por ejemplo en una nota de la bóveda).
IN=$(cat)
if printf '%s' "$IN" | grep -Eq 'pit-[A-Za-z0-9-]{20,}|sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{10,}|AKIA[0-9A-Z]{16}|sb_secret_[A-Za-z0-9_-]{10,}'; then
cat <<'J'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Esto parece un token o clave pegado en un archivo. Guárdalo en un gestor de secretos o variable de entorno, no en la bóveda ni en el código."}}
J
fi
exit 0
