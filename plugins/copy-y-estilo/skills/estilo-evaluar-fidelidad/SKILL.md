---
name: estilo-evaluar-fidelidad
description: Úsala para medir si un texto suena a la persona o marca del perfil, con checklist y comparación ciega. Gatillos - "suena a mí", "evaluar estilo", "evaluate style fidelity", "blind comparison", "detector de IA".
---

# Evaluar la fidelidad de estilo

## Objetivo
Saber si una pieza cumple el perfil sin depender de detectores de IA, que no son fiables (dan falsos positivos y negativos).

## Pasos
1. Aplicar el checklist de 10 puntos (0 = no, 1 = parcial, 2 = sí; máximo 20).
2. Si hay dudas sobre el perfil entero, hacer la comparación ciega (abajo).
3. Decidir con el umbral: 16 a 20 publicar con edición menor; 12 a 15 reescribir con el bucle de `estilo-aplicar-perfil`; menos de 12, revisar perfil y ejemplos.
4. Anotar el resultado y los incumplimientos recurrentes en la nota del perfil (bóveda, `Perfiles de estilo`).

## Checklist
1. Longitud de oración dentro del rango del perfil.
2. Tratamiento (usted o tú) consistente y adecuado.
3. Apertura y cierre del tipo definido.
4. Usa 3 o más palabras del léxico del cliente; cero del léxico prohibido.
5. Tono correcto para la situación.
6. Respeta el máximo de localismos y de humor.
7. Cada afirmación fuerte tiene un dato verificable o lleva `[DATO PENDIENTE]`.
8. Sin marcadores de IA acumulados (ver `antiia-en-espanol`).
9. Un solo siguiente paso, claro.
10. La persona dice "esto lo pude escribir yo" (1 si hay que retocar más de una quinta parte).

## Comparación ciega
1. Generar tres versiones: A (texto real de la persona sobre un tema parecido), B (Claude con perfil y ejemplos), C (Claude sin perfil, control).
2. Unificar formato; quitar emojis, encabezados o marcas que delaten el origen.
3. Ordenar al azar para cada evaluador.
4. Mostrar a 3 o más personas, al menos una del público objetivo: "¿cuál suena más a [persona]?" y "¿cuál le da más confianza?".
5. Si B se confunde con A y supera a C, el perfil funciona. Registrar el resultado tal cual, sin redondear a favor.
6. Si el juez es un LLM: ejecutar ambos órdenes y contar solo si coincide; usar un juez de otra familia que el redactor; contrastarlo con un grupo humano pequeño.

## Errores comunes
- Usar un detector de IA como árbitro. No lo es: sirve, como mucho, de señal débil.
- Evaluar solo con quien escribió el perfil: sesgo de quien conoce la respuesta.
- Borrar marcadores de IA sin arreglar el fondo (vaguedad, falta de dato concreto).
- Medir con una sola pieza y sacar conclusiones generales.
- Contar la fidelidad de estilo como si fuera veracidad: un texto fiel puede traer una cifra inventada.

## Nivel de evidencia
- Los detectores producen falsos positivos y negativos; en el estudio arXiv 2509.14543 la imitación con ejemplos aún se marcaba como IA [consenso].
- Sesgo de posición en jueces LLM: en un estudio de 2026 las comparaciones por pares cambiaron de resultado cerca de 14 por ciento al repetirlas [un estudio; verificar cifra].
- Umbrales 16/12 sobre 20: [mi criterio], ajustar con datos propios.

## Fuente
Informe 01, secciones 5.1 a 5.3.

## Vigencia
2026-10-12
