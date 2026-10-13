---
name: prosp-mensaje-inicial-y-tono
description: Úsalo para redactar el primer mensaje a un taller o empresa de servicios técnicos y las respuestas siguientes, en tono breve y sin exclamaciones. Gatillos: "redacta el mensaje inicial", "primer mensaje", "tono del outreach", "draft first message", "cold message to workshop".
---

# Mensaje inicial y tono

## Objetivo
Redactar mensajes que no parezcan spam ni consulta de un cliente: breves, específicos, sin signos de exclamación, con una sola pregunta de diagnóstico. Esta skill solo redacta; nunca envía. Todo envío lo hace Adrie a mano, tras revisar.

## Pasos
1. Partir de un prospecto que pasó `prosp-filtro-de-prospectos` y de un ángulo asignado (ver lista abajo).
2. Presentarse con nombre real y decir por qué se escribe al negocio.
3. Aclarar desde el inicio que no es cliente ni busca cotizar una reparación (evita que contesten con el menú de cotización del bot).
4. Decidir el formato: (a) apertura que pide permiso para hacer una pregunta, o (b) una sola pregunta de diagnóstico. No mezclar las dos en el mismo mensaje.
5. Una sola pregunta, sobre el proceso actual, nunca sobre la solución. Sin lista de Maps, web, CRM ni IA.
6. Sin exclamaciones, sin mayúsculas de énfasis, sin emojis de venta, sin adjuntos ni enlaces en el primer mensaje.
7. Si hay respuesta humana, seguir la conversación una pregunta por turno; ofrecer demo o propuesta solo si el decisor lo pide o confirma un problema.
8. Si dice que no, o no responde, no insistir ni encadenar mensajes. Registrar opt-out.
9. Revisar contra `prosp-cumplimiento-peru-consentimiento` antes de entregar la tanda a Adrie.

## Plantillas
Ángulos a probar, una variable a la vez (sin ganador aún): equipo ocupado; fuera de horario; datos para cotizar; origen de clientes (Google/Maps); seguimiento de cotizaciones; próxima visita o mantenimiento.

Apertura con permiso:
> Hola, [nombre o equipo]. Soy Adrie. No busco un servicio para mi vehículo: estoy conversando con talleres de Lima sobre cómo atienden las consultas nuevas. ¿Les puedo hacer una pregunta breve?

Pregunta de diagnóstico (solo si aceptan), una por ángulo:
> Cuando el equipo está trabajando en vehículos, ¿quién responde las consultas nuevas que llegan?
> ¿Qué suelen hacer con las consultas que llegan después del cierre?
> Cuando envían una cotización y el cliente no confirma, ¿cómo hacen el seguimiento hoy?

Si contesta el bot como si fuera cliente (una sola vez):
> Gracias. No busco un servicio para mi vehículo. Intento contactar a quien ve la atención de consultas del taller. ¿Podrían derivar mi mensaje o indicarme un canal empresarial para esa persona?

## Errores comunes
- Abrir enumerando soluciones ("Maps, web, CRM e IA"): pone la solución antes del problema.
- Seguir el menú del bot o inventar datos de un vehículo.
- Dos preguntas en un mensaje, o pedir reunión sin contexto.
- Prometer cifras sin línea base o afirmar que la IA reemplaza al asesor.
- Citar o mostrar datos, nombres o capturas de un cliente sin su autorización.
- Reutilizar mensajes del archivo de diseño y obra: allí se leyeron como consulta de cliente de obra.

## Nivel de evidencia
- Tono (breve, sin exclamaciones, aclarar que no es cliente, pedir permiso, una pregunta): [decisión de Adrie, 2026-10-10].
- Pedir interés antes que reunión: [oficial/estudio de Gong sobre correo frío, no WhatsApp ni talleres peruanos]; solo principio transferible.
- Qué texto convierte mejor en Lima: [no verificado]; medir con conversaciones propias.

## Fuente
Notas de outbound a talleres (2026-10-09) y decisiones consolidadas (2026-10-10). Los textos son redacción nueva alineada con esas reglas.

## Vigencia
2026-10-11.
