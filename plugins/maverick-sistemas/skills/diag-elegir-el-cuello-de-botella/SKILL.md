---
name: diag-elegir-el-cuello-de-botella
description: Úsalo cuando ya hay entrevista y mapa del flujo y toca decidir cuál ÚNICO paso conviene resolver primero con un piloto, o si conviene no empezar. Gatillos - "elegir cuello de botella", "qué automatizar primero", "matriz valor dificultad", "pick one bottleneck", "priorizar el piloto".
---

# Elegir el cuello de botella

## Objetivo
Terminar con UNA frase que diga qué paso se resuelve, por qué ese y no otro, y qué número lo mostrará. Si el problema real no se resuelve con un sistema (por ejemplo, falta de mecánicos o técnicos), decirlo y no vender.

## Pasos
1. **Listar candidatos** desde el mapa: visibilidad (cómo los encuentran), atención de consultas, datos para cotizar, seguimiento de cotizaciones, agenda, próxima visita, visibilidad para el dueño.
2. **Descartar primero lo que no es de sistemas.** Un taller con capacidad llena no necesita más demanda; puede necesitar filtrar y ordenar solicitudes. Un negocio que ya tiene menú automático necesita saber qué pasa después (derivación, seguimiento, estado).
3. **Puntuar cada candidato con el dueño**, en pizarra o papel: valor para el negocio (1-10) y dificultad de implementación (1-10, considerando equipo, datos y canal). Anotar quién puso cada número.
4. **Aplicar el trío por candidato:** tiempo perdido, trabajo o ingreso en juego (según el dueño, rotulado estimación) y riesgo si no se hace.
5. **Elegir** el de valor alto y dificultad baja que además cumpla: ocurre varias veces al mes, hay dueño del proceso, se puede medir antes y después, y no exige reemplazar lo que ya usan.
6. **Escribir la frase y la métrica.** Una frase y un número con su línea base posible.
7. **Guardar los descartados** como hoja de ruta posterior, sin venderlos como requisito del piloto.

## Plantillas y prompts listos
**Tabla de decisión**
| Candidato | Valor 1-10 | Dificultad 1-10 | Frecuencia (hecho/estimación) | Tiene dueño | Medible | Decisión |
|---|---|---|---|---|---|---|

**Frase del cuello:** "El cuello es [paso] porque [hecho reciente]. Lo vamos a medir con [métrica] y su línea base de [período]. Todo lo demás queda fuera del piloto."

**Prompt para Claude:** "Con esta tabla y estas notas, propón el candidato con mejor relación valor/dificultad. Señala si el problema parece de capacidad y no de sistemas. Rotula cada cifra como hecho o estimación. No prometas resultados: usa 'hipótesis a medir'."

**Resultado alternativo (válido):** "Hoy no conviene un piloto: el límite es [capacidad/otro]. Sugerimos revisar en [fecha]."

## Errores comunes
- Elegir por lo que más lucen las herramientas, no por el dolor medido.
- Vender el recorrido completo como requisito inicial.
- Aceptar el pedido literal ("quiero un chatbot") sin preguntar la intención.
- Escoger un cuello sin dueño o sin forma de medirlo.
- Automatizar algo que no debería existir o que no se hace hoy de forma ordenada.
- Usar agente de IA cuando bastan reglas fijas; la IA entra solo donde aporte algo comprobable.

## Nivel de evidencia
- Matriz valor-dificultad y priorizar alto valor / baja dificultad: videos de Jack Roberts, lotes 2, 3 y 4 [video; ejemplos monetarios no verificado].
- Trío tiempo, valor y riesgo y elegir el factor más limitante: video B2 y B3 del lote 4 [video, no verificado como resultado].
- Piloto de UN cuello, taller sin mecánicos no necesita más clientes: Decisiones consolidadas 2026-10-10 [decisión].
- Flujos lineales y deterministas por encima de agentes: lote 1 (video 9) [video; la tasa de error citada es no verificado].

## Fuente
Maverick MP: Decisiones consolidadas 2026-10-10; Oferta; Nichos activos y criterios de elección. Jack Roberts, G_negocio_automatizacion_1 a _4.

## Vigencia
2026-10-11.
