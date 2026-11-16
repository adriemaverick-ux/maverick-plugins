---
name: juez-diario-solo-lectura
description: '"El juez" de Meta Ads con Claude Code - revisión diaria del laboratorio que propone apagar, mantener, escalar o variar cada anuncio según CPA y gasto, registra aprendizajes y deja un reporte, en SOLO LECTURA (Adrie aprueba cada cambio). Incluye la estructura de campañas (laboratorio, escala, remarketing) y cuándo abrir cada una. Usar con "juez", "regla de apagado", "rutina diaria de ads", "piloto automático", "laboratorio", "qué apago hoy".'
---

# El juez diario (solo lectura)

Fuente: curso «Meta Ads con Claude» de Benjamín Cordero (oct-2026) [experto, cuenta de US$2.500–3.000/día]. Bóveda: `04 - Conocimiento/02 - Hallazgos/Meta Ads con Claude - aprendizajes del curso de Benjamín Cordero (2026-10)`.

## Lo que hace Cordero (referencia, no copiar tal cual)
- **Métricas:** solo **CPA y CPM**.
- **Apaga** un anuncio si gastó más del umbral con 0 compras, **o** si su CPA supera el umbral. El umbral sale de su CPA promedio (US$100 → US$120–150).
- **Escala:** con 2 o más compras y el CPA bajo el umbral, pasa el anuncio a la campaña de escala.
- **Aprendizajes:** en cada corrida anota qué funcionó y por qué (ángulo, título, formato) y deja un reporte cada mañana.
- **Rutina:** con Claude Code Routines sube creativos, juzga y escala **sin aprobación**. Para marcas «serias» propone aprobar los creativos de a 30, una vez por semana.
- **Error suyo:** borró su campaña real por accidente.

## La versión de Maverick
1. **Corre a diario en solo lectura**, con una tarea programada o a pedido. Lee el conector de Meta Ads y el `tablero-costo-por-venta`.
2. **Propone; no ejecuta.** Por cada anuncio del laboratorio sugiere una de cuatro acciones, cada una con su evidencia:
   - **Apagar:** gastó 1,5–2× el **CPA máximo** de la oferta sin ventas, o su CPA supera el máximo con volumen suficiente.
   - **Mantener:** todavía no tiene datos.
   - **Escalar:** dentro de la misma campaña, +20 %, mientras el presupuesto no permita una campaña de escala.
   - **Variar:** CPA bueno pero con fatiga (frecuencia alta, CTR que cae) → otro título fijo u otro gancho.
3. **Adrie aprueba** y Claude ejecuta solo lo aprobado. **Nunca se borra nada, solo se pausa.**
4. **Registro:** en cada corrida anota el aprendizaje en la bóveda: qué ángulo, título o formato ganó y por qué.
5. **CPA máximo = valor del cliente − costo variable**, sin los costos fijos.
   - **Golden ratio** = valor del cliente ÷ CPA.
   - Se calcula por separado para la **web** (US$997, ventas por WhatsApp con CAPI de mensajería) y para el **kit** (US$97).
6. **Señal:** sin la CAPI de mensajería, Meta no ve las ventas de WhatsApp, así que el juez usa el **costo por conversación calificada** hasta que el puente esté listo (`puente-ghl-whatsapp-a-meta`).

## Estructura de campañas
- **Nombres con color:** 🟢 Laboratorio · 🟠 Escala · 🔴 Remarketing.
- **Laboratorio:** público amplio, mensaje del problema y **un conjunto por formato** (videos Lego, imágenes HTML, «todo es un anuncio» = Reels orgánicos con el final de anuncio), en CBO.
- **Con US$10–35 al día: solo el laboratorio.**
  - **Escala** (~1–2 de cada 10 ganadores) y **remarketing** (web 90 días, seguidores 90 días, vistas de más de 3 s; mensaje de la solución) se abren cuando haya presupuesto y unas 50 conversiones por semana.
  - Mover anuncios de campaña reinicia el aprendizaje: no hacerlo a cada rato.

## Copy y título
- **Título fijo sobre el video** («always-on title»): cambiarlo da una variación nueva del mismo video y baja la fatiga.
- **Llamar a quién le hablas:** «Oye tú, dueño de empresa de fumigación que…».

## Riesgos de automatizar cambios
- Subir muchos anuncios por día a una cuenta nueva acumula rechazos y puede terminar en una restricción. Ir de a pocos y revisar las políticas.
- Las acciones automáticas sin humano pueden borrar o apagar lo que no se debía. El error de Cordero lo demuestra.
- Con poco presupuesto, el juez necesita semanas de datos: no decidir con menos de 3 a 7 días.

## Vigencia
2026-11-15.

## Relacionados
`tablero-costo-por-venta`, `ciclo-semanal-claude-meta`, `reglas-de-decision`, `lego-system-videos-modulares`, `proteccion-de-cuenta`.
