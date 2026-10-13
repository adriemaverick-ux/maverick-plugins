---
name: anti-ai-slop-tipografia-copy-color
description: Elimina el aspecto y el texto "de IA" en un diseño: tipografía por defecto, degradado índigo, tres tarjetas, copy genérico, iconos mezclados. Usar cuando digas "anti-slop", "AI slop", "suena a IA", "se ve genérico", "revisa fuentes/copy/color" o antes de entregar cualquier diseño.
---

# Anti AI slop: tipografía, copy y color

## Objetivo
Detectar y corregir las señales de slop (tipografía, imágenes, jerarquía, color, espaciado y copy) con cambios concretos y verificables.

## Pasos
1. Inventario de señales: fuente por defecto, degradado índigo-violeta, tres tarjetas iguales, mismo redondeo y glass en todo, titulares genéricos, placeholders con cifras inventadas, imágenes de stock sin relación.
2. Tipografía (la palanca más barata): fija una fuente explícita. Extráela de una marca admirada (scrape de identidad con una herramienta de extracción de marca) o pega una captura y pide la fuente libre más cercana. Fuentes libres: Google Fonts, Fontshare, Open Foundry; inspiración: Typewolf, fontsinuse. Máximo 2 familias.
3. Revisa licencias de fuentes, iconos y animaciones (uso personal vs comercial) y anótalas.
4. Color: define roles y proporción 60-30-10 (base, secundario, acento). Parte de paletas reales, no de un degradado por defecto. Verifica contraste del texto.
5. Iconos: un solo estilo por pieza o presentación; pack coherente en lugar de mezclar.
6. Copy: sustituye frases vacías por hechos concretos y dolor nombrado primero. Quita superlativos ("líder", "innovador"), pares "no solo X sino Y", listas de tres por reflejo y pilas de guiones largos. Una pantalla = una idea = una petición.
7. Segunda pasada de copy con otro modelo o con una lista propia de palabras prohibidas; compara con el copy de 5 competidores fuertes del nicho.
8. Reemplaza todos los placeholders por datos reales o márcalos como pendientes visibles.
9. Entrega tabla antes/después con la razón de cada cambio.

## Prompts de ejemplo
- "Audita esta página y lista cada señal de slop por categoría (tipo, imagen, jerarquía, color, espaciado, copy) con una corrección concreta y su ubicación."
- "Reescribe el copy de la sección héroe: nombra el dolor del cliente en la primera línea, evita superlativos y relleno, máximo 7 palabras en el titular. Dame antes/después y por qué."
- "La fuente actual es la de por defecto. Propón tres alternativas libres cercanas a [captura], con licencia comercial confirmada, y aplícalas a la escala tipográfica."

## Errores comunes
- Cambiar color pero dejar la fuente por defecto.
- Mezclar estilos de iconos o tres familias tipográficas.
- Copy "pulido" pero abstracto; lo concreto convence más ("5 minutos en el tren" vs "ahorra tiempo").
- Ignorar licencias.
- Dejar cifras o testimonios de relleno en producción.

## Vigencia
Los patrones de slop evolucionan con los modelos; revisa la lista cada pocos meses. Catálogos de fuentes y packs de iconos cambian precios y licencias (no verificado aquí).

## Criterios de salida
- Fuente explícita y licencia confirmada; máximo dos familias.
- Un solo estilo de iconos y paleta con roles y contraste verificado.
- Tabla antes/después del copy entregada, sin placeholders.
- Ninguna señal de slop sin resolver en la lista de inventario.
