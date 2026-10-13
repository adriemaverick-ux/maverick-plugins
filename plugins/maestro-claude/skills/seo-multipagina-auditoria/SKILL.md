---
name: seo-multipagina-auditoria
description: Usar para añadir páginas internas, blog y SEO técnico a una web existente y auditarla (UI/UX, accesibilidad, SEO). Gatillos - "SEO", "multipágina", "blog", "sitemap", "JSON-LD", "auditoría SEO", "meta tags", "accessibility audit".
---

# SEO multipágina y auditoría

## Objetivo
Ampliar el sitio con páginas coherentes con el diseño y una base técnica de SEO sólida, y verificar con una auditoría priorizada (acciones rápidas vs inversiones).

## Pasos
1. **Inteligencia previa.** Analiza la web del cliente y 5 competidores (Firecrawl o similar): estructura de páginas, keywords, huecos de contenido. Anota patrones, no textos.
2. **Páginas nuevas.** Pide a Claude entender el lenguaje de diseño, preguntarte qué páginas crear (nosotros, testimonios, equipo, servicios, zonas), igualar el estilo y actualizar la navegación.
3. **Infraestructura SEO.** Plantilla de página consistente, `title` y meta descripción dinámicos, Open Graph, Twitter cards, canonical, JSON-LD (datos estructurados), `sitemap.xml`, `robots.txt`, un solo H1 por página, alt en imágenes, URLs limpias.
4. **Blog.** Plantilla de artículos con rutas dinámicas; usa un blog de referencia solo como guía de layout (carpeta temporal que luego se borra). Artículos con investigación de keywords, H1/meta únicos y enlaces internos. Se pueden paralelizar tareas independientes (keywords, borradores, metas) con subagentes.
5. **Auditoría.** Ejecuta una auditoría SEO (skill o comando propio) que revise home, internas, robots, sitemap y puntúe categorías; pide informe HTML con plan priorizado. Añade auditoría UI/UX y accesibilidad: contraste, foco de teclado, tamaño de áreas táctiles, tamaños de imagen, formularios.
6. **Aplica por prioridad** (alto impacto y bajo esfuerzo primero) y vuelve a auditar; pide checklist de lo cambiado.
7. **Medición.** Analytics y Speed Insights; Search Console tras publicar el sitemap.
8. Verifica en producción: /blog, sitemap y robots responden, sin 404.

## Prompts de ejemplo
- "Mira mi sitio, entiende su lenguaje de diseño y pregúntame qué páginas crear. Iguala el diseño, añade SEO completo (title, meta, OG, canonical, JSON-LD) y actualiza la navegación."
- "Audita SEO técnico y de contenido: home, internas, robots.txt y sitemap. Dame puntuación por categoría y un plan con quick wins y estratégicas."
- "Revisa accesibilidad y rendimiento: contraste, teclado, alt, tamaño de imágenes y Core Web Vitals; entrega checklist de cambios aplicados."

## Errores comunes
- Contenido duplicado o artículos genéricos escritos sin investigar keywords.
- Metas repetidas en todas las páginas; olvidar canonical.
- Prometer posicionamiento: los resultados de SEO no están garantizados (cifras de tráfico del creador: no verificado).
- Dejar la carpeta de diseño de referencia en el repo.

## Vigencia
Las reglas de Google y los nombres de métricas evolucionan; las skills de auditoría comunitarias cambian. Verifica con documentación vigente.

## Checklist de salida
- [ ] Un H1, title y meta únicos por página.
- [ ] Canonical, Open Graph y JSON-LD presentes.
- [ ] `sitemap.xml` y `robots.txt` responden en producción.
- [ ] Navegación y enlaces internos actualizados.
- [ ] Informe de auditoría con plan priorizado guardado.
- [ ] Segunda auditoría tras aplicar los quick wins.
