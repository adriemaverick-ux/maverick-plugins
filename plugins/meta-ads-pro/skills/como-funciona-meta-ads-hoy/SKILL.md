---
name: como-funciona-meta-ads-hoy
description: Explica cómo funciona Meta Ads en 2026 (subasta, Andromeda, GEM, Advantage+, atribución). Usar cuando el usuario pregunte "cómo funciona Meta Ads", "qué es Andromeda", "Advantage+ o manual", "why did my results drop", o necesite contexto antes de decidir estructura o creativos.
---

# Cómo funciona Meta Ads hoy (2025-2026)

## Objetivo
Dar un modelo mental correcto y actualizado del sistema para que las decisiones de cuenta no se basen en mitos. Separar siempre lo que Meta documenta de lo que interpretan las agencias.

## Pasos
1. **Subasta.** Gana el anuncio de mayor valor total: puja x tasa de acción estimada + calidad del anuncio, con un multiplicador de pacing. La puja más alta no siempre gana. [oficial]
2. **Tres capas de IA.** Retrieval (Andromeda) preselecciona unos miles de anuncios entre decenas de millones; ranking (GEM, y desde jul-2026 un "Generative Recommender" basado en LLM); luego la subasta. [oficial]
3. **Palanca principal = creatividad.** Meta dice que la diversificación creativa es la mejor palanca para encontrar audiencias relevantes. Diversidad = concepto/ángulo, formato y persona distintos, no variantes cosméticas. [oficial vía Loomer]
4. **Advantage+ por defecto.** Ventas, Clientes potenciales y App traen presupuesto de campaña, audiencia, placements y creatividad Advantage+ activados, desactivables uno a uno. Las campañas heredadas ASC/AAC ya no se pueden crear/actualizar (API v25.0). [analista, citando a Meta]
5. **Menos control manual.** Exclusiones de detailed targeting eliminadas, intereses retirados (15-ene-2026), prueba de eliminación de exclusión de placements por conjunto. Intereses y lookalikes actúan como sugerencia; en categorías especiales (vivienda, empleo, crédito) siguen restrictivos. [analista]
6. **Atribución más corta.** Desde 12-ene-2026 no existen 7d_view/28d_view en la API de Insights; desde mar-2026 "clic" = solo clic en enlace. Una caída en cifras reportadas no implica caída real. [analista citando a Meta]
7. **Fase de aprendizaje.** Referencia ~50 eventos de optimización por conjunto en 7 días; es guía, no ley. [analista]
8. **Click-to-WhatsApp.** Devolver eventos por CAPI ligados a `ctwa_clid` permite optimizar por calidad y no solo por conversaciones. [analista]
9. **Estado agéntico.** El asistente de IA que crea campañas está "en pruebas"; exige vista previa y aprobación. Automatización total NO disponible a oct-2026. [oficial]

## Plantillas / prompts
- "Explica en 5 líneas, con etiqueta de confianza, por qué cayeron mis resultados reportados desde enero 2026 y qué verificar primero (ventana de atribución, definición de clic, ventas reales)."
- "Revisa mi estructura y dime qué controles manuales que uso ya no existen o están en retirada."

## Errores comunes
- Creer que "Andromeda agrupa anuncios similares y 50 variantes = 1 boleto" como hecho: es hipótesis de agencias. [no verificado]
- Creer que "los intereses no sirven para nada" (mito parcial) o que "con amplio no importan las señales" (mito inverso: calidad de CAPI/Pixel sigue clave). [analista]
- Usar la cifra "22% más ROAS con Advantage+ creative" como promesa: es autoinformada por Meta, no auditada. [oficial autoinformado]
- Crear otra cuenta para saltarse una restricción: riesgo de escalar a restricción del Business Manager. No recomendado.
- Atribuir toda caída de 2025-2026 a Andromeda sin revisar oferta, estacionalidad, competencia y medición. [un experto: Loomer]

## Nivel de evidencia
- Subasta, Andromeda/GEM (existencia y rol), roadmap de oct-2026: [oficial].
- Cambios de atribución, Advantage+ unificado, retiro de intereses: [analista] (medios que citan a Meta).
- Fechas de CTC (Creative diversity 26-ago, Messenger Stories 27-ago, términos 30-oct) y umbral de 25 conversiones: [no verificado].
- Cifras de mejora de Meta (GEM, Andromeda) son autoinformadas y no separan el efecto de la creatividad del anunciante.

## Vigencia
Informe base: 2026-10-11. Revisar tras el despliegue de la eliminación de exclusiones de placement y los términos del 30-oct-2026. Verificar en el Help Center de Meta antes de actuar sobre cambios recientes.

## Cómo usar este skill
- Citar siempre la etiqueta de confianza junto a cada afirmación.
- Si el usuario pide una acción (cambiar estructura, presupuesto), pasar a `estructura-de-cuenta-y-campanas` o `reglas-de-decision`.
- Cualquier cambio que gaste dinero requiere confirmación humana.
