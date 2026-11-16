---
name: valor-por-lead-y-escalera
description: 'Cómo puntuar leads (calculadora, chat) y mandarle a Meta su valor y la escalera de eventos (CalcStart → Lead → QualifiedLead → Purchase) para que aprenda a traer empresas que compran, con lo que sí y lo que no funciona en cuentas chicas. Usar al definir eventos, al decidir qué optimizar, o con "valor del lead", "lead scoring", "QualifiedLead", "optimizar por valor", "eventos secuenciados", "value rules".'
---

# Valor por lead y escalera de eventos

## La verdad corta
- Puedes mandar `value` y `currency` en **cualquier** evento, incluso como valor estimado [oficial: developers.facebook.com/documentation/ads-commerce/conversions-api/guides/value-optimization].
- Para que Meta **optimice por valor** hacen falta unas 30 compras con 5 valores distintos en 14 días, o 100 eventos que no sean compra en 14 días [experto: Loomer, jun-2025]. **Con US$10–35 al día no se llega.**
- No hay nada oficial que diga que Meta use el `value` cuando optimiza por cantidad [no verificado].
- **Igual se manda:** no cuesta nada, sirve para medir cada anuncio y deja historial para cuando haya volumen. Esto es criterio propio.

## Escalera para Maverick
**Web (kit y calculadora).** Todo va por píxel + API con el mismo `event_id`:
1. Empieza a usar la calculadora → evento personalizado `CalcStart`.
2. Deja su contacto → `Lead` con `value` según el puntaje, por ejemplo US$0, 20 u 80.
3. Puntaje alto → `QualifiedLead` (evento personalizado).
4. Compra el kit → `Purchase` por US$97.

**WhatsApp (web de US$997).** Se envía `QualifiedLead` y `Purchase` (997) con `ctwa_clid` por la API de conversiones de mensajería (ver `puente-ghl-whatsapp-a-meta`). Meta no deduplica ese canal.

## Puntaje simple (por reglas, no por modelo)
Las guías para cuentas chicas recomiendan una marca binaria o un puntaje por reglas [proveedor, 2025]. Las preguntas salen de la calculadora o del chat:
- ¿Es dueño o encargado de una **empresa** de control de plagas o fumigación? (si no, valor 0)
- ¿Cuántos técnicos salen a campo? (1 = bajo; 2–4 = medio; 5 o más = alto)
- ¿Cuántos servicios hace al mes?
- País (para la moneda y el precio).
- ¿Tiene web? (para la oferta de la web)

**Ejemplo:** independiente = US$0 (sin `QualifiedLead`); 2–4 técnicos = US$20; 5 o más técnicos = US$80 + `QualifiedLead`. Los montos se ajustan con las ventas reales.

## Qué optimizar según el volumen
- **Hoy:** optimizar por `Lead` (o por uso de la calculadora si los leads son pocos). Los eventos de más abajo se mandan solo como señal.
- **Con unos 25 a 50 `QualifiedLead` por semana:** optimizar por `QualifiedLead` (evento personalizado), como hace Loomer [experto, 2026].
- **Eventos secuenciados («maximizar leads calificados» en web, `Lead` → `QualifiedLead`):** está en prueba desde oct-2026, pide la API de conversiones y unos 30 eventos en 7 días para que aparezca [experto: Loomer, 2026-10-06]. Probarlo solo si aparece la opción.
- **Kit:** pasar a `Purchase` cuando haya unas 30 compras por semana.
- **WhatsApp:** pasar a «maximizar compras por WhatsApp» cuando Meta lo habilite (ver `novedades-meta-2026-11`).
- **No usar** Value Rules ni «maximizar valor» hasta tener volumen: sin un problema concreto que resolver, solo suben el costo [experto: Loomer].
- **Conversion Leads** pide unos 200 leads al mes y formularios instantáneos [oficial]. No aplica por ahora.

## Errores comunes
- Valores inflados o todos iguales: confunden el ROAS y no enseñan nada.
- Mandar un valor distinto por el píxel y por la API para el mismo evento.
- Optimizar por un evento con menos de unos 25 por semana y esperar estabilidad.
- Preguntar demasiado en la calculadora: cada pregunta extra baja los leads.

## Vigencia
2026-11-13. Revisar los umbrales y la disponibilidad de los eventos secuenciados fuera de EE. UU.

## Relacionados y aprobación humana
`info-optimizacion-y-capi`, `calificacion-de-leads-whatsapp`, `pixel-y-capi-setup`, `tablero-costo-por-venta`. Ningún cambio de optimización ni de gasto sin la aprobación de Adrie.
