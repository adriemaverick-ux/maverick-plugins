---
name: auto-que-permite-meta-y-que-no
description: Usar antes de diseñar cualquier automatización de DMs o comentarios en Instagram, Messenger o Threads, o cuando alguien pregunte "¿se puede enviar DMs automáticos?", "ventana de 24 horas", "Human Agent", "can I automate Instagram DMs", "cold DM", "scraping". Define qué permite Meta y qué queda prohibido.
---

# Qué permite Meta y qué no (automatización de mensajes)

## Objetivo
Fijar el marco de cumplimiento que toda automatización de Maverick Sistemas debe respetar antes de construir flujos. Regla central: el bot solo responde a acciones iniciadas por la persona. Ningún mensaje sale sin que un humano haya aprobado el flujo y los textos.

## Pasos
1. Confirmar que la cuenta de Instagram es profesional (Business o Creator) y que la automatización usa una API oficial de Meta, directa o a través de un partner aprobado (ManyChat, GHL). [oficial]
2. Verificar que cada conversación nace de una acción del usuario: comentario, respuesta a story, DM entrante, clic en anuncio Click-to-Instagram/Messenger, o enlace ig.me. [oficial]
3. Aplicar la regla de respuesta privada: un solo mensaje por comentario, dentro de 7 días desde el comentario (en Live solo durante la transmisión). Para continuar, la persona debe responder; ahí se abre la ventana de 24 h. [oficial]
4. Controlar la ventana de 24 h: dentro de ella se permite contenido promocional; fuera, ningún mensaje automático. Error 1545041 = ventana cerrada. [oficial]
5. Usar Human Agent solo para respuestas escritas manualmente por una persona, hasta 7 días tras el último mensaje del usuario, sin contenido promocional y sin automatización. Es un permiso que se solicita en App Review (con un partner, lo gestiona el partner). [oficial]
6. Incluir en el primer mensaje el aviso de asistente automatizado y ofrecer pasar a una persona. Meta lo exige "donde lo requiera la ley" y lo recomienda como buena práctica. [oficial]
7. Respetar los límites de tasa (ver skill auto-limites-de-api-por-plataforma); para el volumen de una pyme en Lima no son cuello de botella. [oficial]
8. Registrar toda excepción o duda en el plan de automatización y pedir confirmación humana antes de activar.

## Lo que Meta NO permite (prohibido, y por qué)
| Práctica prohibida | Por qué |
|---|---|
| DMs en frío o masivos no solicitados | Contra las políticas de mensajería de Meta; riesgo real de reportes de spam y bloqueo [oficial] |
| Scraping de seguidores, perfiles o comentarios de terceros | Los términos de Meta prohíben recolectar datos por medios automatizados sin permiso; riesgo de restricción de cuenta [oficial] |
| Herramientas que piden usuario y contraseña de Instagram | No usan OAuth ni API oficial; exponen la cuenta a bloqueo y robo de credenciales [oficial/vendor] |
| Bots no oficiales que simulan navegador o app | Violan los Términos de uso; riesgo alto de baneo [oficial/vendor] |
| Seguir/dejar de seguir, likes o comentarios automáticos en cuentas ajenas | Engagement automatizado; Meta ha litigado contra servicios de engagement falso [oficial] |
| Etiquetas (tags) para promoción fuera de la ventana | Las etiquetas son solo no promocionales [oficial] |
| Hacerse pasar por humano | Contra la política de divulgación de automatización [oficial] |

No se documentan aquí técnicas de evasión de detección: no existen en este plugin.

## Plantillas/ejemplos
- Primer DM válido: "Hola, soy el asistente automatizado de Maverick Sistemas. Aquí tienes lo que pediste. Si prefieres hablar con una persona, toca 'Hablar con un asesor'."
- Respuesta pública opcional (variar o no usar): "Te lo envié por mensaje."

## Errores comunes
- Pensar que "Human Agent" permite que el bot siga escribiendo 7 días: no, solo respuestas humanas.
- Diseñar un segundo mensaje de seguimiento fuera de las 24 h con etiqueta promocional.
- Dejar que ManyChat/GHL y otra app respondan a la vez en la misma cuenta (respuestas duplicadas); usar Conversation Routing o un solo gestor del inbox.
- Confiar en blogs de proveedores que dicen "sin riesgo" o "aprobado por Meta": comprobar que sean partners.
- Desde 2026-04-27 las etiquetas CONFIRMED_EVENT_UPDATE, ACCOUNT_UPDATE y POST_PURCHASE_UPDATE devuelven error 100; Human Agent no se ve afectada. [oficial]

## Nivel de evidencia
- Respuesta privada (1 por comentario, 7 días), ventana 24 h, Human Agent, tags, límites de tasa: [oficial].
- Eventos de comentarios que dejan de llegar en publicaciones promocionadas: [comunidad/no verificado].
- Que Meta exija verificación de negocio para Advanced Access en mensajería de Instagram: [no verificado].
- Nota de riesgo en Perú: ver auto-cumplimiento-peru (corta; decisión de Adrie de no tratar las leyes locales como bloqueo).

## Fuente
Informe 01_manychat_dms_instagram.md (secciones 2, 5, 6.2) en Maverick Research; páginas de Meta: Private Replies, Send a Message, Messenger Platform policy, Conversation Routing.

## Vigencia
2026-10-11. Revisar el changelog de Meta cada trimestre.
