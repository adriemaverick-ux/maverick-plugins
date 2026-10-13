---
name: endurecimiento-y-backup-agente
description: Endurece un agente que corre 24/7 en un servidor (VPS) o equipo propio y configura su respaldo automático sin secretos. Úsalo al desplegar o dejar un agente siempre activo; gatillos - VPS, SSH, firewall, hardening, servidor del agente, backup del agente, Railway, Telegram bot.
---

# Endurecimiento básico y backup del agente

## Objetivo
Reducir la superficie de ataque de un agente siempre encendido (con acceso a tus datos) y poder restaurarlo si falla. Si no necesitas 24/7, ejecutarlo en tu equipo suele ser más simple y seguro que un servidor sin endurecer; software alfa de agentes merece cautela extra.

## Pasos de endurecimiento
1. **Decide dónde vive**: equipo propio (opcionalmente en contenedor Docker para limitar acceso), VPS, o plataforma gestionada sin puertos abiertos. Evita conectar cuentas personales críticas a un agente experimental.
2. **Acceso SSH solo por llave**: crea una llave dedicada, desactiva el login por contraseña y deshabilita el acceso directo de root.
3. **Firewall activo**: deniega todo entrante por defecto y abre solo lo imprescindible. Prefiere arquitecturas donde solo sale tráfico (sin puertos públicos); no expongas el panel del agente a internet.
4. **Actualizaciones**: mantén el sistema y el agente al día; revisa qué cambia en cada versión.
5. **Canal de mensajería con lista blanca**: si usas un bot de Telegram u otro, permite solo tu ID de usuario; el token va en variable de entorno (ver `gestion-claves-entorno`).
6. **Mínimos privilegios del agente**: usuario sin privilegios, carpeta de trabajo acotada, conectores de solo lectura/borrador, sin envío ni pagos automáticos; aprobación humana para acciones de riesgo.
7. **Una sola instancia activa**: no corras la misma instancia en local y en la nube a la vez (duplica mensajes y acciones).
8. **Límites y vigilancia**: tope de gasto en proveedores, máximo de iteraciones por tarea, registro de comandos y alerta ante fallos de tareas programadas.
9. **Revisión de skills/repos de terceros** antes de instalarlos: escanea instrucciones ocultas o inyección de prompts; ponlos en cuarentena si dudas.

## Pasos de backup
1. Crea un **repositorio privado** espejo de configuración, personas/skills, soul y notas.
2. Excluye claves, tokens, `.env` y datos sensibles (`.gitignore`).
3. Programa un **respaldo nocturno** (cron o tarea programada) y revisa que realmente se ejecute.
4. **Prueba de restauración** trimestral en un entorno limpio.
5. Guarda un archivo de troubleshooting (cómo reabrir el panel, puertos, comandos clave).

## Prompts de ejemplo
- "Guíame paso a paso para endurecer mi servidor Ubuntu donde correrá el agente: llave SSH dedicada, sin login por contraseña, firewall con puertos mínimos. Muestra cada comando, explícame qué hace y espera mi confirmación antes de ejecutarlo."
- "Crea un respaldo nocturno de la configuración del agente en un repo privado. Antes, lista los archivos que se incluirían y confirma que no hay claves ni datos personales."
- "Audita mi instalación del agente: puertos abiertos, usuarios, permisos de conectores, tareas programadas y último respaldo. Entrega hallazgos por gravedad sin modificar nada."

## Errores comunes
- Servidor con contraseña root y puerto del panel abierto.
- Sin lista blanca en el bot: cualquiera puede mandarle órdenes.
- Respaldos con secretos incluidos.
- Nunca probar la restauración.
- Dar al agente permisos de envío o pago "porque está en un servidor seguro".
- Cerrar el portátil y olvidar que se cierran los puertos del panel local.

## Vigencia
Basado en guías de agentes de ene-jun 2026. Los comandos, proveedores y estado del software (alfa) cambian; consulta la documentación actual y trata las recomendaciones de hardening como mínimos, no como garantía de seguridad.
