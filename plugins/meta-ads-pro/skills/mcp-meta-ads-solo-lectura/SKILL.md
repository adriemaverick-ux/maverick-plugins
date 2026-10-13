---
name: mcp-meta-ads-solo-lectura
description: Úsala para elegir y conectar un MCP o CLI de Meta Ads con Claude (oficial, Pipeboard, Adspirer, Porter, claude-ads), con riesgos, y cómo empezar de forma segura en solo lectura. Gatillos - "conectar Meta Ads a Claude", "MCP de Meta", "Pipeboard", "Adspirer", "Porter", "solo lectura", "connect Meta Ads MCP".
---

# MCP de Meta Ads en solo lectura

## Objetivo
Conectar Claude a la cuenta publicitaria empezando solo con lectura; toda escritura bajo aprobación humana explícita, con registro.

## Pasos
1. Probar primero el MCP oficial `https://mcp.facebook.com/ads` (open beta desde 2026-04-29, OAuth, gratis en beta) [oficial]. Si devuelve `is_ads_mcp_enabled:false`, el acceso es gradual y no hay apelación [vendor].
2. Alternativa: CLI oficial `meta-ads` (Python >= 3.12) con token de system user de mínimo privilegio; sirve para scripts [oficial]. La versión npm/endpoint `mcp.meta.com` contradice la doc [no verificado].
3. Si solo necesitas reportes: Porter o Pipeboard en modo lectura, o exportar CSV (14+ días) a un skill sin dar acceso.
4. Configurar solo permisos de lectura (`ads_read`) cuando sea posible. Las reglas del servidor MCP (2026-07-16) permiten limitar presupuestos y catálogos [oficial, detalle no documentado].
5. Primera sesión: pedir que liste cuentas y confirme cuenta, moneda y zona horaria. Verificar 3-5 cifras en Ads Manager.
6. Escribir solo bajo aprobación: crear en pausa, activar manualmente (`ads_activate_entity` es lo que gasta dinero), tope de cambio de presupuesto de ±15-20%, bitácora [comunidad].
7. Revisar el SKILL.md y la licencia de cualquier skill de GitHub antes de darle tokens.

## Plantillas / prompts listos
Comparativa resumida:
- Oficial Meta: ~29 herramientas, lee y escribe, crea en pausa, gratis en beta; acceso gradual [oficial/vendor].
- Pipeboard: 28-42 herramientas (no concilian), BSL 1.1, token en URL como riesgo [vendor/comunidad].
- Adspirer: 36-60 herramientas según la página, planes desde US$49 con cuotas bajas de llamadas [vendor].
- Porter: orientado a lectura y reportes, tier gratis (páginas inconsistentes) [vendor].
- claude-ads (AgriciDaniel): plugin, solo lectura por defecto, MIT [comunidad]. mikusnuz: 135 herramientas, alto riesgo [comunidad].
- Prompt inicial: "Modo solo lectura. No crees, edites ni actives nada. Lista cuentas, confirma moneda y zona horaria, e indica qué herramientas de escritura tienes disponibles para que las deshabilite."

## Errores comunes
1. Dar token con permisos de escritura amplios en la primera prueba.
2. Usar servidores con 100+ herramientas sin necesidad.
3. Dejar el agente con escritura corriendo sin supervisión.
4. Pegar el token como `?token=` en URL; se filtra en logs.
5. Asumir que "oficial" = sin riesgo: los rechazos de política y el ritmo de llamadas siguen contando.

## Nivel de evidencia
- [oficial] Servidor MCP, CLI, permisos, creación en pausa.
- [vendor] Estado de acceso gradual (~10% de cuentas a inicios de mayo), conteos de herramientas y precios.
- [comunidad] Repos y sus estrellas.
- [no verificado] Pricing posterior a la beta; reglas del servidor; política contra MCP de terceros (no existe una publicada).

## Checklist de arranque seguro
- [ ] Acceso al MCP oficial probado en la cuenta propia.
- [ ] Permisos de lectura únicamente en la primera semana.
- [ ] Token en variable de entorno, nunca en URL ni en git.
- [ ] Herramientas de escritura y de audiencias deshabilitadas.
- [ ] Bitácora de cambios lista antes de habilitar cualquier escritura.

## Vigencia
2026-10-11. La beta cambia rápido; reconfirmar acceso y herramientas.
