---
name: auto-limites-de-api-por-plataforma
description: Usar cuando haya que consultar límites, cuotas, tokens o permisos de las APIs de Instagram, Facebook, Threads, YouTube, Google Business Profile, GHL o WhatsApp. Gatillos "límite de la API", "rate limit", "cuota", "API limits", "cuántos posts por día".
---

# Límites de API por plataforma

## Objetivo
Tener una tabla de referencia con etiquetas de evidencia para diseñar automatizaciones que queden muy por debajo de los topes. Verificar las cifras críticas en la consola o documentación antes de construir.

## Pasos
1. Identificar la plataforma y la operación (mensajería, publicación, analítica).
2. Consultar la tabla y la etiqueta de evidencia.
3. Si la etiqueta es [no verificado], medir en una cuenta de prueba (ej. GET content_publishing_limit en Instagram, cuota en Google Cloud Console).
4. Diseñar con reintentos, backoff y deduplicación (comment_id, message_id, webhookId).
5. Registrar uso y alertas; revisar el changelog de cada plataforma cada trimestre.

## Tabla de límites
| Plataforma | Límite o regla | Etiqueta |
|---|---|---|
| Instagram Send API | 300 llamadas/seg por cuenta (texto/links); audio/video 10/seg; Conversations API 2/seg | [oficial] |
| Instagram respuestas privadas | 750/hora por cuenta (posts y reels); Live 100/seg; 1 por comentario, 7 días | [oficial] |
| Instagram alto volumen | Más de 72.000 mensajes enviados y recibidos pierde visualización y envío hasta bajar | [oficial] |
| Messenger | 300/seg por Página; 200 llamadas por usuario en 24 h; umbral alto volumen 40 mensajes/seg | [oficial] |
| Ventana de mensajería | 24 h; Human Agent 7 días solo manual; error 613 = límite, 1545041 = ventana | [oficial] |
| Instagram publicación | 100 posts/24 h según una sección, 50 según otra de la misma página; carrusel hasta 10 | [oficial, contradictorio]; usar 50 |
| Instagram límites generales | 4.800 x impresiones de la cuenta por 24 h (no mensajería) | [oficial] |
| Facebook Reels API | 30 por Página/24 h; 3-90 s; programar entre 10 min y 29 días | [oficial] |
| Facebook posts programados | 10 min a 30 días | [oficial] |
| Threads | 250 posts/24 h; 500 caracteres; video hasta 5 min; token largo 60 días | [oficial] |
| Threads DMs | No hay API oficial confirmada | [no verificado] |
| YouTube Data API | 10.000 unidades/día por defecto; subida ~100 unidades desde 2025-12-04; cubos propios desde 2026-06-01 | [oficial], cifra exacta [no verificado]: ver consola |
| YouTube Shorts | Hasta 3 min, vertical o cuadrado | [comunidad] |
| Google Business Profile API | 300 consultas/min tras aprobación (0 = no aprobado); perfil verificado 60+ días y sitio web | [oficial] |
| GHL API v2 (OAuth) | Ráfaga 100 solicitudes/10 s; 200.000/día por app y recurso | [oficial]; para PIT [no verificado] |
| GHL webhooks | Reintentos hasta 12; firma X-GHL-Signature (Ed25519); la firma RSA caducó el 2026-09-01 | [oficial] |
| GHL MCP | Límites no especificados | [no verificado] |
| ManyChat External Request | Timeout 10 s | [comunidad] |
| ManyChat precios y contactos | Cifras contradictorias entre fuentes | [vendor/no verificado] |
| WhatsApp en GHL | Ventana 24 h; 72 h en entry points gratuitos (CTWA) si se responde en 24 h | [oficial] |

## Plantillas/ejemplos
Registro de uso: fecha, plataforma, llamadas hechas, errores (613, 1545041, 190, 10), acción tomada.
Regla de diseño: no superar el 20% del tope documentado; ante 613 o 429, esperar y reintentar con backoff.

## Errores comunes
- Tratar una cifra de blog como tope oficial.
- No renovar tokens (Threads 60 días; LinkedIn en GHL ~60 días) y no detectar el fallo.
- Usar nombres de métricas retiradas (impresiones y fans de Facebook retiradas 2025-11-15; plays/video_views de IG 2025-04-21). [oficial]
- Olvidar que Meta cambió etiquetas el 2026-04-27 (error 100).

## Nivel de evidencia
Etiquetado fila por fila arriba. Cifras de cuota de YouTube y de publicación de IG se contradicen en las propias páginas oficiales; verificar en la consola.

## Fuente
Informes 01 (2.5, 2.6), 02 (6.1-6.4) y 03 (sección 2) de Maverick Research.

## Vigencia
2026-10-11. Los límites cambian; reconfirmar antes de construir.
