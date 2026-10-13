---
name: estilo-extraer-perfil-de-voz
description: Úsala cuando haya que sacar el perfil de voz de una persona o marca a partir de 3 a 5 muestras reales (mensajes, guiones, audios transcritos). Gatillos - "extraer perfil de voz", "cómo escribe", "mi estilo", "extract voice profile", "style guide from samples".
---

# Extraer un perfil de voz desde muestras reales

## Objetivo
Convertir 3 a 5 textos reales en un perfil con rasgos medibles y reglas observables, no una lista de adjetivos ("cercano, profesional"). El perfil alimenta a `estilo-aplicar-perfil`.

## Pasos
1. Reunir 3 a 5 muestras del mismo género que se quiere producir (WhatsApp enviados, guion hablado, post). Separar por canal: el WhatsApp no suena como la propuesta. Si el género es informal, pedir más muestras informales.
2. Anonimizar: quitar nombres de clientes, teléfonos y datos personales antes de procesar.
3. Medir con la plantilla de abajo, a mano o con ayuda de Claude. Con pocas muestras los números son orientativos: decirlo en el perfil.
4. Comparar con un texto genérico de IA sobre el mismo tema. Lo que cambia es la voz.
5. Escribir reglas observables. Mal: "cercano". Bien: "una pregunta directa en las tres primeras líneas; oraciones de hasta 22 palabras".
6. Elegir 3 a 5 ejemplos dorados variados y 2 o 3 contraejemplos (suena a la persona pero no es).
7. Guardar el perfil en la bóveda de Obsidian, carpeta `Perfiles de estilo` (ruta: `Maverick MP/Perfiles de estilo/`), un archivo por perfil, con versión y fecha. No guardar perfiles dentro del plugin: el plugin trae solo las plantillas y los perfiles iniciales provisionales.
8. Registrar el cambio en la bitácora de la bóveda según la regla del dueño.

## Plantilla de medición (completar por muestra)
- Oración: palabras promedio, máxima y porcentaje de oraciones de menos de 10 palabras.
- Párrafo: oraciones por párrafo; líneas máximas en pantalla.
- Persona y tratamiento: yo, nosotros, tú o usted; cuándo cambia.
- Puntuación: uso de dos puntos, paréntesis, rayas, exclamaciones, puntos suspensivos.
- Preguntas: cuántas por cada 100 palabras; directas o retóricas.
- Humor: tipo (seco, autoironía, ninguno) y frecuencia.
- Léxico: 20 a 30 palabras que usa siempre; 20 a 30 que nunca usa; tecnicismos que mantiene o traduce.
- Entrada y salida: cómo abre (dato, pregunta, escena) y cómo cierra (paso siguiente, pregunta).
- Formato: viñetas, negritas, emojis y su posición.
- Localismos: cuáles usa y con qué frecuencia [no verificado: confirmar cada uno en el diccionario].

## Perfil de salida (esqueleto)
```
PERFIL DE ESTILO - [nombre] - v1.0 - [fecha] - n muestras = __
1. Público y propósito
2. Voz: 3 a 5 rasgos, cada uno con regla observable
3. Tono por situación (frío, cotización, seguimiento, video)
4. Rasgos medibles (tabla de arriba)
5. Léxico: decimos / traducimos / nunca decimos
6. Ejemplos dorados y contraejemplos
7. Límites (afirmaciones que requieren respaldo)
8. Mantenimiento: próxima revisión, cómo sumar muestras
```
La plantilla completa está en `../../references/perfiles-iniciales.md`.

## Errores comunes
- Describir con adjetivos en lugar de medir.
- Usar una sola muestra o muestras de canales distintos mezcladas.
- Perfilar la voz de un tercero famoso con sus textos protegidos: ver `etica-de-imitar-estilos`.
- No decir cuántas muestras sustentan el perfil.
- Guardar el perfil dentro del plugin y que se pierda en una actualización.

## Nivel de evidencia
- Medir rasgos y exigir ejemplos junto al perfil: [consenso] en el uso de ejes de tono y ejemplos; las plantillas concretas son práctica de agencias [un experto].
- Burrows' Delta usa las 100 a 150 palabras más frecuentes [consenso académico]; no hace falta calcularla para un perfil de marca.
- Mínimo de 3 a 5 muestras: criterio práctico [mi criterio]; el informe sugiere 8 a 20 para un perfil robusto.

## Fuente
Informe 01 (Copy Research), secciones 3.1 a 3.3; regla de bóveda: registro en Obsidian.

## Vigencia
2026-10-12
