---
name: auto-conectar-llm-a-mensajeria
description: Usar cuando se quiera conectar Claude, GPT o Codex a Instagram/Messenger/WhatsApp vía ManyChat, GHL, n8n o una función en la nube. Gatillos "conectar IA a Instagram", "chatbot con IA", "External Request timeout", "LLM en DMs", "connect Claude to Instagram".
---

# Conectar un LLM a la mensajería (dentro de lo permitido)

## Objetivo
Usar un modelo de lenguaje como apoyo acotado (FAQs, resumen para el vendedor), nunca como vendedor autónomo. Claude Code y Codex sirven para escribir el código; el modelo que atiende al cliente en producción se llama por la API de Anthropic u OpenAI.

## Pasos
1. Elegir la ruta: (a) IA nativa de ManyChat o Conversation AI de GHL; (b) External Request a n8n o función en la nube; (c) integración directa con la API de Meta (fase 2). Para empezar, (a) o (b). [vendor/comunidad]
2. Patrón asíncrono por el timeout de 10 s de External Request de ManyChat: el endpoint responde 200 de inmediato, procesa con el LLM y entrega la respuesta después por la API de ManyChat (setCustomField + sendFlow o Send Content). Si no, el campo llega vacío. [comunidad]
3. Activar "Encode to JSON" y no entrecomillar a mano los placeholders del body. [comunidad]
4. El endpoint (n8n o función serverless) verifica un token propio, deduplica por message_id, carga memoria, llama al LLM con base de conocimiento corta y valida la salida.
5. Memoria: por contact_id/IGSID guardar los últimos 6-10 turnos, un resumen rodante, campos calificados, estado (bot/humano) y marca de tiempo para saber si sigue la ventana de 24 h. Definir retención (ej. 12 meses sin actividad) y borrado a pedido. [analista]
6. Escalado a humano: reglas fijas antes del LLM (precio, contrato, queja, "quiero hablar con alguien") derivan sin pasar por el modelo; máximo 3 turnos de IA por hilo. Ver auto-escalado-a-humano-y-calificacion.
7. Divulgación: el primer mensaje dice que es un asistente automatizado; nunca hacerse pasar por humano. [oficial]
8. Modo borrador primero: Conversation AI de GHL o el endpoint sugieren respuestas que un humano aprueba; activar auto-respuesta solo para FAQs y agenda tras pruebas con el simulador. [vendor]
9. Costos: medir tokens reales; el modelo pequeño cuesta fracciones de centavo por conversación. El costo dominante es el software y el tiempo del vendedor.
10. Seguridad: scopes mínimos, tokens en variables de entorno (nunca en documentos), tratar el texto del usuario como datos (inyección de instrucciones).

## Plantillas/ejemplos
```
ManyChat --External Request--> n8n webhook
   n8n: responde 200 -> busca memoria -> LLM (system prompt + FAQ)
        -> validador (sin precios, plazos, garantías inventados)
        -> API ManyChat: setCustomField(respuesta) + sendFlow
Si confianza baja: "No quiero equivocarme, te paso con una persona" + tag humano.
```
Prompt de sistema (resumen): responde solo con la base de conocimiento; no inventes precios, plazos ni descuentos; si no sabes, deriva; indica que eres un asistente automatizado.

Órdenes de magnitud (verificar en las páginas oficiales): 8 turnos de ~1.500 tokens de entrada y 150 de salida son unos 12.000 y 1.200 tokens; con un modelo pequeño es del orden de céntimos o menos. Precios por millón de tokens citados: Claude Sonnet 5.5 USD 2/10 y Haiku 5.5 USD 0,10/0,50 [oficial vía resumen de búsqueda, confirmar]; GPT-5 mini USD 0,25/2,00 [comunidad/no verificado]; GHL pay-per-use GPT-5 mini 0,25/2,00 [oficial].

## Errores comunes
- Esperar la respuesta del LLM dentro de los 10 s: falla con modelos grandes.
- Dejar que el LLM cotice, negocie o afirme garantías técnicas.
- Capturar datos sensibles (tarjetas, claves) por DM.
- Mensajes proactivos o reintentos insistentes fuera de ventana.
- Pegar tokens (GHL PIT, Meta, OpenAI) en prompts, notas o repositorios.
- WhatsApp: desde 2026-01-15 Meta prohíbe chatbots de IA de propósito general como producto; los bots de negocio acotados siguen permitidos. [vendor/comunidad, confirmar en términos oficiales]

## Nivel de evidencia
- Límites y reglas de Meta: [oficial]. Timeout de 10 s y patrón asíncrono: [comunidad]. Precios de LLM: [oficial/no verificado]. Calidad de la IA nativa de ManyChat: [vendor/comunidad]. Plantillas n8n con OpenAI: [comunidad, no verificadas de extremo a extremo].

## Fuente
Informe 01_manychat_dms_instagram.md (sección 4) y 02_ghl_crm_y_redes.md (secciones 3 y 6.4).

## Vigencia
2026-10-11.
