---
name: campana-click-to-whatsapp
description: Úsala para diseñar, revisar u optimizar una campaña Click-to-WhatsApp (CTWA) de ticket alto, optimizando por calidad (conversación calificada, venta) y no por conversación barata. Gatillos - "campaña a WhatsApp", "click to WhatsApp", "CTWA", "optimizar por conversaciones", "CAPI WhatsApp", "ctwa_clid".
---

# Campaña Click-to-WhatsApp (estructura y optimización por calidad)

## Objetivo
Armar una campaña CTWA que aprenda de cierres reales. Para ticket alto, la conversación iniciada es la señal más débil del embudo; se mide costo por conversación calificada y por venta, no solo por conversación.

## Pasos
1. Definir el negocio: pieza o línea, margen, ticket, quién cierra (en Casa Soyer, Adrie por WhatsApp). Confirmar que existe un número en WhatsApp Business Platform (BSP o desarrollo propio). La app gratuita WhatsApp Business no emite webhooks, por lo tanto no hay CAPI-BM ni optimización por compra [oficial].
2. Fase 1 (semanas 1-3, aprendizaje): 1 campaña, 1-3 conjuntos amplios (Lima + provincias con envío), optimización por CONVERSATIONS, 3-5 creativos por pieza o línea. Guardar el `ctwa_clid` de cada chat desde el día 1 [oficial].
3. Instrumentar CAPI para Business Messaging: `action_source=business_messaging`, `messaging_channel=whatsapp`, `user_data` con `whatsapp_business_account_id` y `ctwa_clid`; `custom_data` con `currency` y `value` en Purchase [oficial].
4. Fase 2 (calidad): enviar `QualifiedLead` y `Purchase`. Comparar costo por conversación vs por conversación calificada vs por venta. Mover presupuesto al conjunto o creativo con mejor costo por venta.
5. Fase 3 (escala): optimizar por Purchase solo si hay volumen de eventos; mantener una campaña de conversaciones de respaldo. Umbral ~50 eventos/semana por conjunto [no verificado].
6. Mensaje de bienvenida: continuar la promesa del anuncio (ver skill `cierre-ticket-alto-por-chat`). Registrar tiempo de primera respuesta.
7. Venta cerrada fuera del chat (transferencia, showroom): registrarla en el CRM y enviar `Purchase` con el `ctwa_clid` guardado, el mismo día.
8. Escribir cambios en la cuenta solo con aprobación humana; crear siempre en pausa.

## Plantillas / prompts listos
- Prompt de diseño: "Con estos datos (pieza, precio, margen, stock real, zona de entrega), propón estructura CTWA en 3 fases, 3 creativos por pieza y los eventos CAPI a enviar. No actives nada; entrega un borrador en pausa para aprobación."
- Tabla de lectura por etapa: conversaciones, % que responde 2 turnos, calificadas, citas, cotizaciones, ventas, margen. Costo = gasto / cantidad de cada etapa.
- Eventos válidos: LeadSubmitted (no "Lead"), QualifiedLead, Purchase, InitiateCheckout, OrderCreated, entre otros [oficial].

## Errores comunes
1. Celebrar CPL bajo sin medir calificación ni venta.
2. No guardar `ctwa_clid` ni enviar eventos; Meta no aprende de los cierres.
3. Eventos tardíos, duplicados (Meta no deduplica) o con `value` incorrecto.
4. Catálogo dinámico con piezas únicas sin stock sincronizado; mejor creativos por pieza ancla.
5. Optimizar por Purchase en Instagram: no disponible, Meta sugiere conversaciones [oficial].
6. Depender de una sola meta de optimización (en 2023 Meta pausó temporalmente "initiated conversations") [caso].

## Nivel de evidencia
- [oficial] CAPI-BM, eventos, parámetros, facturación por IMPRESSIONS en CTWA, Purchase no disponible en Instagram.
- [benchmark] Afirmación de 24% menor costo por lead optimizando por leads frente a conversaciones: dato de plataforma sin verificación independiente.
- [no verificado] Extensión del objetivo Leads a CTWA con preguntas en Ads Manager; confirmar en tu cuenta. Umbral de ~50 eventos/semana.

## Checklist antes de aprobar
- [ ] Número en WhatsApp Business Platform (no app gratuita).
- [ ] `ctwa_clid` guardado por conversación.
- [ ] Criterio de "calificado" escrito.
- [ ] Stock real confirmado de cada pieza anunciada.
- [ ] Todo creado en pausa; activación manual por Adrie.
- [ ] Responsable de responder en menos de 5 min definido.

## Vigencia
2026-10-11. Revisar al abrir cada campaña: opciones de objetivo y destino cambian en Ads Manager.
