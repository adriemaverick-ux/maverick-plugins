#!/usr/bin/env python3
"""Hook Stop: si esta respuesta produjo trabajo importante y no se escribió nada en la bóveda,
pide a Claude registrarlo antes de cerrar. Falla en silencio: nunca debe romper la sesión."""
import json, os, sys

def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    if data.get("stop_hook_active"):          # evita bucles: solo un recordatorio por respuesta
        return
    path = data.get("transcript_path")
    if not path or not os.path.exists(path):
        return
    vault = os.environ.get("MAVERICK_VAULT") or os.path.expanduser("~/Downloads/Maverick MP")
    vault_names = {os.path.basename(vault.rstrip("/")), "Maverick MP", "Casa Soyer"}

    last_user = -1
    events = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f):
            try:
                ev = json.loads(line)
            except Exception:
                continue
            events.append(ev)
            if ev.get("type") == "user":
                content = (ev.get("message") or {}).get("content")
                text = ""
                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    text = " ".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
                if text.strip() and "task-notification" not in text and "system-reminder" not in text and "SYSTEM NOTIFICATION" not in text:
                    last_user = len(events) - 1

    if last_user < 0:
        return
    tools = []
    for ev in events[last_user + 1:]:
        if ev.get("type") != "assistant":
            continue
        content = (ev.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        for b in content:
            if isinstance(b, dict) and b.get("type") == "tool_use":
                tools.append((b.get("name", ""), json.dumps(b.get("input", {}), ensure_ascii=False)))

    substantive_names = ("Write", "Edit", "NotebookEdit", "Bash", "Agent", "WebSearch", "WebFetch")
    substantive = sum(1 for n, _ in tools if n in substantive_names or n.startswith("mcp__")) >= 3 \
        or any(n in ("Write", "Edit") for n, _ in tools)
    if not substantive:
        return
    wrote_vault = any(n in ("Write", "Edit", "Bash") and any(v in inp for v in vault_names) for n, inp in tools)
    if wrote_vault:
        return
    reason = ("Antes de cerrar: en esta respuesta hubo trabajo con hallazgos o cambios y no se registró nada en la bóveda de Obsidian. "
              "Usa la skill registrar-hallazgos-en-obsidian: guarda decisiones, hallazgos (con su nivel de confianza), cambios, pendientes y próximos pasos "
              "en la nota que corresponda de la bóveda, anótalo en Bitácora IA.md, sin claves ni datos personales, y luego da a Adrie un resumen de una línea. "
              "Si no hubo nada importante que guardar, dilo en una línea y termina.")
    print(json.dumps({"decision": "block", "reason": reason}, ensure_ascii=False))

try:
    main()
except Exception:
    pass
sys.exit(0)
