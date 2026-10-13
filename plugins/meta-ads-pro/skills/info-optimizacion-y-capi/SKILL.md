---
name: info-optimizacion-y-capi
description: Define eventos de optimización y CAPI para infoproductos, incluida Conversion Leads y envío de compra desde pasarela o CRM. Usar cuando se pregunte "qué evento optimizar", "CAPI desde Hotmart/CRM", "Conversion Leads", "optimize for purchase vs lead".
---

# Optimización y CAPI para infoproductos

## Objetivo
Alimentar a Meta con la señal correcta según el ticket y enviar eventos de negocio reales (compra, llamada, calificado) por Conversions API.

## Pasos
1. Elige evento por objetivo:
   - Venta barata: Compra con valor. Regla práctica ~50 eventos por conjunto por semana para salir de aprendizaje [un experto/benchmark; Meta no lo confirmó en lo leído].
   - Webinar: Registro y, con volumen, "Asistió".
   - Aplicación + llamada: Lead de aplicación; con volumen, "llamada agendada/calificado".
   - Lead magnet + WhatsApp: Lead o conversación iniciada; mide lead que responde y que compra.
2. Conversion Leads exige: formularios instantáneos, CRM conectado, al menos 200 leads al mes, etapa objetivo dentro de 28 días de la captación y tasa de esa etapa entre 1% y 40% [oficial]. Si no llegas a 200, optimiza al evento más profundo que sí tenga volumen.
3. CAPI (guía oficial): `action_source` en todos los eventos; `event_source_url` y `client_user_agent` en web; `external_id` y `event_id` siempre; más datos de cliente mejoran Event Match Quality; hashea tú los parámetros si no usas SDK.
4. Deduplicación: mismo `event_name` y `event_id` entre Pixel y CAPI.
5. Eventos: ViewContent/PageView (Pixel), Lead o CompleteRegistration (Pixel+CAPI), InitiateCheckout, Purchase con valor y moneda (webhook de pago aprobado desde pasarela), llamada agendada/asistió/calificado (CRM a CAPI), reembolso (evento propio o ajuste manual).
6. Prueba con Test Events y concilia semanalmente contra la pasarela.
7. Consentimiento: obtén permisos legales antes de compartir datos de clientes.
8. Estructura simple: prospección con pocos conjuntos amplios, retargeting por etapa, exclusión de compradores [oficial: best practices + un experto].

## Plantillas / prompts
- Tabla de mapeo: `evento | origen | parámetros | dedup (event_id) | prueba hecha`.
- "Revisa este webhook de compra y dime qué parámetros CAPI faltan."

## Errores comunes
- Optimizar por lead barato sin medir lead a venta.
- Pixel y CAPI sin `event_id` común (doble conteo).
- Enviar Purchase sin valor o sin datos de emparejamiento.
- Esperar que Meta reste reembolsos automáticamente [no verificado].
- Prometer CAPI sin consentimiento.

## Nivel de evidencia
- Requisitos de Conversion Leads y CAPI: [oficial].
- ~50 eventos/semana, exclusión de detailed targeting eliminada el 31-mar-2025: [no verificado] en fuente oficial.
- Event Match Quality solo disponible para eventos web: [oficial]; para conversion leads u offline, consultar a Meta.
- Fricción en formularios (verificación de teléfono): [un experto], no verificado en documentación oficial.

## Vigencia
2026-10-11. Cualquier cambio de presupuesto o lanzamiento requiere aprobación humana.

## Relacionados y aprobación humana
- Skills relacionados: `info-economia`, `info-checklist-prelanzamiento`.
- Ningún gasto, lanzamiento ni cambio de presupuesto sin aprobación humana explícita.
- Si un dato falta, usa marcadores `<...>` y márcalo [no verificado]; no inventes cifras.
- Este skill no contiene promesas de ingresos ni técnicas de evasión de políticas.
