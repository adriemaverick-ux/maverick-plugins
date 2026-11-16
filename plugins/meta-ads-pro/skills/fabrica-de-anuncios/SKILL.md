---
name: fabrica-de-anuncios
description: 'Cómo pasar de un guion a varios anuncios listos para Meta con el sistema de edición de Maverick (HyperFrames + ffmpeg, formato definitivo de pantalla dividida) - un video por hook, versiones 9:16 y 4:5, zonas seguras de anuncios, final para anuncio, nombres y parámetros de URL. Usar al producir anuncios, o con "fábrica de anuncios", "versiones del anuncio", "exportar para ads", "zona segura", "4:5".'
---

# Fábrica de anuncios

## Objetivo
De **un concepto grabado** salen **3 anuncios** (uno por hook), en dos formatos, listos para subir, medibles y distintos de los demás conceptos activos.

## Entrada
- Guion con la plantilla de 9 bloques y 3 hooks (lluvia de hooks; el hook nombra al rubro en el primer segundo).
- Grabación: los **3 hooks seguidos** al inicio, el cuerpo una sola vez y **dos finales**: orgánico («Comenta X») y anuncio («Toca el botón y te la mando por WhatsApp» o «Entra y calcula gratis»).
- Herramientas: `~/video-editor-maverick/reel-kallaway/formato-split-graficos/` (LEEME.md, `borrador7.py`) y HyperFrames.

## Pasos
1. **Editar una vez el cuerpo** con el formato definitivo: pantalla dividida con gráficos blanco y naranja, subtítulos sin signos, zooms y whooshes.
2. **Armar 3 versiones** cambiando solo los primeros 2 a 4 s (hook dicho + hook escrito). El resto es idéntico, así se compara el hook.
3. **Final de anuncio:** se cambia el final orgánico por el final de anuncio. Sin «Comenta X».
4. **Zonas seguras de Reels para anuncios** [oficial: facebook.com/business/ads-guide/update/video/instagram-reels]:
   - Dejar libre el **14 % de arriba (~269 px)**, el **35 % de abajo (~672 px)** y el **6 % de cada lado (~65 px)** en 1080×1920.
   - Ojo: en el formato orgánico los gráficos van entre y 990 y 1720. En el anuncio, lo de **abajo de y ≈ 1248** puede quedar debajo del botón y del texto. Subir los elementos clave de los gráficos o revisarlo en la vista previa de Ads Manager.
   - Hay una fuente que habla de una zona segura única para Reels e Historias desde mar-2026 (20–35 % abajo) [no verificado].
5. **Formatos:**
   - **9:16** para Reels e Historias.
   - **4:5** (1080×1350) para el feed [experto: Loomer, 2025]. Se recorta el centro; en pantalla dividida, revisar que no se pierda la cara ni el gráfico.
   - Resolución recomendada para 9:16: 1440×2560 o, como mínimo, 1080×1920.
6. **Sin música con licencia** en los anuncios: Meta lo recomienda y los posts con música con licencia no se pueden usar como anuncio [oficial]. Usar música libre o solo la voz con efectos.
7. **Nombres:** `concepto_hookA|B|C_9x16|4x5_v1` (por ejemplo `desglose_hookB_9x16_v1`). El tablero agrupa por concepto y por hook.
8. **Parámetros de URL** (anuncios a web): `utm_source={{site_source_name}}&utm_campaign={{campaign.name}}&utm_content={{ad.id}}&utm_term={{placement}}&h=<angulo>` (ver `pagina-por-anuncio`).
9. **Mensaje ya escrito** (anuncios a WhatsApp): repite el gancho, por ejemplo «Quiero la demo de la web para mi empresa de fumigación».
10. **Al subir:** apagar las mejoras automáticas de Advantage+ que deforman el video del fundador: música, retoques visuales o recorte, efectos y mejoras de texto. Revisar después de publicar, porque Meta puede encender algunas solo [experto: Loomer].
11. **Entrega:** carpeta `videos-listos/ads/<concepto>/` con los 6 archivos (3 hooks × 2 formatos) y un `.txt` con el texto principal, el título, la URL con parámetros o el mensaje de WhatsApp.

## Diversidad (lo que pide Meta)
Cada concepto nuevo cambia el **ángulo, el motor narrativo o el formato**, no solo el hook. Si dos conceptos se parecen mucho, Meta los trata casi como uno [declaración de Meta: «diversificar»; lo del Entity ID no está confirmado].

## Cómo sacar conceptos distintos [un experto: Adrián Sáenz y Roger Viladrosa, tutorial de jul-2024; bóveda `04 - Conocimiento/02 - Hallazgos/Meta Ads - aprendizajes del tutorial de Adrián Sáenz (2024-07)`]
- **Las primeras 24–48 h educan a Meta:** según quién reaccione primero, Meta arma el «avatar» al que le muestra el anuncio. El gancho tiene que **filtrar al dueño de la empresa** y espantar al curioso (por ejemplo, a quien tiene cucarachas en su casa), porque si no, Meta busca más curiosos.
- **Mapa de mensajes por nivel de conciencia:** muy frío (el problema, sin nombrar el producto) → frío (la solución directa) → templado (dudas y objeciones) → caliente («escríbeme», objeciones de plata y tiempo). Para empezar, apuntar al dueño que **ya sabe que existen soluciones**.
- **Tres ángulos:** entrar en una conversación que el dueño ya tiene, abrirle una que no se planteó, o responder sus objeciones.
- **El mismo ángulo en positivo y en negativo** cuenta como dos conceptos (el sueño frente a la pesadilla).
- **Cambiar el primer 50 % del video** (gancho y planteo) ya le llega a gente distinta; así se sacan varios conceptos de una sola grabación.
- **Un dolor, un tipo de comprador y un CTA por anuncio.** Se vende solo el siguiente paso: el mensaje de WhatsApp o usar la calculadora.
- **Plantilla:** «Te gustaría [deseo] pero [obstáculo] → es normal si estás en [situación] → lo que necesitas es [solución] → logras [deseo] sin [dolor] → cómo te sentirías → CTA».
- **Mostrar la solución en uso** (la calculadora calculando, la web recibiendo una consulta), no describirla.
- Persona mirando a cámara, ocupando buena parte del encuadre, siempre con subtítulos.
- Lo que **no** sirve de ese tutorial (es de 2024): intereses, exclusiones, públicos de 1–2 M y retargeting en varios niveles.

## Errores comunes
- Gráficos o texto clave tapados por el botón del anuncio.
- Subir el video orgánico con «Comenta X» como anuncio.
- 4:5 que corta la cara o el gráfico.
- Dejar activadas las mejoras automáticas y que Meta le ponga música o recorte la cara.

## Vigencia
2026-11-13.

## Relacionados y aprobación humana
`testeo-creativo-y-fatiga`, `anatomia-anuncio-ganador`, `marca-creativos-founder-led`, `ciclo-semanal-claude-meta`, `pagina-por-anuncio`; formato definitivo en la bóveda (`03 - Go-to-market/Formato definitivo - gráficos en pantalla dividida - 2026-11-12`). Publicar o subir anuncios solo con la aprobación de Adrie.
