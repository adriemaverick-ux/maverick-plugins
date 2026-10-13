#!/bin/sh
# Toda escritura en una cuenta publicitaria (crear, activar, presupuesto, pausar, borrar) pide confirmación humana.
cat <<'J'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Esta acción modifica una cuenta de Meta Ads y puede gastar dinero. Revisa el detalle (campaña, presupuesto, estado) y confirma explícitamente. Por defecto trabajamos en solo lectura."}}
J
