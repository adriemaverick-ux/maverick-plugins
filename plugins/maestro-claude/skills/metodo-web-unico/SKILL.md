---
name: metodo-web-unico
description: Método único y por defecto para crear cualquier web, landing o app con IA - Claude Design para diseñar, Claude Code para construir, Supabase solo si hace falta backend, GitHub y Vercel para publicar. Usar SIEMPRE que se pida crear, rehacer o mejorar una web, landing, tienda o app, antes de elegir herramientas. Gatillos - "crear web", "landing", "página web", "build a website", "rediseñar", "método web", "cómo hago esta web".
---

# Método web único

Una sola ruta, siempre la misma. Las otras skills del plugin son los detalles de cada paso; este es el orden y las reglas. No cambies de herramienta salvo que un paso no se pueda hacer con la indicada.

## Stack fijo
1. **Claude Design** → diseño y sistema de diseño.
2. **Claude Code** (app de escritorio, pestaña Code) → construcción.
3. **Supabase** → solo si la web necesita login, base de datos o leads.
4. **GitHub + Vercel** → guardar y publicar.
Opcionales (solo si el paso lo exige): **Firecrawl** para extraer marca/competencia; un generador de imagen/video para activos propios.
Fuera del método por defecto: Antigravity, Stitch, AI Studio, Lovable, Cursor. Úsalos solo si Adrie lo pide.

## Los 7 pasos
1. **Brief y plan** → skill `plan-mode-entrevista-previa` (+ `blast-sistemas-agenticos` si toca varios servicios). Claude te entrevista y devuelve un SOP corto. No se construye nada antes de aprobarlo.
2. **Estrategia y estructura** → skill `web-que-vende-por-secciones`: tipo de tráfico, 3 problemas del visitante, sitemap y wireframes. El texto sale de quejas reales (`copy-por-pain-points`).
3. **Referencias y diseño** → skills `design-system-desde-referencias` y `extraer-adn-diseno`: 3-5 referencias reales etiquetadas, una sola referencia de estilo por prompt, design system en Claude Design. Si el cliente tiene marca, extráela de su URL.
4. **Pulido con críticos** → skills `design-loop-criticos` y `anti-ai-slop-tipografia-copy-color`: checklist escrita antes, subagentes críticos, fuente explícita, sin degradado índigo ni tres tarjetas iguales.
5. **Handoff y construcción** → skill `handoff-claude-design-a-code`: exporta el zip, carpeta nueva y vacía, localhost, borrador al 80%, luego refinado. Hero animado o 3D solo si aporta: `web-3d-scroll-animado`, `motion-animacion-en-codigo`.
6. **Backend si hace falta** → `backend-supabase-login-leads`. Claves solo en variables de entorno (`gestion-claves-entorno`).
7. **QA, SEO y publicación** → `checklist-qa-visual`, `qa-seguridad-e2e`, `seo-multipagina-auditoria`, luego `publicar-github-vercel`. **Antes de publicar, desplegar o comprar dominio, pide un "sí" explícito.** Para clientes: `portal-cambios-clientes`.

## Reglas fijas
- Una referencia de estilo por prompt; nunca prompt en blanco.
- Primero el 80%, después refinar; no perfeccionar la primera pasada.
- Probar en móvil real antes de entregar.
- Nada de claves en el código. Nada publicado sin confirmación.
- No copiar sitios: solo estructura y principios (`clonar-estructura-web-por-referencia`).
- Si el cliente es Casa Soyer, el negocio es ecommerce en Shopify: no mezclar con otros sistemas.

## Cuándo desviarse
Solo si (a) Claude Design no está disponible en la cuenta, o (b) el paso pide algo que no existe en el stack. Anótalo en el SOP y vuelve al método en el paso siguiente.

## Vigencia
Basado en videos hasta 2026-10-10. Los productos cambian; revisa si Claude Design o el handoff a Code cambiaron antes de asumir los pasos.
