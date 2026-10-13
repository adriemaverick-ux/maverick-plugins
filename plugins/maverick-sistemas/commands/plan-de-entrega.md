---
description: Genera el plan de entrega de un piloto aceptado (recepción por WhatsApp, seguimiento de cotizaciones, agenda y próxima visita, panel del dueño, salida y mantenimiento) con pruebas, permisos y costos. No despliega nada.
argument-hint: "[negocio o ruta de la propuesta aceptada]"
---

Diseña el plan de entrega para: $ARGUMENTS

Usa el agente `arquitecto-de-entrega` y los skills `piloto-diseno-y-metricas-antes-despues`, `entrega-recepcion-de-consultas-whatsapp`, `entrega-seguimiento-de-cotizaciones`, `entrega-agenda-y-proxima-visita-recurrente`, `entrega-panel-simple-del-dueno` y `entrega-checklist-de-salida-y-mantenimiento`.

## Pasos
1. Lee la propuesta aceptada: alcance, qué queda fuera, métricas y línea base. Si no hay línea base, el primer tramo del plan es medirla.
2. Incluye solo los módulos del cuello elegido; el resto va como hoja de ruta posterior.
3. Entrega: diagrama del flujo, piezas y herramientas (GHL como fuente única cuando se pueda; n8n o Make solo si hace falta), cuentas y permisos, costos recurrentes y por uso, plan de pruebas con datos de prueba o autorizados, criterios para pasar a producción, forma de pausar y mantenimiento.
4. Redacta los mensajes y plantillas como borradores para aprobación, con aviso de asistente automático, consentimiento y baja.
5. Termina con el checklist de salida y la lista de pendientes por confirmar.

## Reglas
- Ningún despliegue, activación, envío ni cambio en cuentas del cliente sin confirmación humana expresa de Adrie, paso a paso.
- No pidas ni guardes contraseñas, tokens o API keys en archivos o chats.
- WhatsApp por canal oficial; no uses vías no oficiales en producción.
- No inventes cifras ni precios; resultados como "hipótesis a medir". Conserva las etiquetas de evidencia.
- No uses nombre, logo ni métricas de clientes sin autorización.
