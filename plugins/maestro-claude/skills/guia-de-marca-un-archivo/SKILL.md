---
name: guia-de-marca-un-archivo
description: Genera una guía de marca estable en un solo archivo (paleta, tipografía, logo, voz, reglas) para adjuntar en cada proyecto con Claude. Usar con "guía de marca", "brand guidelines", "brand book", "identidad", "logo", "voz de marca" o "importar marca".
---

# Guía de marca en un archivo

## Objetivo
Darle a Claude una identidad portable y verificable, estructurada como las guías de marcas admiradas pero única, que se adjunta a cualquier proyecto para mantener coherencia.

## Pasos
1. Reúne ejemplos de guías de marca que te gusten (guías públicas de marcas conocidas) y de logos o decks desde galerías de referencia; anota qué estructura te sirve.
2. Define esencia: propuesta, público, tono, 3 adjetivos de personalidad y 3 cosas que la marca nunca hace.
3. Pide a Claude una estructura de guía inspirada en la que elegiste, pero con contenido propio: logo y zonas de respeto, paleta con roles, tipografías, iconografía, imágenes, voz y ejemplos de copy, usos correctos e incorrectos.
4. Logo: pide 6-9 opciones con un generador conectado, a partir de varios logos de referencia; selecciona una y pide versiones (claro/oscuro, monocromo, ícono).
5. Tipografía: elige fuentes con licencia comercial confirmada; si partes de una captura, pide la alternativa libre más cercana.
6. Paleta: parte de paletas existentes, fija roles y proporción 60-30-10, comprueba contraste.
7. Si usas un editor con marcas (importar desde URL logo/colores/tipografía), úsalo como atajo y compara con tu archivo.
8. Escribe la guía en un único archivo (Markdown + tokens CSS/JSON) y añade ejemplos de aplicación (post, slide, email).
9. Pruébala: pide 3 piezas distintas usando solo la guía; ajusta reglas ambiguas.
10. Adjúntala al crear proyectos o conviértela en design system (ver design-system-desde-referencias). Guarda copia fuera de la herramienta.

## Prompts de ejemplo
- "Me gusta cómo está organizada la guía de marca de [marca conocida]. Propón una estructura equivalente para mi proyecto, con contenido original, y entrégala como un solo archivo Markdown más un bloque de tokens CSS."
- "Con esta guía, crea un post cuadrado, una slide y un encabezado de email. Señala cualquier regla que haya sido ambigua."
- "Dame 9 opciones de logo para [marca] inspiradas en estas referencias, sin copiar ninguna, con justificación de cada una."

## Errores comunes
- Copiar la identidad de otra marca en vez de inspirarse en su estructura.
- Guía sin ejemplos negativos ("qué no hacer").
- Paleta sin roles ni contraste verificado.
- Fuentes sin revisar licencia comercial.
- Tener la guía solo dentro de una plataforma.

## Vigencia
Las herramientas de importación de marca y los generadores de logo cambian de funciones y planes (precios no verificados). La estructura de la guía es estable; el flujo de importación no.

## Criterios de salida
- Un solo archivo con paleta, tipos, logo, voz, usos correctos e incorrectos.
- Tres piezas de prueba creadas solo con la guía.
- Licencias de fuentes y assets anotadas.
- Copia guardada fuera de la plataforma de diseño.
