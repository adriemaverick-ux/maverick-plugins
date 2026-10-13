---
name: extraer-adn-diseno
description: Extrae el "ADN de diseño" de un sitio, póster o pieza que admiras (tipografía, espaciado, color, estructura) y lo convierte en reglas y tokens reutilizables, sin copiarlo. Usar con "design DNA", "extraer estilo", "replicar este diseño", "comparar con referencia", "brecha de diseño" o "convertir en skill".
---

# Extraer ADN de diseño

## Objetivo
Pasar de "me gusta cómo se ve" a reglas medidas que Claude pueda aplicar a otro contenido, y verificar con tests que las reglas bastan para reconstruir el original.

## Pasos
1. Elige la pieza (URL o captura) y su alcance: web completa, una sección, póster o clip.
2. Extrae medidas, no descripciones: familias y pesos tipográficos, tamaños y line-height en px, escala de espaciado, radios, sombras, paleta con proporciones, ancho de contenedor, grilla, tiempos y curvas de animación. Con una URL, usa un extractor de marca (identidad, colores, tipografía) para no depender de navegación manual.
3. Anota lo que la pieza NO hace: lo que rechaza (sin bordes, sin degradados, sin iconos decorativos) y las "rarezas" deliberadas.
4. Documenta layouts con nombre (hero, bento, footer) y sus proporciones.
5. Escribe las reglas en un archivo: builder brief (texto), tokens (JSON/CSS) y un scaffold HTML mínimo.
6. Escribe tests que una mala copia fallaría (ej. "el titular nunca supera 7 palabras", "el acento ocupa menos del 10 %").
7. Reconstruye el original usando solo las reglas; compara lado a lado. Cada diferencia es una regla olvidada: añádela y repite.
8. Comparación de brechas: con tu web y la referencia, pide un informe HTML breve con valores lado a lado y las 3 correcciones de mayor impacto; aplícalas.
9. Empaqueta como skill que, al invocarse, pregunte sujeto, contenido y variantes de color.

## Prompts de ejemplo
- "Analiza esta URL y extrae su arquitectura de diseño en un archivo: tipografías con pesos, tamaños y line-height en px, escala de espaciado, paleta con proporciones y estructura de secciones. No copies texto ni imágenes."
- "Compara mi página con esta referencia con criterio estricto. Entrega un informe HTML corto con tabla de valores lado a lado (espaciado, radios, elevación, jerarquía) y prioriza tres arreglos."
- "Con estas reglas, reconstruye la pieza original desde cero y marca qué diferencias visuales aparecen; cada diferencia debe convertirse en una regla nueva."

## Errores comunes
- Describir en lugar de medir.
- Replicar contenido o marca ajena: extrae estructura y principios, no copies assets ni textos protegidos.
- No definir tests; las reglas parecen completas pero fallan en la reconstrucción.
- Usar una sola referencia para todo.
- Hacer el análisis con una captura de baja resolución.

## Vigencia
Los extractores de marca y sus formatos de salida cambian; confirma qué devuelve la herramienta que uses. Las reglas de proporción (60-30-10, razón áurea) son heurísticas, no leyes.

## Criterios de salida
- Archivo de reglas, tokens y scaffold generados.
- Los tests de reglas se pasan y la reconstrucción coincide con el original dentro de lo razonable.
- Informe de brechas con las 3 correcciones prioritarias, si hubo comparación.
- No se copiaron textos ni assets de terceros.
