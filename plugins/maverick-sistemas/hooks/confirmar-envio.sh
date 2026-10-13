#!/bin/sh
# Todo envío de mensajes, publicación, cambio de contactos o flujos pide confirmación humana.
cat <<'J'
{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Esta acción puede enviar un mensaje, publicar o cambiar datos de clientes/flujos. Revisa el destinatario y el contenido y confirma explícitamente."}}
J
