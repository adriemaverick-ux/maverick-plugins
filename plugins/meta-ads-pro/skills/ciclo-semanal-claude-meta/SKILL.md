---
name: ciclo-semanal-claude-meta
description: El ritual semanal del sistema Claude + Meta Ads de Maverick - qué hace Claude, qué hace Adrie, qué necesita aprobación, cada día y cada mes. Usar al operar campañas activas, al planear la semana de pauta o con "ciclo semanal", "qué toca hoy en ads", "rutina de Meta Ads", "operación semanal".
---

# Ciclo semanal Claude + Meta Ads

## Principio
Claude **lee, analiza, escribe y produce**. Adrie **graba, vende, decide y aprueba**. Meta **no se toca a mitad de semana**: los cambios se juntan en un solo momento para no reiniciar el aprendizaje.

## Todos los días (Adrie, unos 15 minutos)
- Responder los WhatsApp **en minutos**.
- Mover las tarjetas en GHL: Conversación → Calificado → Compró, con el monto. Así el puente le avisa a Meta.

## Lunes: números (Claude)
1. Leer los últimos 7 días en solo lectura (MCP de Meta + `tablero-costo-por-venta`).
2. Revisar primero el registro de cambios y después los números.
3. Entregar el informe: gasto, costo por venta por anuncio y por concepto, frecuencia, top 3 y bottom 3, y **3 acciones propuestas** (cortar, mantener o escalar un 20 %) con su evidencia.
4. **Adrie aprueba o rechaza** cada acción.

## Martes: ideas (Claude)
1. Leer las objeciones y frases reales de los chats de la semana, sin datos personales.
2. Proponer **2 o 3 conceptos nuevos**, realmente distintos de los activos (`testeo-creativo-y-fatiga`).
3. Escribir cada uno con la plantilla de 9 bloques y 3 hooks, desde la lluvia de hooks.
4. Adrie elige.

## Miércoles: grabación (Adrie)
Grabar los guiones elegidos. Los 3 hooks se graban seguidos al inicio, y el final se graba en dos versiones: orgánico («Comenta X») y anuncio («Toca el botón…»).

## Jueves: fábrica (Claude)
Editar con `fabrica-de-anuncios`: un video por hook, formatos 9:16 y 4:5, zonas seguras, nombres `concepto_hook_formato` y la URL con `{{ad.id}}`. Si cada concepto tiene página propia, se genera también.

## Viernes: carga (Adrie aprueba)
- Los anuncios nuevos entran **juntos** al conjunto activo (como máximo un 20 % del presupuesto para lo nuevo, si aplica). Se apagan los que se aprobó cortar el lunes.
- Desde el viernes hasta el lunes siguiente no se toca nada.

## Cada mes (Claude)
- Revisar `novedades-meta-2026-11` y actualizar el plugin.
- Recalcular el CPA máximo con las comisiones y los reembolsos reales.
- Decidir con Adrie si se sube de escalón de evento (por ejemplo, de Lead a Purchase cuando haya volumen).

## Lo que nunca hace Claude sin aprobación escrita
Crear, activar, pausar o borrar campañas, cambiar presupuestos, publicar anuncios o mandar mensajes a clientes.

## Vigencia
2026-11-13.

## Relacionados
`tablero-costo-por-venta`, `fabrica-de-anuncios`, `reglas-de-decision`, `workflows-claude-meta-ads`, `puente-ghl-whatsapp-a-meta`.
