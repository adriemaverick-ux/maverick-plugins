---
name: lego-system-videos-modulares
description: Sistema de videos modulares para anuncios ("Lego System") - grabar de una vez varios ganchos, muchos cuerpos (una pieza de la oferta cada uno) y pocos CTA, cortarlos con Claude Code y combinarlos en anuncios de ~30 s, adaptado a Maverick (formato definitivo, un dolor por anuncio, sin IA). Usar al planear una grabación para anuncios o con "Lego System", "videos modulares", "ganchos y cuerpos", "combinar clips", "muchos anuncios de una grabación".
---

# Lego System: videos modulares para anuncios

Fuente: curso «Meta Ads con Claude» de Benjamín Cordero (oct-2026) [experto, cuenta de US$2.500–3.000/día]. Bóveda: `04 - Conocimiento/02 - Hallazgos/Meta Ads con Claude - aprendizajes del curso de Benjamín Cordero (2026-10)`.

## Idea
Una sola grabación larga se corta en piezas y se combina en muchos anuncios. Cordero graba **10 ganchos + ~50 cuerpos + un par de CTA**; de una grabación saca 55 piezas y arma 5 anuncios por tanda (**1 gancho + 2–3 cuerpos + 1 CTA**, unos 30 s). Dice que con estos anuncios tuvo su costo por compra más bajo.

## Adaptación a Maverick
1. **Una grabación por oferta**, nunca la web y el kit juntos.
2. **Guion previo** (Claude lo escribe, Adrie lo lee de corrido):
   - **3–5 ganchos** que llaman al dueño de la empresa de fumigación o control de plagas (ver `b2b-duenos-mundo-hispano`).
   - **10–15 cuerpos**, cada uno con **una sola cosa** real de la oferta.
     - **Web:** botón de WhatsApp, zonas que atiende, certificados, fotos de trabajos, formulario de cotización, carga rápida.
     - **Kit:** costo por servicio, precio mínimo, contratos mensuales, cómo subir precios.
     - Nunca funciones que no existen.
   - **1 CTA** por oferta: WhatsApp para la web y la calculadora para el kit.
3. **Marca de corte:** decir **«Listo»** y pausar 2 s entre piezas.
4. **Corte con Claude Code:**
   1. Transcribir (whisperx).
   2. Ubicar «Listo» y cortar con ffmpeg.
   3. Nombrar `gancho_01`, `cuerpo_07_whatsapp`, `cta_01`.
   4. Quitar las pausas.
5. **Edición con el formato definitivo:** cada cuerpo lleva su gráfico blanco y naranja (HyperFrames) en pantalla dividida y subtítulos sin signos pegados al gancho (ver `fabrica-de-anuncios` y la bóveda).
6. **Combinar:** 1 gancho + 2–3 cuerpos **del mismo dolor** + el CTA. Así se respeta «un dolor por anuncio»; Cordero mezcla al azar, nosotros no.
7. **Volumen con US$10–35 al día:** **5 combinaciones por semana**, no 5 por día.
8. **Nombres:** `oferta_gancho01_c07-c03_cta01_9x16`.

## Imágenes fijas (sin IA)
Cordero gasta buena parte en imágenes porque se hacen rápido. Los formatos que mejor le fueron:
- «elige tu plan»;
- diagrama de un dato;
- tier list;
- captura de mensajes;
- «la semana en…»;
- carrusel de testimonios.

Él las hace con IA (Higgsfield); **Maverick no usa IA ni stock**: se hacen en **HTML con pantallas reales** (la web en el celular, la calculadora con un resultado, un chat de WhatsApp de ejemplo marcado como ilustrativo). Van en un **conjunto propio** dentro del laboratorio.

## Subida
- El conector de Meta Ads **puede no dejar subir video** en algunas cuentas. Cordero usó un token de usuario del sistema (`ads_read` + `ads_management`).
  - Ese token lo genera **Adrie** y se guarda en variables de entorno.
  - Claude no lo pide por el chat ni lo pega en archivos.
- **Todo se sube en pausa** y se activa **solo con el OK de Adrie**.
- **Rechazo conocido:** el enlace en un botón que Meta ya no acepta. Se arregla creando el creativo sin descripción y con el título en el campo del video.

## Errores comunes
- Mezclar cuerpos de dolores distintos en un mismo anuncio.
- Contar como «concepto nuevo» un anuncio que solo cambia un cuerpo: para Meta es una variación.
- Grabar cuerpos que prometen lo que la oferta no hace.

## Vigencia
2026-11-15.

## Relacionados
`fabrica-de-anuncios`, `testeo-creativo-y-fatiga`, `juez-diario-solo-lectura`, `ciclo-semanal-claude-meta`.
