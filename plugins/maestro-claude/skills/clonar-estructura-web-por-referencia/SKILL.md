---
name: clonar-estructura-web-por-referencia
description: Usar al replicar la estructura, ritmo y principios de conversión de un sitio de referencia, o generar variantes por negocio, sin copiar su contenido ni marca. Gatillos - "clonar web", "copiar estilo de", "replicar layout", "HTML de referencia", "design DNA", "variantes por cliente".
---

# Clonar estructura por referencia (sin copia literal)

## Objetivo
Extraer el "ADN" de un sitio admirado (estructura, espaciado, jerarquía, animación) y reconstruirlo con tu marca, copy e imágenes propios. El resultado debe ser original: la referencia es guía de layout, no código de producción.

## Pasos
1. **Elige UNA referencia** y guarda capturas (hero, secciones, móvil). Comprueba que puedas usarla solo como inspiración.
2. **Obtén la estructura.** Descarga el HTML renderizado (guardar página / view-source / un extractor) y colócalo en una carpeta temporal `reference/`, con las capturas.
3. **Extrae el ADN, no el contenido.** Pide a Claude un `design-brief.md`: tipografías y pesos, line-height, escala de espaciado, paleta, orden de secciones, patrón de animación. Nada de textos, logos ni imágenes del original.
4. **Reconstruye con lo tuyo.** Aplica tu marca (tokens de color, tipografía, logo), tu copy y tus imágenes. Pide "úsalo solo como guía de layout; no es código de producción".
5. **Revisa la divergencia.** Pide una lista de qué es propio y qué sigue demasiado parecido; cambia lo literal.
6. **Limpia.** Borra `reference/` al terminar.
7. **Variantes por negocio.** Descompón la web en 5-6 elementos que cambian (identidad, reseñas, contacto, zona, precios, FAQ, paleta), pásalos a un `site-config` y genera cada variante cambiando solo la configuración, con placeholders donde falten datos. Guarda el proceso como skill una vez validado.
8. Mide la calidad con `ui-ux` y SEO de `seo-multipagina-auditoria`.

## Prompts de ejemplo
- "Lee la carpeta reference/ y escribe design-brief.md con tipografía, escala de espaciado, estructura de secciones y estilo de animación. No copies textos ni imágenes."
- "Recrea la home con mi marca (tokens en brand.md) y este copy. Mantén solo el ritmo y la jerarquía; dime qué partes siguen siendo demasiado parecidas al original."
- "Descompón este sitio en elementos intercambiables y refactoriza a site-config.ts; luego genera una variante para [negocio] con placeholders."

## Errores comunes
- Pegar HTML ajeno directamente en producción (riesgo legal y de calidad).
- Dar 20 instrucciones o varias referencias a la vez: la IA no cumple ninguna.
- Dejar la carpeta de referencia en el repo público.
- Clonar la marca de un tercero: usa su sitio solo como inspiración, nunca su identidad.

## Vigencia
Los extractores de HTML y sus límites cambian. Las cifras de venta mencionadas por el creador: no verificado. Verifica derechos y términos del sitio de referencia.

## Checklist de salida
- [ ] `design-brief.md` sin textos, logos ni imágenes del original.
- [ ] Marca, copy e imágenes propios en el resultado.
- [ ] Lista de partes aún demasiado parecidas revisada y corregida.
- [ ] Carpeta `reference/` borrada y fuera del repo.
- [ ] Derechos y términos de la referencia considerados.
- [ ] Si hay variantes, `site-config` validado con placeholders marcados.
