---
name: marca-metricas-y-atribucion
description: Usar para medir una marca personal hasta la venta: costo por lead, cita y cliente, show rate, CAC, CAPI de citas y ventas, y atribución difusa. Gatillos - "costo por lead", "CAC", "show rate", "CAPI citas", "atribución", "cómo medir marca personal".
---

# Métricas y atribución para marca personal

## Objetivo
Medir lo que importa (lead calificado, cita, venta) y devolver esos eventos a Meta, aceptando que la atribución de marca es difusa.

## Pasos
1. **Jerarquía:** negocio (ingresos, CAC, margen) > embudo (CPL, costo por cita, por asistente, por cliente) > calidad (lead a cita, show rate, cierre, tiempo de respuesta) > creativo (retención, CTR de enlace, frecuencia) > marca (seguidores netos, visitas, búsquedas de marca, DMs).
2. **Fórmulas** (marcos propios):
   - Costo por cita = gasto / citas efectivas (o CPL / tasa de agendamiento).
   - CAC = (pauta + herramientas + producción) / clientes nuevos.
   - Cierre necesario = CAC objetivo / (ticket x margen) por cita.
3. **Tracking:** píxel y Conversions API con eventos de lead, cita agendada, cita asistida y venta. Enviar "cita" o "venta" por CAPI entrena al sistema en calidad, no solo volumen [un experto]; Meta añadió envío de eventos de lead por CAPI [oficial, Social Media Today oct 2025].
4. **Datos que no sean de Meta:** pregunta "¿cómo nos conociste?" en el formulario, registra DMs y búsquedas de marca.
5. **Ajusta atribución:** al 2026-03-10: click-through 7 días, engage-through 1 día, view-through 1 día; el panel subvalora marca y video [un experto: Loomer]. Para leads o remarketing, considera desactivar engage-through [un experto].
6. **Línea base y registro semanal** de gasto, CPM, CTR, CPL, citas, ventas y aprendizajes.
7. **Brand Lift no es viable** para una marca personal pequeña por umbral de presupuesto [un experto/no verificado]; usa holdouts manuales por región (hipótesis propia).

## Plantillas / prompts
```
Semana | Gasto | Leads | Calificados | Citas | Asistieron | Ventas | CAC | Notas
```
Prompt: "Con esta tabla semanal calcula costo por lead calificado, por cita, show rate y CAC; señala qué etapa del embudo pierde más y qué dato falta."

## Errores comunes
- Reportar costo por seguidor o alcance como éxito.
- No enviar a Meta citas y ventas; optimizar solo a volumen.
- Juzgar video y marca con ventanas cortas sin otras señales.
- Comparar tu CPL con el de EE. UU.; son referencia, no promesa.

## Salida esperada
- Tabla semanal completa del lead a la venta.
- Eventos CAPI de cita y venta definidos y verificados.
- Fuente declarada ("¿cómo nos conociste?") junto a la atribución de Meta.
- Lectura honesta: qué etapa pierde más y qué dato falta.

## Nivel de evidencia
- [benchmark] CPL mediano Facebook USD 27,66 (WordStream, abr 2024 a jun 2025); CPC mediano leads USD 1,92. Variación por definición de lead y Q4 +30 a 60%.
- [un experto] Atribución 2026 y retiro de ventanas de 7 y 28 días de vista en la API (desde 2026-01-12; Meta no confirmado en la búsqueda).
- [no verificado] Todo dato de Lima/Perú (S/ 3 a 30 de CPL, kom.pe).
- No hay benchmarks de costo por cita ni seguidor con metodología sólida.

## Vigencia
2026-10-11.
