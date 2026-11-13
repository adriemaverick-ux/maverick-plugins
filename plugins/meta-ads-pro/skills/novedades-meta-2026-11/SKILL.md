---
name: novedades-meta-2026-11
description: Cambios de Meta Ads verificados entre oct-2025 y nov-2026 que actualizan el resto del plugin (investigación base del 2026-10-11) - regla de 50 conversiones reafirmada, optimización por compras y leads en WhatsApp, Advantage+ por defecto, fin de las exclusiones de segmentación, diversidad creativa, AEM. Usar antes de planear o auditar una campaña, o con "qué cambió en Meta", "novedades Meta Ads", "está actualizado".
---

# Novedades de Meta Ads (al 2026-11-13)

> Esta skill **manda** sobre las cifras más viejas del plugin cuando choquen.

## Cambios
1. **Regla de unas 50 conversiones por semana por conjunto: sigue vigente.** Meta la reafirmó en oct-2026 y dice que por debajo el costo por compra fue cerca de 28 % mayor (sin método publicado) [oficial vía PPC Land, 2026-10-25: ppc.land/meta-says-ad-sets-under-50-weekly-conversions-cost-28-more-per-purchase]. Pide agrupar los cambios para no reiniciar el aprendizaje.
2. **WhatsApp optimiza por compras o leads, no solo por conversaciones.**
   - Configuración: objetivo Ventas en modo manual, destino de mensajes → WhatsApp y meta «maximizar compras por WhatsApp». Para leads: objetivo Clientes potenciales con «leads de mayor calidad».
   - Resultados reportados por Meta: costo por compra −10 % y costo por lead −24 % frente a optimizar por conversaciones.
   - La opción aparece «al cumplir criterios» que Meta no publica.
   - Hace falta la API de conversiones para mensajería con `ctwa_clid` (ver `puente-ghl-whatsapp-a-meta`).
   - [oficial: whatsappbusiness.com/resources/resource-library/down-funnel-optimizations-whatsapp, aprox. mar-2026]
3. **Advantage+ es el flujo por defecto** en Ventas y Leads desde 2025; Advantage+ shopping pasó a llamarse Advantage+ sales [oficial vía prensa, feb-2025].
4. **Segmentación:** Meta quitó las exclusiones de segmentación detallada y fusionó intereses. Dice que quitar las exclusiones mejoró la mediana del costo por conversión en 22,6 % [oficial vía prensa, ene-2025]. En la práctica: público amplio y el anuncio nombra al cliente.
5. **Diversidad creativa:** Meta pide «diversificar, probar y dejar optimizar» [declaración a prensa, 2026-09-29]. Lo de que los anuncios casi iguales cuentan como uno (Entity ID) **no** está confirmado por Meta. Loomer: variar concepto, ángulo, formato y persona, no retoques menores; Meta retiró la recomendación de 6 anuncios por conjunto [experto, 2025-08/12].
6. **GEM** (modelo de ranking): +5 % de conversiones en Instagram y +3 % en el Feed de Facebook en el 2T-2025 [oficial: engineering.fb.com, 2025-11-10].
7. **AEM:** ya no hace falta priorizar 8 eventos ni verificar el dominio para eso [experto: Loomer]. Igual se verifica el dominio, para controlar los enlaces.
8. **Stripe no acepta comerciantes en Perú** (2026-11-13) [oficial: stripe.com/global].
9. **Retargeting con poco presupuesto:** no conviene una campaña aparte. Mejor varios anuncios en secuencia dentro de una campaña amplia [experto: Nick Boddington, 2026-03].

## Qué cambia en las demás skills
- `plan-de-prueba-inicial`, `estructura-de-cuenta-y-campanas`, `campana-click-to-whatsapp`: sumar la escalera de eventos y la optimización por compras en WhatsApp.
- `info-audiencia-primero` y `marca-flujo-organico-a-pauta`: son opinión, no veto (decisión de Adrie).
- Pagos: ver `info-peru-pagos-y-legal`, ya actualizada.

## Vigencia
2026-11-13. Revisar cada mes.

## Relacionados y aprobación humana
`como-funciona-meta-ads-hoy`, `testeo-creativo-y-fatiga`, `puente-ghl-whatsapp-a-meta`. Ningún gasto ni cambio de presupuesto sin la aprobación escrita de Adrie.
