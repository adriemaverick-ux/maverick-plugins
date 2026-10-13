---
name: design-system-desde-referencias
description: Crea un design system propio a partir de referencias reales (galerías, URLs, capturas, proyecto previo) en vez de un prompt vacío. Usar cuando digas "design system", "sistema de diseño", "moodboard", "referencias", "que no se vea genérico", "brand assets" o antes de cualquier web, deck o app.
---

# Design system desde referencias

## Objetivo
Dar a Claude un sistema (tokens, componentes, assets, reglas) construido desde buen diseño real, para que todo lo que produzca después sea coherente y no genérico. Principio: "dale un sistema, no un prompt".

## Pasos
1. Define el negocio en 3 líneas: qué vende, a quién, qué sensación debe producir y qué quieres evitar.
2. Reúne referencias por tipo, no una sola: galerías de sitios y apps (Mobbin, referral.design, Godly, Awwwards, Land-book, Pinterest), una "gold standard" de tu nicho y 1-2 de fuera del nicho. Guarda 3-5 capturas y las URLs.
3. Pide a Claude 3 referencias cercanas a tu nicho desde una galería, elige una (opcional una segunda) y di qué imitar de cada una: tipografía, espaciado, jerarquía, motion.
4. Genera assets propios antes del sistema: logo, mascota/personajes, texturas, imágenes héroe (generador de imágenes conectado, p. ej. por CLI/MCP). Es el paso que más se salta y el que más diferencia.
5. En Claude Design: Design systems > Create. Sube logos, fuentes, assets, capturas, notas de estilo y, si existe, repo de código. Si ya tienes un proyecto bueno, expórtalo (Share > project HTML / archive) y úsalo como base.
6. Revisa elemento por elemento (colores, tipos, iconos, botones, gradientes). Aprueba o corrige con ejemplos de "me gusta / no me gusta". Itera 5-10 vueltas.
7. Si no hay sistema propio o dudas de la calidad, trabaja sin sistema: uno malo es peor que ninguno.
8. Exporta el sistema (zip/HTML) y guárdalo fuera de la herramienta: así lo usas en Claude Code, otros modelos o Open Design.
9. Reutilízalo: al crear piezas nuevas, selecciónalo o adjunta el archivo exportado y pide "usa este design system".

## Prompts de ejemplo
- "Aquí tienes 4 capturas y 2 URLs de sitios que admiro para una tienda de café de especialidad. Antes de diseñar, escribe qué rasgos concretos tomarías de cada uno (tipo, grilla, radios, color) y cuáles descartarías."
- "Crea un design system para [marca]: paleta con roles (fondo, texto, acento, estados), escala tipográfica, espaciado en múltiplos de 8, radios, sombras, 6 componentes base y reglas de uso. Mantén todo en un solo archivo de tokens."
- "Usa el design system adjunto para una landing de 5 secciones. No inventes colores ni fuentes fuera del sistema; si falta algo, dime qué añadir."

## Errores comunes
- Pedir diseño sin referencias: sale el resultado de todos (degradado índigo, tres tarjetas).
- Copiar una sola referencia en lugar de combinar varias.
- Subir un sistema a medio pensar y heredarlo en todo.
- No exportar el sistema y quedar atado a un solo entorno.
- Adjuntar archivos muy pesados (en Claude Design hay un tope de tamaño; comprime).

## Vigencia
Los menús de Claude Design (Share, project archive, Design systems), el tope de archivos y las galerías citadas cambian con frecuencia; verifica en la UI actual. Las capacidades de modelos y los límites de uso dependen del plan y de la fecha.

## Criterios de salida
- Existe un archivo de tokens y un zip/HTML del sistema guardado fuera de la herramienta.
- Cada color, fuente e icono tiene rol y licencia anotados.
- Una pieza de prueba usa solo el sistema y no necesita excepciones.
- Quedan registradas las referencias usadas y qué se tomó de cada una.
