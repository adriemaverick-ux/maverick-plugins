---
name: seo-web-de-servicios-para-clientes
description: Usar para planificar la web de un cliente de servicios locales (saneamiento, HVAC, equipos de cocina): páginas por servicio y por zona, datos estructurados LocalBusiness, velocidad y citas. Gatillos "páginas por servicio", "páginas por distrito", "datos estructurados", "LocalBusiness JSON-LD", "local landing pages", "doorway pages".
---

# Web de servicios para clientes

## Objetivo
Construir un sitio con una página real por servicio, páginas por zona solo cuando tengan valor propio, y datos estructurados correctos, evitando spam de doorway pages y contenido masivo generado con IA.

## Pasos
1. Mapear servicios principales y zonas de atención reales del cliente.
2. Crear una página dedicada por servicio (factor n.º 1 orgánico local según expertos). [analista]
   Contenido: qué incluye, para quién, cuánto tarda, cómo se agenda, preguntas frecuentes, fotos reales, certificaciones verificables (DIGESA, municipalidad según rubro), CTA a WhatsApp y llamada.
3. Páginas por zona (distrito) solo si hay contenido real y distinto: casos, tiempos de llegada, fotos, reseñas de esa zona. Empezar con 3-6. Doorway pages y keyword stuffing de ciudades son spam. [oficial]
4. Estructura: Home -> hub de servicios -> página por servicio -> (opcional) zonas -> casos/blog -> contacto con mapa, teléfono, WhatsApp, horarios y Libro de Reclamaciones virtual visible.
5. Datos estructurados JSON-LD con el subtipo más específico (AutoRepair, HVACBusiness, LocalBusiness). Obligatorios: name y address; recomendados: geo (5+ decimales), openingHoursSpecification, telephone con +51, url, priceRange. Debe coincidir con el contenido visible. [oficial]
6. No marcar con aggregateRating o review las reseñas propias del negocio: solo para sitios que recolectan reseñas de otros. [oficial]
7. Validar con Rich Results Test, enviar sitemap, revisar Search Console.
8. Rendimiento móvil: LCP <= 2,5 s, INP <= 200 ms, CLS <= 0,1; botones de llamar y WhatsApp visibles; imágenes optimizadas. [oficial]
9. NAP idéntico en web, ficha y directorios (Páginas Amarillas, Facebook, Yelp si aplica). No comprar enlaces. [analista/oficial]
10. IA: puede redactar borradores con datos reales del negocio, generar el JSON-LD y auditar; un humano revisa cada página antes de publicar.

## Plantillas/ejemplos
JSON-LD mínimo (sustituir con datos reales verificados del cliente):
```json
{
  "@context": "https://schema.org",
  "@type": "HVACBusiness",
  "name": "[Nombre real igual al rótulo]",
  "url": "https://[dominio]/",
  "telephone": "+51[número]",
  "address": {"@type": "PostalAddress", "streetAddress": "[calle y número]",
    "addressLocality": "[distrito]", "addressRegion": "Lima", "addressCountry": "PE"},
  "openingHoursSpecification": [{"@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:00", "closes": "18:00"}]
}
```
Esquema de página de servicio: H1 servicio + zona principal, resumen, qué incluye, proceso, tiempos, FAQ, fotos, CTA.

## Errores comunes
- 30 páginas de distritos con el mismo texto cambiando el nombre: doorway/scaled content abuse. [oficial]
- Generar cientos de páginas con IA sin valor propio.
- Datos estructurados que no coinciden con lo visible o con la ficha.
- Usar un enlace a Facebook o Instagram como sitio web de la ficha. [no verificado]
- Páginas sin teléfono, WhatsApp ni Libro de Reclamaciones.
- Medir solo con Search Console y olvidar GBP, WhatsApp y llamadas.

## Nivel de evidencia
- Políticas de spam, datos estructurados LocalBusiness, Core Web Vitals, SEO de video, funciones de IA: [oficial].
- Importancia de la página por servicio, relevancia geográfica y menciones para IA: [analista] (Whitespark 2026).
- Directorios útiles en Perú y disponibilidad de Apple Business Connect o Bing Places: [no verificado].

## Fuente
Informe 05_google_business_profile_y_seo_local.md (secciones 4, 10, 11E).

## Vigencia
2026-10-11.
