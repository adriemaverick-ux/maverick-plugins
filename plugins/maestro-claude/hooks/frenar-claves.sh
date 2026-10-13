#!/bin/sh
# Pide confirmación si lo que se va a escribir parece una clave/token pegado en un archivo.
IN=$(cat)
if printf '%s' "$IN" | grep -Eq 'sk-[A-Za-z0-9_-]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{10,}|sb_secret_[A-Za-z0-9_-]{10,}'; then
cat <<'J'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Esto parece una clave o token pegado en un archivo. Usa una variable de entorno (.env fuera de git) en vez de escribirla en el código."}}
J
fi
exit 0
