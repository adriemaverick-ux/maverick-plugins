---
name: info-embudo-segun-precio
description: Elige el embudo de un infoproducto (venta directa, tripwire, webinar, challenge, VSL, aplicación+llamada, lanzamiento) según precio y margen. Usar cuando se pregunte "qué embudo uso", "webinar o llamada", "funnel for my course", "tripwire vs VSL".
---

# Embudo según precio del infoproducto

## Objetivo
Elegir el embudo más simple que alcance el margen, y el evento de optimización que le corresponde. Los umbrales de precio son una heurística [cálculo propio / un experto], no un estándar de industria.

## Pasos
1. Calcula el margen neto por venta y el CPA máximo (ver skill `info-economia`). Sin eso no se elige embudo.
2. Compara el CPA que Meta da hoy en tráfico frío con el CPA máximo. Si es mayor, hace falta subir el valor por cliente (bump/OTO, webinar, llamada) o bajar el CAC (audiencia caliente).
3. Elige según la tabla:

| Embudo | Precio típico (heurística) | Evento a optimizar | Cuándo |
|---|---|---|---|
| Venta directa (landing/VSL corta a checkout) | hasta ~USD 50 | Compra | Producto simple, resultado fácil de explicar, audiencia fría amplia |
| Tripwire / bump / OTO | producto USD 7-47 | Compra (valor del carrito) | Cubrir el CAC subiendo el ticket medio |
| Lead magnet + email/WhatsApp | producto USD 30-300 vendido después | Lead | Construir lista propia; requiere nutrición |
| Webinar / masterclass | USD 100-1,500 | Registro; con volumen, Asistió | Ticket medio donde hay que enseñar y generar confianza |
| Challenge 5 días | USD 100-1,000 | Registro | La audiencia necesita probar el método; alta carga operativa |
| VSL | USD 47-500 | Compra o Lead | Mensaje claro, prueba social, tráfico templado |
| Aplicación + llamada | USD 1,000+ | Lead de aplicación; idealmente llamada agendada/calificado | Mentorías y cohortes de alto ticket |
| Lanzamiento / cohorte | USD 200-3,000+ | Registro y luego Compra | Solo con audiencia y prueba social acumuladas |

4. Para precios sobre ~USD 500 no mandes tráfico frío directo a la página de venta; se cita como "el error más común" [un experto: benly.ai 2026].
5. Empieza con el embudo más simple. Añade un paso solo si mide mejor que el anterior.
6. Mide el costo por etapa en la primera semana (registro, asistencia, aplicación, venta) y compáralo con tu CPA máximo.

## Plantillas / prompts
- "Con precio <PRECIO>, margen neto <MARGEN>, audiencia caliente <TAMAÑO LISTA> y CPA frío observado <CPA>, recomienda un embudo y el evento de optimización; indica qué dato falta."
- Registro de etapas: `etapa | costo por etapa | tasa a la siguiente | decisión`.

## Errores comunes
- Vender un producto caro a tráfico frío en un solo paso.
- Elegir webinar por moda sin capacidad de pitch ni de seguimiento.
- Optimizar por registro barato sin medir asistencia ni compra.
- Presentar rangos de blogs como metas: úsalos solo como sanity check.

## Nivel de evidencia
- Mapa precio-embudo: [cálculo propio / un experto].
- Rangos de referencia (CPL de registro de webinar, show-up 20-50%, cierre de llamadas 15-30%): [benchmark] de blogs de proveedores, muy amplios, no específicos de Perú.
- No hay benchmark primario de show-rate de llamadas en high-ticket [no verificado].
- Costo por registrante de challenge: sin benchmarks públicos fiables.

## Vigencia
2026-10-11. Releer antes de lanzar; todo gasto requiere aprobación humana.
