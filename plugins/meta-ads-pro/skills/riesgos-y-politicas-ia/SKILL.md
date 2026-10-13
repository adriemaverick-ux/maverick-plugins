---
name: riesgos-y-politicas-ia
description: Úsala antes de usar IA para crear anuncios o automatizar cambios en Meta Ads - divulgación de contenido con IA, automatización agresiva, privacidad de datos y cuentas restringidas. Gatillos - "etiquetar contenido IA", "AI info", "riesgo de baneo", "automatizar Meta Ads", "datos de clientes en IA", "AI disclosure".
---

# Riesgos y políticas de IA en Meta Ads

## Objetivo
Usar IA sin poner en riesgo la cuenta publicitaria, la marca ni los datos de clientes.

## Pasos
1. Divulgación: en anuncios políticos/sociales hay que divulgar imagen, video o audio realista hecho con IA; Meta detecta automáticamente desde 2026-06-01 y rotula "AI info" [oficial]. En anuncios comerciales, el etiquetado automático (C2PA, herramientas de Meta) viene de blogs [no verificado]; revisar la política vigente al lanzar.
2. Contenido: mostrar el producto real (no uno distinto al vendido), revisar manos, texto y logos, no crear "clientes reales" sintéticos ni testimonios fabricados.
3. Si el guion usa presentador sintético, incluir una línea de divulgación.
4. Automatización: patrón "agente propone, humano aprueba, script ejecuta con límites" (`--dry`, tope ±15-20% de presupuesto por día y entidad, backoff ante errores 613/17, bitácora) [comunidad].
5. No automatizar la interfaz de Ads Manager con navegador ni dejar bucles nocturnos con escritura.
6. Cuentas restringidas: hay reportes anecdóticos de 2026 tras operaciones masivas con tokens no oficiales; no hay política publicada de Meta que prohíba MCP de terceros ni conteos [no verificado]. La vía más segura a una restricción son los rechazos de política acumulados.
7. Privacidad: no pegar teléfonos, correos ni chats de clientes en un LLM o conector sin base legal; las audiencias personalizadas solo con hash y consentimiento, fuera del flujo de IA. Deshabilitar `ads_delete_custom_audience` y escritura de audiencias.
8. Tokens: variable de entorno, mínimo privilegio, system user por cliente, rotar, no subir a git.
9. Agencias o clientes: acuerdo escrito sobre acceso de IA y cambios.

## Plantillas / prompts listos
- Línea de divulgación: "Presentador generado con IA."
- Cláusula interna: "La IA solo propone. Cambios de presupuesto, activación, audiencias y mensajes a clientes requieren aprobación humana escrita."
- Prompt: "Revisa este anuncio contra riesgos: promesas de resultados, atributos personales, urgencia falsa, personas o testimonios sintéticos, texto en imagen. Lista cada riesgo con la política que lo sustenta o marca [NO VERIFICADO]."

## Errores comunes
1. Dejar un agente con permisos de escritura sin supervisión.
2. Usar tokens personales amplios en servidores de baja reputación.
3. Escalar presupuesto por regla de IA sin umbral mínimo de datos.
4. Usar imagen o voz de personas reales sin consentimiento (aplica la ley local aparte de Meta).
5. Urgencia falsa en piezas de stock limitado.

## Nivel de evidencia
- [oficial] Divulgación en anuncios políticos/sociales, detección automática desde 2026-06-01, canales aprobados (MCP/CLI).
- [comunidad]/[vendor] Disparadores de baneo (más de ~4 ediciones de presupuesto por adset por hora, más de ~10 de límite de gasto por día): [no verificado].
- [no verificado] Etiquetado de IA en anuncios comerciales; frase del Help Center sobre bloqueo con el MCP oficial.

## Checklist previo a publicar o automatizar
- [ ] Contenido con IA revisado y divulgado si corresponde.
- [ ] Producto mostrado idéntico al real; sin testimonios sintéticos.
- [ ] Ninguna escritura automática sin aprobación y límites.
- [ ] Sin datos de clientes en prompts.
- [ ] Política de Meta revisada en la fecha de lanzamiento.

## Vigencia
2026-10-11. Revisar la política de Meta cada trimestre.
