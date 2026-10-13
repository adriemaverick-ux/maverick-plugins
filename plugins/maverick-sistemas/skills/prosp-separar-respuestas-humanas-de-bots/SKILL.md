---
name: prosp-separar-respuestas-humanas-de-bots
description: Úsalo al revisar respuestas recibidas de talleres para distinguir personas de bots, mensajes de bienvenida y menús, y decidir qué cuenta como Respondió. Gatillos: "respondió un taller", "es un bot", "respuesta automática", "clasificar respuestas", "human vs bot reply".
---

# Separar respuestas humanas de bots

## Objetivo
Evitar inflar el pipeline con saludos automáticos. Solo una respuesta humana relevante cuenta como **Respondió**; lo demás se registra aparte y alimenta aprendizaje, no oportunidades.

## Pasos
1. Leer la respuesta y clasificarla en una de estas clases: **Humana relevante**, **Humana no relevante** (ocupado, número equivocado), **Respuesta automática** (bienvenida, horario, menú de cotización), **Opt-out**, **Sin respuesta**.
2. Señales de bot: saludo genérico idéntico, menú numerado, pide datos del vehículo, responde al instante sin tocar lo que se preguntó, repite el menú tras una aclaración.
3. Si el bot contesta como si fuera un cliente, responder una sola vez con transparencia y pedir derivación; no inventar datos de un vehículo ni seguir el menú. Si no hay derivación posible, parar ese hilo.
4. Si es humana relevante: guardar la respuesta textual breve, el problema que menciona, el siguiente paso y la fecha. No copiar conversaciones completas ni datos sensibles.
5. Mover a **Respondió** solo si hay una persona y se identificó un asunto. Una respuesta automática nunca crea oportunidad calificada.
6. Si hay opt-out, registrar "No contactar" y no volver a escribir.
7. Usar los menús detectados como señal de mercado: ese taller ya automatiza la recepción. Siguiente pregunta útil: derivación a una persona, seguimiento y estado de cada consulta; no ofrecerle una automatización básica como novedad.
8. Cuando hay duda de si es persona o bot, dejarlo como "por confirmar" y preguntar una vez; no contarlo como Respondió.
9. Reportar el conteo por clase al cerrar la tanda: contactos, automáticas, humanas relevantes, opt-outs.

## Plantillas
Registro de respuesta:
```
Negocio / Fecha / Clase (humana relevante | automática | opt-out | otra)
Texto breve (literal, sin datos personales):
Problema mencionado:
Siguiente paso y fecha:
Etapa sugerida: Respondió | (sin etapa)
```

Respuesta a bot (una vez):
> Gracias. No busco un servicio para mi vehículo. Intento contactar a quien ve la atención de consultas del taller. ¿Podrían derivar mi mensaje o indicarme un canal empresarial para esa persona?

## Errores comunes
- Contar un "¡Hola, bienvenido!" como interés.
- Seguir el flujo del bot y terminar generando una cotización falsa.
- Insistir con varios mensajes a un hilo automático.
- Confundir "me interesa" con aceptación de propuesta.
- Optimizar por "visto" o por respuesta automática en vez de problema confirmado.

## Nivel de evidencia
- Varios talleres enviaron menús automáticos de cotización: [observado en el vault, 2026-10-10]; prueba que algunos automatizan la recepción, no que funcione bien o mal.
- Regla "automática no es Respondió": [decisión de Adrie].
- Proporción de bots frente a humanos en Lima: [no verificado].

## Fuente
Pipeline comercial (servicios recurrentes), outbound a talleres (2026-10-09), decisiones consolidadas (2026-10-10).

## Vigencia
2026-10-11.
