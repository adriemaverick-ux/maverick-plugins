# maverick-sistemas v1.4

Plugin para Maverick Sistemas (sistemas para empresas de mantenimiento y servicios técnicos recurrentes). Fuente de verdad: tu bóveda `~/Downloads/Maverick MP` (`00 - Inicio.md`).

**59 skills · 10 subagentes · 17 comandos**
- Marca, casos y registro (7) · Contenido en cámara, canales y producción (11) · Prospección, CRM y nichos (11) · Diagnóstico, propuestas, piloto y entrega (14) · Automatización de redes y SEO (12).
- Canales: YouTube, Instagram, Facebook, Threads y web. Ficha de Google Maps propia: probablemente no elegible (software remoto); SEO local y ficha son servicio para clientes.

**Comandos:** /revisar-pieza, /registrar-en-boveda, /guion-video, /plan-semanal-contenido, /reporte-semanal-contenido, /preparar-tanda, /registrar-respuesta, /revisar-pipeline, /diagnostico-cliente, /propuesta-piloto, /plan-de-entrega, /disenar-flujo-dm, /auditar-ficha-google, /plan-automatizacion-redes, /overlay-hyperframes, /analizar-reel, /recurso-y-palabra-clave.

**Conector:** GHL (MCP oficial, requiere autorizar en tu cuenta; URL tomada de un informe, no probada).
**Hooks:** confirmación antes de enviar, publicar o cambiar datos; aviso si intentas escribir un token en un archivo.

**Decisiones del dueño aplicadas:** las leyes peruanas de mensajería no bloquean (solo nota corta); SÍ se respetan las reglas de Meta/WhatsApp. Cadencia de contenido por defecto: la de la bóveda (4 Reels, 1 carrusel, 1 video largo); la alternativa de 3 videos en cámara reutilizados está como propuesta.

**Límites:** casi todo lo de Jack Roberts es [no verificado]; precios de ManyChat sin confirmar; no hay datos de talleres peruanos; los agentes redactan, nunca envían. No probado instalado.

**Seguridad pendiente tuya:** la nota `GHL - Integracion privada.md` de la bóveda guarda un token y un Location ID en texto plano. Muévelos a un gestor de secretos y rota el token.

**Novedades v1.4:** `contenido-hooks-operativo` (hooks para tu nicho) y `produccion-overlays-hyperframes-claude-motion` (flujo decidido el 2026-10-12: Claude Motion explora, HyperFrames produce overlays con el CLI local, CapCut monta). Escribir en tu voz: instala también `copy-y-estilo`.

**Novedades v1.4:** `analisis-reels-con-gemini` (Gemini ve los Reels y los describe en fichas; Claude extrae estilo de edición, hooks, ritmo, overlays y sonido). Incluye prompt, plantilla de síntesis y un script de la API (no probado).

**Novedades v1.4:** `conversion-palabra-clave-y-recurso` (cierre de cada video con palabra clave en comentarios y recurso gratuito por mensaje directo; decisión del 2026-10-12, basada en el estudio de 20 Reels). Comando `/recurso-y-palabra-clave`.

**Novedades v1.4:** referencias cruzadas al estudio de Reels en `contenido-hooks-operativo` y evidencia de overlays parciales en `produccion-overlays-hyperframes-claude-motion`.
