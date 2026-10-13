---
name: auto-manychat-vs-ghl
description: Usar cuando Adrie deba decidir entre ManyChat, GoHighLevel (GHL) o ambos para automatizar Instagram/Facebook, o pregunte "ManyChat vs GHL", "¿necesito ManyChat?", "qué herramienta de chatbot uso", "which tool for comment-to-DM".
---

# ManyChat vs GHL: cuándo cada uno y arquitectura recomendada

## Objetivo
Elegir la herramienta mínima que cubra el comentario-a-DM y la calificación, evitando duplicar bandejas y costos. GHL es el CRM (fuente de verdad); ManyChat se evalúa solo si GHL muestra una limitación concreta.

## Pasos
1. Definir el caso: ¿es un solo operador con pocos leads/día y cierre por WhatsApp/llamada? Entonces empezar solo con GHL. [analista/comunidad]
2. Probar en GHL el disparador "Instagram - Comment(s) On A Post" (filtro por post y palabra clave, respuesta pública + DM). Está en la lista oficial de triggers. [oficial]
3. Anotar limitaciones reales: ramas conversacionales complejas, plantillas de crecimiento, reacciones/respuestas a stories por palabra clave. Los disparadores de story y DM por palabra clave en GHL solo los respalda una guía de agencia. [comunidad/no verificado]
4. Solo si hay limitación demostrada, evaluar ManyChat en plan de prueba para el tramo comentario-a-DM y enviar el lead a GHL por webhook/API cuando deje teléfono, correo o pida cotización.
5. Elegir UN gestor del inbox de Instagram. Si ambos se conectan a la misma cuenta pueden responder duplicado; probar si Meta tolera dos apps y, si no, dejar una sola. [no verificado]
6. Confirmar precios en las páginas oficiales el día de contratar (ver tabla).
7. Documentar la decisión y pedir aprobación humana antes de conectar la cuenta de Instagram.

## Comparación
| Tema | GHL | ManyChat |
|---|---|---|
| Comentario a DM por palabra clave | Sí (trigger + respuesta pública + DM) [oficial] | Sí, con Growth Tools y plantillas [vendor/comunidad] |
| Constructor de flujos de chat con ramas | Workflows, más orientado a CRM | Más maduro para chat [comunidad] |
| CRM, calendario, pipeline, cotizaciones | Nativo [oficial] | No |
| Story reply, anuncios Click-to-Instagram, IA nativa | Parcial / no verificado | Sí [vendor/comunidad] |
| Timeout External Request | n/a | 10 s [comunidad] |
| Precio | Starter USD 97/mes (3 sub-cuentas) [oficial]; IA y WhatsApp por uso | NO VERIFICADO: la página oficial dio 403 |

Precios de ManyChat: una fuente (eesel.ai, 2026-09-28) cita Free con 25 contactos, Essential 14, Pro 29 por mes en facturación anual; otras guías citan 1.000 contactos gratis y precios distintos. Tratar todo como [vendor/no verificado] y confirmar en manychat.com/pricing.

## Arquitectura recomendada (fase inicial)
```
Contenido (Social Planner / Metricool) -> comentario con palabra clave
   -> GHL workflow -> respuesta pública opcional + DM de calificación
   -> Contacto + Opportunity en GHL -> WhatsApp / llamada / calendario de demo
   -> Claude vía MCP oficial de GHL (lectura primero) para resúmenes y borradores
```
Fase 2 (si se justifica): ManyChat solo en el tramo de Instagram, LLM acotado por External Request (ver auto-conectar-llm-a-mensajeria), y webhook hacia GHL.

## Errores comunes
- Pagar ManyChat y GHL "por si acaso" y duplicar contactos facturables.
- Facturación de ManyChat por contacto activo (incluye DMs orgánicos): vigilar sobrecargos. [vendor]
- Guardar el token de GHL en archivos de documentación o chats: usar variables de entorno y rotar cada 90 días. [oficial]
- Asumir que Starter incluye todo el acceso API/MCP: verificar en Settings > Private Integrations. [no verificado]

## Nivel de evidencia
- Trigger de comentarios de GHL, precios de GHL: [oficial]. Preferencia por ManyChat en flujos de chat: [comunidad]. Precios y límites de ManyChat: [vendor/no verificado].

## Fuente
Informes 01_manychat_dms_instagram.md (sección 3) y 02_ghl_crm_y_redes.md (secciones 4.2, 5, 7).

## Vigencia
2026-10-11. Los precios cambian con frecuencia; reconfirmar antes de contratar.
