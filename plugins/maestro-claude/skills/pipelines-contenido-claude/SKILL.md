---
name: pipelines-contenido-claude
description: Monta pipelines de contenido con Claude - sitios web, presentaciones HTML, vídeo corto, guiones y anuncios - con referencias, extracción de marca, assets generados y revisión anti-relleno. Úsalo para producir entregables repetibles. Triggers - sitio web, landing, deck, presentación, vídeo, YouTube, anuncios, AI slop, Firecrawl, Higgsfield.
---

# Pipelines de contenido

## Objetivo
Pasar de "pídele algo a la IA" a un proceso repetible: investigar, referenciar, generar, revisar y publicar, con calidad consistente y costos controlados.

## Pasos
1. Sustancia antes que estilo: define público, acción deseada, objeciones y tono. Para webs, investiga primero a los mejores competidores del nicho y saca sitemap/estructura antes de diseñar.
2. Reúne referencias visuales (galerías de diseño, componentes, capturas): mostrar vale más que describir. Respeta derechos: úsalas como inspiración de estilo, no copies productos ni marcas ajenas.
3. Extrae la identidad de la marca propia o del cliente (tipografía, paleta, logo) con una herramienta de scraping y guarda un archivo de diseño reutilizable con tokens (colores, escala tipográfica, espaciado).
4. Activa skills de diseño revisados (ver auditoria-repos-seguridad) y genera 2-3 versiones; elige una y refina por iteraciones.
5. Assets: imágenes y vídeo por CLI/API de un generador. Pide primero un recibo de costos estimado, fija proporciones y calidad, y genera pocas variantes. Claves por variable de entorno.
6. Diseña también la versión móvil; una idea por pantalla. Comprueba contraste y legibilidad.
7. Texto: pasa el copy por una revisión anti-relleno (vocabulario genérico de IA, regla de tres, promesas vagas); sustituye por detalles concretos y verificables. No inventes cifras ni testimonios.
8. Vídeo/guion: analiza canales del nicho (estructura, gancho, duración), escribe el guion y reescríbelo en tu voz; no publiques contenido genérico generado sin criterio propio ni suplantes voces de terceros. Revisa las políticas de la plataforma.
9. Anuncios: estudia bibliotecas públicas de anuncios para detectar patrones (gancho, ritmo, estructura, llamada a la acción) y crea piezas originales con tu producto; no clones creatividades ajenas ni hagas afirmaciones de resultados sin prueba.
10. Publica por CLI (GitHub + hosting) previa confirmación explícita, y entrega un panel de edición limitado si el cliente necesita cambiar textos, para no re-gastar tokens.
11. Convierte el pipeline ganador en skill (crear-skill-desde-flujo).

## Prompts de ejemplo
- "Investiga 5 sitios líderes del nicho [X] y responde: ¿para quién es?, ¿qué acción debe hacer?, ¿qué objeciones tiene?, ¿qué tono?, ¿qué activos de marca? Termina con un sitemap propuesto. No diseñes aún."
- "Usa estas 3 capturas como referencia de estilo y construye 2 versiones del hero. Antes de generar vídeo o imágenes dame el costo estimado y espera mi confirmación."
- "Revisa este texto buscando frases genéricas y promesas sin prueba; reescribe con detalles concretos que yo pueda verificar."

## Errores comunes
- Pedir "hazme una web" sin referencias ni estructura.
- Generar muchos assets sin controlar costo.
- Publicar texto de IA sin revisión ni verificación de datos.
- Copiar diseños o anuncios ajenos.
- Ignorar el diseño móvil.

## Checklist de cierre
- Público, acción y objeciones definidos.
- Costo de assets aprobado antes de generar.
- Texto verificado y sin cifras inventadas.
- Versión móvil revisada y publicación confirmada.

## Vigencia
- Modelos de imagen/vídeo, herramientas y precios cambian cada mes; las cifras de ingresos, conversión o coste por pieza del creador: no verificado.
- Reglas de plataformas (monetización, anuncios, IA) y licencias de repos de diseño: confirma las vigentes.
