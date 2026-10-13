---
description: Genera el reporte semanal de Meta Ads (solo lectura) con datos vs hipótesis, calidad de leads y 3 acciones para aprobar.
argument-hint: "[cuenta o negocio: casa-soyer | inmobiliario] [fecha inicio opcional] [ruta de CSV opcional]"
---

Genera el reporte semanal de Meta Ads para: $ARGUMENTS

Sigue `workflows-claude-meta-ads`, y consulta `mcp-meta-ads-solo-lectura`, `calificacion-de-leads-whatsapp` y `riesgos-y-politicas-ia`.

Pasos:
1. Fuente de datos: si hay MCP o CLI conectado, úsalo en solo lectura; si no, pide un CSV exportado (campaña, conjunto y anuncio por día, 14+ días) o la ruta indicada. Nunca pegues listas de clientes ni teléfonos.
2. Confirma cuenta, moneda y zona horaria antes de calcular. Usa los 7 días completos anteriores frente a los 7 previos.
3. Antes de explicar variaciones, lista campañas terminadas y cambios de presupuesto o del log de actividad.
4. Incluye: gasto, conversaciones, conversaciones calificadas, citas, ventas y margen (si el usuario los aporta), CPA o costo por conversación, frecuencia, top 5 y bottom 5 creativos con gasto. Calcula costo por etapa, no solo CPL.
5. Separa DATO de HIPÓTESIS; las causas son hipótesis, con el dato que las confirmaría. Marca "datos insuficientes" donde haya pocos eventos.
6. Cierra con 3 acciones recomendadas para aprobación humana. No cambies nada en la cuenta, no actives ni modifiques presupuestos, no envíes mensajes.
7. Etiqueta cualquier benchmark ([benchmark], [no verificado]) y recuerda que Meta reporta conversiones atribuidas, no ingresos verificados: contrasta con Shopify o CRM.
8. Guarda el informe como `reportes/AAAA-MM-DD.md` solo si el usuario lo confirma; si un paso falla, escribe qué falló en lugar de omitirlo. Vigencia 2026-10-11.
