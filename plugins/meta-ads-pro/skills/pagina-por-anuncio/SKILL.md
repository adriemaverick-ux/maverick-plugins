---
name: pagina-por-anuncio
description: 'Cómo hacer que la página de destino repita el gancho del anuncio (coherencia anuncio–página) de forma barata, con título dinámico por parámetro de URL y medición por anuncio con {{ad.id}}, y cuándo no vale la pena. Usar al crear landings para anuncios, o con "landing por anuncio", "message match", "página de destino", "parámetros de URL", "utm_content".'
---

# Página por anuncio (coherencia anuncio–página)

## Por qué
- Si la página cumple lo que prometió el anuncio, convierte más. Google lo mide como «experiencia en la página de destino» y pide un mensaje coherente y carga rápida [oficial: support.google.com/google-ads/answer/6167118].
- Caso con texto dinámico (Campaign Monitor + Unbounce): +31,4 % de conversión [proveedor, sin fecha]. La cifra de +212 % que circula no tiene fuente primaria [no verificado].
- Meta: en 2017 anunció que la velocidad de carga influye en la entrega [oficial vía prensa]. Hoy publica ejemplos de malas experiencias después del clic. No hay un puntaje oficial de calidad de página [no verificado].

## Cómo se hace barato
1. **Una sola página con título dinámico**, no muchas páginas. La URL lleva `?h=desglose` y la página cambia el título, la primera frase y la imagen según `h`. El resto queda igual.
2. **Parámetros de URL del anuncio** (campo «Parámetros de URL» en Meta):
   `utm_source={{site_source_name}}&utm_campaign={{campaign.name}}&utm_content={{ad.id}}&utm_term={{placement}}&h=<angulo>` [proveedor: terminusapp, 2026].
3. La página guarda `utm_content` (el `ad_id`) en el lead y en la metadata del checkout, para que el webhook de la pasarela lo devuelva y el `tablero-costo-por-venta` sepa qué anuncio vendió.
4. **Velocidad:** página estática en Vercel, imágenes livianas y nada de librerías pesadas. Debe cargar en menos de unos 2 s en un celular.
5. En la **calculadora:** el gancho del anuncio aparece arriba («¿Cuánto te deja de verdad un servicio de fumigación?») y los campos ya vienen con un ejemplo del rubro.

## Click-to-WhatsApp
No hay página. Lo que repite el gancho es el **mensaje ya escrito** del anuncio («Quiero ver la demo de la web para mi empresa de fumigación») y la **primera respuesta automática**.

## Cuándo no vale la pena
- Con US$10–35 al día, cada variante recibe muy pocos clics para notar diferencias. Como máximo, **2 o 3 variantes por ángulo**, no una por anuncio.
- Si la oferta no vende, ninguna página la salva.

## Errores comunes
- La página promete otra cosa que el anuncio, por ejemplo un anuncio de «contratos» que lleva a una página genérica.
- Olvidar `{{ad.id}}`: las ventas quedan sin anuncio.
- Popups, cookies o formularios largos antes de mostrar el valor.

## Vigencia
2026-11-13.

## Relacionados
`tablero-costo-por-venta`, `valor-por-lead-y-escalera`, `pixel-y-capi-setup`, `anatomia-anuncio-ganador`.
