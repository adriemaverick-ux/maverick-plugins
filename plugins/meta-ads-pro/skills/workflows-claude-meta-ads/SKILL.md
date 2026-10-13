---
name: workflows-claude-meta-ads
description: Úsala para correr auditorías, reportes programados, análisis de tendencias, minería de la Biblioteca de Anuncios y generación de ángulos con Claude sobre Meta Ads, con prompts listos y sus límites. Gatillos - "auditar cuenta Meta", "reporte semanal", "Biblioteca de Anuncios", "analizar tendencias", "por qué cayó el ROAS", "ad library".
---

# Workflows de Claude con Meta Ads

## Objetivo
Usar Claude donde funciona (análisis, auditoría, borradores, ángulos) y evitar donde falla (causalidad, análisis visual, decisiones de escalado sin contexto). Todo en solo lectura salvo aprobación.

## Pasos
1. Crear contexto persistente (CLAUDE.md): objetivo, margen, evento principal, ventana de atribución, calendario de promociones, lo prohibido (no activar, no tocar presupuesto).
2. Auditoría: ejecutar prompt A, y verificar 3-5 cifras en Ads Manager antes de actuar.
3. Tendencias: ejecutar prompt B; primero revisar el log de actividad (cambios, campañas terminadas) antes de explicar.
4. Reporte programado: ejecutar prompt C con tarea programada; la máquina debe estar despierta y un humano revisa antes de enviar a un tercero.
5. Biblioteca de Anuncios: elegir 5-10 competidores, filtrar país y "Activos", priorizar más días activos (proxy, no prueba), guardar capturas, y ejecutar prompt D. La API oficial cubre anuncios políticos y comerciales solo en UE/Reino Unido; para Perú, revisión manual en la web [vendor, no verificado].
6. Ángulos y hooks: dar objeciones reales de chats de WhatsApp (sin datos personales) y ejecutar prompt E.
7. Contrastar ventas con Shopify o CRM: Meta reporta conversiones atribuidas, no ingresos verificados.

## Plantillas / prompts listos
- A (auditoría): "Solo lectura. Confirma cuenta, moneda y zona horaria. Audita los últimos 30 días: estructura, señales (Pixel/CAPI), CPA por campaña a 7d clic y 1d clic, creativos (frecuencia, CTR, gasto). Tabla con severidad, evidencia exacta y acción propuesta. Marca 'no verificable' lo que no puedas demostrar. No cambies nada."
- B (tendencias): "Compara los últimos 7 días completos con los 7 anteriores. Antes de explicar, lista campañas terminadas o con cambios de presupuesto en el log. Luego variaciones de gasto, CPM, CTR de enlace, CPC, conversiones y CPA. Separa dato de hipótesis y di qué dato confirmaría cada hipótesis."
- C (reporte): "Con el MCP en solo lectura, genera el informe de los 7 días completos anteriores: gasto, resultados, CPA, frecuencia, top 5 y bottom 5 creativos, 3 acciones para aprobar. Si algo falla, escribe qué falló."
- D (Biblioteca): "Clasifica estos [N] anuncios: formato, hook, promesa, prueba, oferta, CTA, duración activa. Patrones por competidor y 5 huecos de mensaje. No infieras gasto ni rendimiento."
- E (ángulos): "10 ángulos distintos con 3 hooks de 3 s, 1 texto (<125 caracteres) y 1 título (<40). No inventes cifras ni testimonios; usa [FALTA PRUEBA]."

## Límites
- Las explicaciones causales fallan: en una prueba, Claude atribuyó a fatiga una caída que fue de una campaña terminada.
- Los números suelen cuadrar; los errores son de interpretación, configuración (clics vs clics de enlace) y atribución (7d clic + 1d vista infla retargeting).
- El MCP devuelve métricas, no mira imágenes; el análisis visual requiere pasar archivos a un modelo con visión.
- Si el prompt es ambiguo, el modelo puede inventar un número preciso.
- Claude no es el motor de reglas: usar reglas nativas o scripts con umbrales.

## Errores comunes
1. Aceptar la explicación causal sin revisar el log de actividad.
2. Declarar ganador un anuncio con pocos eventos.
3. Copiar creativos de competidores.
4. Reportar a un cliente sin revisión humana.

## Nivel de evidencia
- [oficial] Herramientas del MCP (`ads_get_ad_entities`, `ads_insights_anomaly_signal`, `ads_library_search`).
- [comunidad] Prompts y pruebas (e-dialog, Vaizle). [vendor] Supermetrics, Passionfruit, límites de la Biblioteca.
- [no verificado] Umbrales (frecuencia > 2.5-3, CPA > 1.5x) son puntos de partida de la comunidad.

## Vigencia
2026-10-11.
