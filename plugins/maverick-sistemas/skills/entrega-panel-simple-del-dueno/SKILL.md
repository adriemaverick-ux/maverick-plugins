---
name: entrega-panel-simple-del-dueno
description: Úsalo para construir una lectura simple del negocio para el dueño (consultas, tiempo de respuesta, cotizaciones, trabajos confirmados, servicios próximos) con métricas definidas y validadas contra la fuente. Gatillos - "panel del dueño", "tablero simple", "reporte semanal", "owner dashboard", "ver estado sin preguntar".
---

# Panel simple del dueño

## Objetivo
Que el dueño vea el estado de solicitudes, cotizaciones y servicios próximos sin pedir actualizaciones al equipo. Pocas cifras, definidas con él, y que cuadren con la fuente.

## Pasos
1. **Elegir 4 a 6 indicadores** ligados al cuello del piloto: consultas recibidas, tiempo a la primera respuesta, cotizaciones enviadas y pendientes, trabajos confirmados, servicios próximos a vencer.
2. **Definir cada indicador por escrito** con el dueño (qué cuenta, qué no, período, fuente, responsable). Ver la ficha de métrica en piloto-diseno-y-metricas-antes-despues. Si no está definida, no se muestra.
3. **Construir primero la versión fea y exacta:** una tabla o vista del CRM con los números correctos, validada contra el registro original de 10 casos. Recién después mejorar el diseño.
4. **Usar lo que ya trae el CRM** (reportes de pipeline y vistas por etapa) antes de montar una aplicación aparte; el alcance exacto de los reportes en GHL está [no verificado en detalle], confirmar en la cuenta.
5. **Acceso por persona** con permisos mínimos; el dueño ve todo, el equipo ve lo suyo.
6. **Rotular datos:** hecho registrado, estimación o dato faltante. Los vacíos se muestran como vacíos.
7. **Rutina de uso:** 10 minutos semanales con el dueño para leerlo, anotar decisiones y ajustar definiciones.
8. **Resumen con IA al final y opcional:** un párrafo de lectura del período, siempre con el dato visible debajo. No agregar IA si no aporta.

## Plantillas y prompts listos
**Vista semanal sugerida**
| Indicador | Esta semana | Semana anterior | Nota (hecho/estimación) |
|---|---|---|---|
| Consultas recibidas | | | |
| Tiempo a primera respuesta humana (mediana) | | | |
| Cotizaciones enviadas / abiertas / estancadas | | | |
| Trabajos confirmados | | | |
| Próximas visitas en 30 días | | | |

**Ficha de indicador:** nombre, definición, fuente, responsable, frecuencia, límite de interpretación.

**Prompt:** "Con estas cifras de la semana y sus definiciones, escribe una lectura de 5 líneas para el dueño: qué cambió, qué quedó sin siguiente paso y qué conviene mirar. No expliques causas que no estén en los datos ni prometas tendencias."

**Frase para la reunión:** "Estas cifras son lo que registró el sistema, no una proyección. Si algo no cuadra con lo que ves en el taller, lo corregimos juntos."

## Errores comunes
- Mostrar demasiadas métricas o de vanidad (vistas, seguidores).
- Mostrar números sin definición ni verificar contra la fuente.
- Empezar por el diseño visual y romper la exactitud.
- Un panel de redes sociales cuando el dolor es de seguimiento.
- Dar acceso de administrador a todos.
- Interpretar con pocos casos como si fuera tendencia.

## Nivel de evidencia
- Panel simple con consultas, tiempo de respuesta, cotizaciones, trabajos confirmados y servicios próximos; definir cada métrica con el dueño: Oferta, 2026-10-10 [decisión].
- Primero conexión exacta y feo, luego diseño; validar contra la fuente; acceso por cliente: videos de Jack Roberts, lote 2 (video 6) [video, aplicable con adaptación].
- Reportes de GHL: informe 02 [oficial/no verificado en detalle].
- Ligar cada sistema a un número medido: lote 4 [video; cifras no verificado].

## Fuente
Maverick MP: Oferta (punto 5); Decisiones consolidadas 2026-10-10. Maverick Research: 02_ghl_crm_y_redes (sección 2). Jack Roberts: G_negocio_automatizacion_2 (video 6 y aplicabilidad), _4 (E).

## Vigencia
2026-10-11.
