---
name: perfiles-iniciales
description: Úsala como router para elegir el perfil de voz correcto antes de escribir - Maverick Sistemas, Casa Soyer o Adrie en cámara (provisional). Gatillos - "qué perfil uso", "perfil Maverick", "perfil Casa Soyer", "voz de Adrie", "which style profile".
---

# Router de perfiles iniciales

## Objetivo
Escoger rápido el perfil adecuado, saber qué tan firme es y qué falta calibrar. Los tres perfiles de arranque están en `../../references/perfiles-iniciales.md`, derivados solo de las reglas de la bóveda y de los informes, sin muestras reales.

## Pasos
1. Identificar quién habla y a quién:
   - Mensaje, caption, propuesta o ficha de Maverick Sistemas para dueños de talleres, saneamiento o mantenimiento técnico: perfil Maverick.
   - WhatsApp consultivo, ficha de producto, anuncio o guion de Casa Soyer para compradores de mueble y decoración de diseño: perfil Casa Soyer.
   - Video donde sale Adrie hablando a cámara: perfil Adrie en cámara (PROVISIONAL).
   - Mezcla (por ejemplo video de Maverick con Adrie): combinar Adrie en cámara para el modo de hablar y Maverick para contenido y límites.
2. Cargar primero la versión calibrada desde la bóveda (`Perfiles de estilo`). Si existe, manda sobre el perfil inicial. Si no, usar el inicial y avisar en una línea que es provisional.
3. Aplicar con `estilo-aplicar-perfil`; el léxico sale de `idioma-del-icp-glosario`.
4. Si el perfil es provisional, pedir a Adrie 3 a 5 muestras reales (audios transcritos de video, WhatsApp enviados, guiones) y recorrer `estilo-extraer-perfil-de-voz`.
5. Evaluar con `estilo-evaluar-fidelidad` cuando haya muestras.
6. Guardar la versión calibrada en la bóveda, no en el plugin.

## Tabla de decisión
| Situación | Perfil | Firmeza |
|---|---|---|
| Outreach, propuesta, bio de Maverick | Maverick | Media: sale de reglas escritas de la bóveda |
| Respuesta a consulta de mueble | Casa Soyer | Baja: tuteo y tono vienen de inferencia |
| Guion hablado de Adrie | Adrie en cámara | Provisional: sin muestras |

## Errores comunes
- Tratar el perfil provisional como definitivo y fijarlo en piezas públicas sin revisión.
- Mezclar tuteo de Casa Soyer con el usted de Maverick en un mismo mensaje.
- Escribir como Adrie sin sus muestras e inventarle muletillas.
- Guardar el perfil calibrado dentro del plugin.
- Poner el nombre de un cliente real como ejemplo sin permiso.

## Nivel de evidencia
- Perfil Maverick: reglas de bóveda [observado en fuente: bóveda local] más inferencias del informe 05 [inferido].
- Perfil Casa Soyer: registro y frases [inferido]; no se leyeron materiales de la tienda.
- Perfil Adrie: [no verificado] hasta recibir muestras.

## Fuente
Bóveda: 00 - Inicio, Marca Maverick y contenido; informe 05, secciones 4 y 5; informe 01, sección 3.3 (plantilla).

## Vigencia
2026-10-12
