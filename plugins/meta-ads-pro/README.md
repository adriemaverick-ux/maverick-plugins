# meta-ads-pro v1.2

Plugin de Meta Ads construido sobre 11 informes de investigación (2026-10-11) en `~/Downloads/Meta Ads Research/`.

**66 skills · 9 subagentes · 12 comandos**
- Base (34): estrategia y auditoría · creativos · medición, Pixel/CAPI y protección de cuenta · WhatsApp, ticket alto, Perú y Claude+IA.
- Por negocio (32): `ecom-*` (Casa Soyer / Shopify) · `saas-*` · `marca-*` (marca personal) · `info-*` (infoproductos).

## Novedades 1.2.1 (2026-11-14)
Se suman aprendizajes del tutorial de Meta Ads de Adrián Sáenz y Roger Viladrosa (jul-2024), filtrados contra lo vigente, a `tablero-costo-por-venta`, `ciclo-semanal-claude-meta` y `fabrica-de-anuncios`.

## Novedades 1.2.0 (2026-11-13)
Sistema Claude + Meta de Maverick. **9 skills nuevas:**
- `novedades-meta-2026-11`: manda sobre las cifras viejas.
- `puente-ghl-whatsapp-a-meta`: GHL no envía el `ctwa_clid`.
- `valor-por-lead-y-escalera`.
- `pagina-por-anuncio`.
- `fabrica-de-anuncios`: zonas seguras, 9:16 y 4:5, un video por hook.
- `formatos-trial-reels-y-colaboracion`.
- `b2b-duenos-mundo-hispano`.
- `tablero-costo-por-venta`.
- `ciclo-semanal-claude-meta`.

**Cambios en skills existentes:**
- Sin Hotmart; infraestructura propia (`info-economia`, `info-optimizacion-y-capi`, `info-peru-pagos-y-legal`): Stripe no acepta Perú; Polar o Lemon Squeezy para el kit; Culqi o dLocal Go para servicios.
- `info-audiencia-primero` y `marca-flujo-organico-a-pauta` quedan marcadas como opinión, no como veto (decisión de Adrie: los ads prueban ofertas).

**Comandos:** /auditar-cuenta-meta, /plan-campana-meta, /brief-creativo, /guiones-anuncio, /revisar-tracking-meta, /proteger-cuenta-meta, /campana-whatsapp, /reporte-meta-semanal, /plan-ecommerce-meta, /plan-saas-meta, /plan-marca-meta, /plan-infoproducto-meta.

**Conectores:** Meta oficial (beta; puede no estar habilitado en tu cuenta) y Pipeboard (tercero: tus datos pasan por ellos). Empieza en SOLO LECTURA.
**Hook:** toda herramienta que cree, active, cambie presupuesto, pause o borre pide confirmación.

**Límites:** gran parte de las cifras vienen de blogs de proveedores y están etiquetadas [no verificado]; no hay benchmarks medidos de Perú; no hay casos públicos verificables de SaaS B2B a gran escala; varias páginas oficiales de Meta no se pudieron leer. Los ejemplos numéricos son ilustrativos. Nada evade políticas de Meta. No probado instalado.
