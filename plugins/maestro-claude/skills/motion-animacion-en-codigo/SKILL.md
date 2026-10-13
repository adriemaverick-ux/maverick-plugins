---
name: motion-animacion-en-codigo
description: Crea motion graphics, loops, animaciones de producto y video programático en código (HTML/CSS/JS, Remotion) con marca real. Usar con "animación", "motion", "loop", "Remotion", "subtítulos animados", "hero animado", "reel", "logo animado" o "micro-interacciones".
---

# Motion y animación en código

## Objetivo
Producir animación con propósito, reproducible y fiel a la marca, evitando el aspecto genérico: cada elemento en movimiento tiene una función y los loops cierran limpio.

## Pasos
1. Define la pieza: idea única, duración (3-20 s), formato (cuadrado, vertical, horizontal) y destino (web, reel, slide).
2. Trae la marca real: extrae colores, logo y tipografía de la URL con una herramienta de scraping de identidad; no dejes que el modelo navegue a ciegas.
3. Si hay datos, investígalos primero con una fuente real; si no, saldrán cifras inventadas.
4. Referencia visual: un clip o captura "gold standard" y una frase de qué imitar (ritmo, easing, composición).
5. Pide 3 variantes de estilo y elige; no te quedes con la primera pasada.
6. Loops: una función de render por sección; el último fotograma debe ser idéntico al primero.
7. Micro-interacciones web: hover con elevación, presión suave, contadores, transiciones; tiempos cortos y consistentes con el design system. Un solo estilo de iconos; Lottie solo con licencia revisada.
8. Video programático (Remotion): carpeta de entrada, transcripción con timestamps por palabra, corte de errores y repeticiones, limpieza de audio, subtítulos con fuente de marca y jerarquía clara; renderiza a una carpeta de salida.
9. Para clips sobre un video largo: transcribe a HTML con tiempos, detecta momentos donde una animación aporta, genera los clips y entrégalos o insértalos.
10. Reutiliza: cuando una animación guste, pide "codifícala como estilo/skill reutilizable" y, tras un proceso repetible, pide también un SOP.
11. Exporta en varios aspect ratios y comprime. Prueba en móvil y con "reducir movimiento" activado.

## Prompts de ejemplo
- "Haz un loop de 10 s para [producto] con estos colores y esta fuente. El último frame debe coincidir con el primero. Dame 3 variantes de estilo para elegir."
- "Transcribe este video con tiempo por palabra, propón 6 momentos donde una animación aporte y explica por qué; luego crea el clip del primero con la marca adjunta."
- "Anima el logo en 3 s con la identidad de [URL]. Un movimiento principal, sin efectos decorativos, y exporta en cuadrado y vertical."

## Errores comunes
- Animar sin propósito; efectos que distraen.
- Loops con salto visible.
- Datos de gráficos inventados.
- Subtítulos con tamaño o jerarquía pobres (el detalle tipográfico es el error principal).
- Ignorar peso del archivo y accesibilidad de movimiento.
- Usar assets (Lottie, fuentes) sin revisar licencia.

## Vigencia
Remotion, los menús de Animation en Claude Design y las herramientas de scraping cambian rápido; el consumo de tokens y créditos de generación varía y no está verificado. Verifica versión de cada herramienta.

## Criterios de salida
- Loops sin salto, probados en los formatos requeridos.
- Archivo comprimido y versión de movimiento reducido considerada.
- Datos y marca verificados contra la fuente.
- Estilo o proceso guardado como skill o SOP si se va a repetir.
