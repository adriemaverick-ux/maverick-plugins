# casa-soyer-ecommerce (plugin)

Negocio paralelo de Adrie: ecommerce y pauta de Casa Soyer por comisión sobre margen bruto.

**Incluye:** 6 skills · 4 subagentes · 5 comandos (`/cs-auditar`, `/cs-campana`, `/cs-comision`, `/cs-limpieza`, `/cs-reporte`) · MCP (Shopify Dev, Storefront de casasoyer.com) · hook de seguridad que pide confirmación ante toda escritura en la tienda.

**Sin credenciales:** el plugin no trae claves. Para leer/escribir la tienda real conecta el conector de Shopify en tu cuenta de Claude.

**Límites:** el MCP Storefront es público y solo lee catálogo; los datos de ventas/costos y Meta Ads requieren los conectores propios de tu cuenta. El hook solo cubre herramientas MCP cuyo nombre incluya update/delete/bulk/create/etc.
