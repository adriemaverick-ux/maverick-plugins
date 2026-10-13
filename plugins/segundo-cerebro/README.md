# segundo-cerebro v1.0

Guarda en tu bóveda de Obsidian (`~/Downloads/Maverick MP`, o la ruta de `MAVERICK_VAULT`) lo importante de cada conversación.

**8 skills · 2 subagentes · 5 comandos · 2 hooks**
- Skills: registrar-hallazgos-en-obsidian, wrap-up-de-sesion, estructura-de-boveda, captura-rapida, revision-semanal, reporte-consolidado-3-negocios, higiene-de-claves, memoria-del-negocio.
- Comandos: /wrap-up, /capturar, /revision-semanal, /reporte-consolidado, /auditar-claves.

**Cómo funciona el guardado automático**
Claude Code no tiene un evento de "terminó la conversación". El hook se dispara cada vez que Claude termina de responder: si esa respuesta incluyó trabajo importante (escribió o editó archivos, o usó varias herramientas) y no se escribió nada en la bóveda, le pide registrar los hallazgos antes de cerrar. Máximo un recordatorio por respuesta. Si no hubo nada importante, no molesta. Probado con transcripciones simuladas; no probado en vivo.

**Límites**
- Puede añadir un paso extra al final de respuestas con trabajo. Para desactivarlo, quita el bloque `Stop` de `hooks/hooks.json`.
- No detecta el final real de la conversación.
- No registra si cierras la app sin que Claude termine de responder.
- Si el trabajo se hizo en otra bóveda (por ejemplo Casa Soyer), el hook lo reconoce por el nombre de la carpeta.

**Seguridad:** el hook de secretos pide confirmación si intentas escribir un token en un archivo. Pendiente tuyo: el token de GHL en `GHL - Integracion privada.md`; rotarlo.
