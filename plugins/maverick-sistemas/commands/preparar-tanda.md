---
description: Prepara una nueva tanda de prospección (solo redacta y registra, no envía), aplicando la regla "manda nuevos" y evitando duplicados.
argument-hint: "[cantidad, por defecto 5] [sector: saneamiento | mantenimiento | equipos] [ángulo opcional]"
---

Usa el agente `prospector-maverick` para preparar una tanda con estos argumentos: $ARGUMENTS

Pasos:
1. Lee el registro de outreach completo y aplica la regla "manda nuevos": los contactos de la tanda anterior pasan a Enviado (por regla acordada) con la fecha de hoy. Muéstrame esos cambios antes de escribir el registro si hay más de cinco o algo no cuadra.
2. Propón candidatos que pasen `prosp-filtro-de-prospectos`, con señal de encaje verificada y fuente. Descarta duplicados por nombre, teléfono o dominio.
3. Asigna un ángulo distinto a cada candidato y redacta la apertura según `prosp-mensaje-inicial-y-tono` (breve, sin exclamaciones, aclara que no es cliente, una sola pregunta).
4. Registra la tanda como **Pendiente de envío**. No incluyas teléfonos en el resumen; remíteme al registro.
5. Aplica las reglas de plataforma de `prosp-cumplimiento-peru-consentimiento` (nota corta de riesgo; no es bloqueo).

No envíes nada. El envío es manual y lo confirmo yo.
