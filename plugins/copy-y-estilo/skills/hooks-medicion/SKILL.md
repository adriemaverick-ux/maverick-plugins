---
name: hooks-medicion
description: Cómo medir si un gancho funciona - hook rate, hold rate, ThruPlay, retención de YouTube, clics en email y conversaciones calificadas por WhatsApp. Usar al revisar resultados de un video o anuncio o al comparar dos ganchos. Gatillos - "hook rate", "hold rate", "retención", "cómo mido el gancho", "thumbstop".
---

# Medición de ganchos

## Objetivo
Saber qué gancho funciona sin engañarse con una métrica de vanidad. Para cuentas pequeñas de servicios o de ticket alto, la métrica final es la cantidad de conversaciones calificadas por WhatsApp; el hook rate solo dice si la apertura detiene el pulgar.

## Pasos
1. Define la pregunta: ¿detiene (hook rate), mantiene (hold rate) o convierte (conversación calificada)?
2. Saca los datos del mismo periodo y de la misma ubicación. No compares un Reel con una historia.
3. Calcula a mano lo que Meta no da con ese nombre (ver tabla).
4. Compara contra tu propio historial; los benchmarks de abajo son solo orientación.
5. Cambia UNA cosa por prueba (el gancho, no gancho y oferta a la vez).
6. Decide con volumen suficiente y mira conversaciones calificadas antes de declarar ganador.

## Métricas
| Métrica | Cómo se calcula | Origen |
|---|---|---|
| Reproducción de 3 s | Veces que el video se ve al menos 3 s (o casi completo si es más corto); repeticiones no suman | Meta [oficial, leído vía buscador] |
| Hook rate (thumbstop) | Reproducciones de 3 s ÷ impresiones × 100 | Convención [vendor]; algunos dividen por alcance y no son comparables |
| Hold rate | Habitual: ThruPlays (o reproducciones de 15 s) ÷ reproducciones de 3 s × 100 | Sin definición oficial de Meta [vendor]; varía por fuente |
| ThruPlay | Video visto completo o al menos 15 s | Meta [oficial] |
| YouTube | % que sigue a los ~30 s de intro; CTR de título y miniatura | YouTube Studio [oficial] |
| Email | Clics y respuestas mejor que aperturas (Apple MPP las infla) | [vendor] |
| Negocio | Leads, conversaciones calificadas, ventas | [un experto] Kane |

## Benchmarks de referencia (todos [vendor], no estándar de Meta)
- Hook rate: 15-35 % (Kickbite); 25-30 % medio y 30-40 % bueno (Vaizle vía Segwise); base 30-40 % y bajo 25 % (Motion).
- Hold rate: medio 40-50 %, fuerte más de 60 %, flojo bajo 30 % (Motion).
Úsalos para ubicarte, no para juzgarte.

## Plantilla de registro
`Pieza: [x] | Gancho: [texto] | Tipo: [curiosidad/escena/...] | Hook rate: [ ] | Hold rate: [ ] | Conversaciones calificadas: [ ] | Decisión: [seguir/cambiar gancho/cortar]`

## Errores comunes
- Celebrar vistas o seguidores sin mirar conversaciones calificadas.
- Mezclar fórmulas (impresiones vs alcance) entre piezas.
- Cambiar gancho y oferta a la vez.
- Concluir con pocas impresiones.
- Citar "el hook rate normal es X" como si fuera regla de Meta.

## Nivel de evidencia
- Reproducción de 3 s y ThruPlay: [oficial] Meta.
- Fórmula del hook rate, hold rate y todos los rangos: [vendor]; la definición de hold rate no es oficial.
- Medir por negocio y no por vistas: [un experto] (Kane, NAR abr-2026).
- Cifras sueltas virales (por ejemplo, "40.000 a 780.000 vistas al cortar 3 segundos"): [no verificado]; no usar.

## Fuente
Informe 04, sección 6 (Motion, Kickbite, Segwise, Meta Business Help, YouTube Help), 2026-10-12.

## Vigencia
2026-10-12
