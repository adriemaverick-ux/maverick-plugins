---
name: ecom-estructura-advantage-sales-y-manual
description: Úsala para decidir entre Advantage+ Sales y campañas manuales, y cómo separar prospección, retargeting y exclusiones en una tienda Shopify. Gatillos - "Advantage+ Sales", "ASC", "existing customer cap", "prospección vs retargeting", "estructura de campañas ecommerce", "campaign structure".
---

# Estructura: Advantage+ Sales vs manual (ecommerce)

## Objetivo
Definir una estructura mínima de campañas para una tienda Shopify de ticket alto con poco volumen, sin fragmentar la señal y con exclusiones correctas.

## Pasos
1. Entender el cambio de plataforma: Meta unificó Advantage+ Shopping/App en "Advantage+ Sales" (mayo 2025);
   ASC/AAC se eliminan por versión de API (v24.0 impide crear/editar, v25.0 lo elimina) [oficial, Meta Developers 3-jun-2025].
2. Recordar que el Existing Customer Budget Cap no está disponible en campañas Advantage+ nuevas [oficial vía documentación de API y Jon Loomer].
   Algunas guías de 2026 dicen lo contrario [no verificado]. Comprobar en Ads Manager antes de planificar.
3. Para separar prospección de clientes existentes, usar campañas manuales: (a) conjunto que excluye audiencias de clientes;
   o (b) dos conjuntos (solo clientes / amplio excluyendo clientes) con límite de gasto en el de clientes [oficial vía Jon Loomer].
4. Estructura recomendada para ticket alto con poco volumen (pocas campañas): A) prospección amplia (Advantage+ o manual);
   B) retargeting pequeño de alta intención (visitantes de pieza, WhatsApp iniciado, carrito, 7-30 días);
   C) prueba creativa ABO separada solo si el gasto lo permite [un experto + razonamiento propio].
5. Elegir el objetivo según volumen: compra si hay cerca de 50 eventos/semana por conjunto (poco probable en piezas únicas) [un experto];
   si no, mensajes/leads con eventos de CRM (ver `ecom-ticket-alto-pieza-unica`).
6. Exclusiones: compradores (lista de clientes + píxel 180 días) fuera de prospección;
   piezas vendidas fuera del retargeting dinámico;
   opcional, quienes ya abrieron conversación en 7-14 días si el equipo no da abasto [razonamiento propio].
7. Validar la mezcla durante 4-6 semanas con datos propios;
   no hay consenso publicado sobre splits (10-15% a 40% para retargeting según agencia) [un experto, fuentes en conflicto].
8. Cualquier creación o cambio de presupuesto queda en borrador/pausa hasta que el humano lo apruebe.

## Plantillas / prompts
- Prompt: "Con estos datos (eventos/semana, ticket, clientes en lista, stock activo), propón estructura de 2-3 campañas con exclusiones, objetivo y evento de optimización.
   Marca cada afirmación con su etiqueta. No actives nada."
- Tabla de estructura: campaña | objetivo | audiencia | exclusiones | evento | tope de gasto (lo define el usuario).

## Errores comunes
1. Fragmentar en muchos conjuntos con pocos eventos cada uno.
2. Buscar el tope de clientes existentes en la UI nueva y asumir que existe.
3. Retargeting sin techo: la audiencia es pequeña y sube frecuencia sin ventas [razonamiento propio].
4. Copiar splits de agencias (60/25/15) como si fueran reglas; son heurísticas en conflicto [un experto].
5. Lookalike manual por inercia: Advantage+ audience es el predeterminado;
   pasar la lista como sugerencia y probar contra manual en cuenta propia [un experto].

## Nivel de evidencia
- Cronología y retiro de ASC/ECBC: [oficial] (el detalle de UI actual: verificar).
- Splits de presupuesto y calidad de semilla: [un experto], sin consenso.
- Pausa de retargeting por "Polaris": [no verificado].

## Vigencia
2026-10-11. Meta cambia esta estructura con frecuencia; reverificar en Ads Manager antes de ejecutar.
