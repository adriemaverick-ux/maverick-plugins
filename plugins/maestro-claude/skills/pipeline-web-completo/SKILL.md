---
name: pipeline-web-completo
description: Usar al crear o rehacer una landing o web desde cero, de la estrategia a la publicación (moodboard, diseño, build, refinado, deploy). Gatillos - "crear una web", "landing page", "build a website", "pipeline web", "rediseñar sitio".
---

# Pipeline web completo

## Objetivo
Llevar una web de la idea a producción con calidad visual y de conversión, repartiendo bien el trabajo: un primer borrador visual rápido (AI Studio, Stitch, Lovable o el propio Claude Code) y el refinado profesional en local con Claude Code.

## Pasos
1. **Estrategia.** Define el tipo de tráfico (frío: valor y diagnóstico; cálido: valor y compromiso; outbound: confianza). Responde: los 3 mayores problemas del visitante, qué ya cree, qué dudas tiene, por qué hizo clic. Si dudas, trata el tráfico como frío.
2. **Plan antes de construir.** Abre Claude Code en modo plan (Shift+Tab) y pídele que cuestione tu idea y devuelva un SOP corto con funciones, secciones y objetivo de conversión. Aprueba solo cuando lo entiendas.
3. **Moodboard.** Reúne 3-5 capturas (Dribbble, Mobbin, Godly, Behance) y etiquétalas ("hero como la 3", "testimonios como la 5"). Para marca existente, extrae colores, tipografías y logo (Firecrawl en formato branding o la guía de marca en markdown).
4. **Primer borrador (80%).** Prompt en tres partes: qué es el negocio, estilo (animación, profundidad, tipografía, UNA sola referencia) y estructura (hook, propuesta de valor, 2-3 detalles, prueba, CTA). Genera 3-4 versiones y quédate con la mejor; si se desvía, empieza en blanco en vez de pedir reconstruir.
5. **Llevarlo a local.** Descarga el zip o clona el repo, abre la carpeta, instala dependencias y corre en localhost. Los builders online suelen dejar dependencias sin instalar y dan pantalla en blanco al publicar directo.
6. **Refinado.** Claude Code: copy, estructura, accesibilidad, responsive y una pasada de auditoría con checklist de cambios. Carpeta `design-inspo/` para referencias; bórrala al final si contiene HTML ajeno.
7. **Componentes puntuales ("UI sniping").** Toma un componente de 21st.dev, Magic UI o CodePen, pide colocarlo en un lugar concreto y adáptalo a tu marca. Uno por vez.
8. **Publicar.** Sigue la skill `publicar-github-vercel`; luego `seo-multipagina-auditoria` y `qa-seguridad-e2e`.

## Prompts de ejemplo
- "Modo plan. Lee este proyecto y propón mejoras de copy y diseño para convertir visitas en reservas. Hazme las preguntas de aclaración que necesites antes de tocar nada."
- "Diseña una landing para [negocio] dirigida a [avatar]. Estilo: [referencia única], fondo oscuro, micro-interacciones sutiles, tipografía fuerte. Estructura: hook, propuesta de valor, 3 puntos, prueba social, CTA con formulario. Usa las capturas adjuntas solo para el estilo."
- "Ábrela en localhost, revísala en móvil y dime qué falla antes de seguir."

## Errores comunes
- Sobre-especificar colores en el primer prompt o mezclar varias referencias de estilo.
- Meter todo el análisis de competencia en el builder visual: más información suele dar peor diseño.
- Un solo mensaje y una sola acción por sección; si todo es protagonista, nada lo es.
- Publicar sin probar móvil ni el formulario con un dato real.
- Pegar claves en el código: usa variables de entorno.

## Vigencia
Los nombres de builders, menús y límites gratuitos (AI Studio, Stitch, Lovable) cambian cada pocas semanas; verifica la herramienta vigente. Las cifras de ventas de webs citadas por el creador original: no verificado. El método (estrategia, plan, referencia única, local, auditoría) es estable.

## Checklist de salida
- [ ] Objetivo de conversión y tipo de tráfico escritos en CLAUDE.md.
- [ ] Una sola referencia de estilo usada y documentada.
- [ ] Build local sin errores y revisión móvil hecha.
- [ ] Formulario probado con un dato real de prueba.
- [ ] Sin claves en el repo; `.env.example` sin valores.
- [ ] Carpetas temporales de referencia eliminadas.
