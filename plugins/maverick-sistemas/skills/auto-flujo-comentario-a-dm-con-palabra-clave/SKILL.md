---
name: auto-flujo-comentario-a-dm-con-palabra-clave
description: Usar para diseñar el flujo "comenta una palabra y te envío X" en Instagram (respuesta privada por comentario), con ejemplo para talleres, saneamiento y mantenimiento. Gatillos "comentario a DM", "comment to DM", "palabra clave", "lead magnet por Instagram", "CHECKLIST".
---

# Flujo comentario a DM con palabra clave

## Objetivo
Entregar un recurso útil a quien comenta una palabra clave, calificar con botones y pasar a un humano, cumpliendo las reglas de Meta y de Perú. Ningún flujo se activa sin que Adrie lo apruebe.

## Pasos
1. Elegir el recurso y la palabra clave (ej. CHECKLIST: lista de verificación de mantenimiento preventivo para taller). Publicar el reel/post con la instrucción exacta: "Comenta CHECKLIST y te lo envío por mensaje".
2. Configurar el disparador "comentario en esta publicación" (publicación específica, palabra clave con variantes). En GHL: "Instagram - Comment(s) On A Post"; en ManyChat: disparador de comentarios. [oficial/vendor]
3. Respuesta pública opcional y corta; variar el texto o no usarla (la repetición idéntica parece spam). [comunidad]
4. Respuesta privada (un solo mensaje, dentro de 7 días): saludo + aviso de asistente automatizado + un botón ("Recibir checklist"). El botón obliga a responder y abre la ventana de 24 h. [oficial]
5. Al tocar el botón: entregar el recurso y pedir consentimiento para guardar datos, con enlace a la política de privacidad y botones Sí/No.
6. Si Sí: etiqueta `lead_checklist`, campo `origen = comentario`. Si No: entregar solo el recurso y no guardar datos de contacto.
7. Calificación en 3 botones (tipo de negocio, tamaño, principal problema); guardar en campos.
8. Si califica (decisor + urgencia): ofrecer "Hablar con un asesor", etiqueta `calificado` + `humano`, pausar el bot y avisar al vendedor con resumen (ver auto-escalado-a-humano-y-calificacion).
9. Si no responde en 20-22 h: un único recordatorio dentro de la ventana, no promocional agresivo; luego cerrar. No insistir.
10. Probar con una cuenta de prueba, revisar errores (1545041, 613) y medir la semana siguiente.

## Plantillas/ejemplos
Ejemplo por nicho (mismo esqueleto, cambia el recurso):
| Nicho | Palabra | Recurso | Pregunta 1 |
|---|---|---|---|
| Taller | CHECKLIST | Checklist de mantenimiento preventivo | "¿Cuántos vehículos atiendes por semana? Menos de 20 / 20-100 / Más de 100" |
| Saneamiento | VISITAS | Plantilla de calendario de próximas visitas | "¿Cuántos clientes recurrentes tienes?" |
| Mantenimiento técnico | COTIZA | Formato de seguimiento de cotizaciones | "¿Cuántas cotizaciones envías al mes?" |

DM de apertura: "Hola, soy el asistente automatizado de Maverick Sistemas. Aquí está tu checklist: [enlace]. ¿Quieres que guardemos tu nombre y contacto para enviarte recursos relacionados? Política: [url]  [Sí] [No]".

## Errores comunes
- Enviar dos DMs por comentario: Meta solo permite una respuesta privada. [oficial]
- Primer mensaje sin botón: no hay interacción y no se abre la ventana de 24 h.
- Comentarios anidados (respuestas a otro comentario) pueden no activar el disparador. [comunidad]
- En publicaciones promocionadas los eventos de comentarios pueden no llegar; para anuncios usar Click-to-Instagram. [comunidad/no verificado]
- Los anuncios pueden duplicar notificaciones: deduplicar por comment_id. [oficial]
- Pedir teléfono o correo antes del consentimiento.
- Prometer en el DM precios o resultados sin base.

## Nivel de evidencia
- 1 respuesta privada por comentario, 7 días, 24 h: [oficial]. Comportamiento de disparadores y comentarios anidados: [comunidad]. Porcentajes de apertura (40-60%) son hipótesis, no benchmark: [no verificado].

## Fuente
Informe 01_manychat_dms_instagram.md (secciones 2.4, 6.3 Flujo A, 7); informe 02_ghl_crm_y_redes.md (sección 4.1).

## Vigencia
2026-10-11.
