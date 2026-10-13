---
name: ecom-plan-90-dias-casa-soyer
description: Úsala para armar el plan de 90 días de pauta de Casa Soyer - prerrequisitos de limpieza de catálogo, fases de prueba pequeñas y reglas de corte, sin montos de dinero fijos. Gatillos - "plan 90 días", "Casa Soyer", "primera campaña", "limpieza de catálogo", "prerrequisitos", "roadmap ecommerce".
---

# Plan de 90 días - Casa Soyer

## Objetivo
Pasar de cero pauta histórica (100% tráfico orgánico en 90 días, 4.683 sesiones) a un sistema medible de piezas de ticket alto vendidas por WhatsApp, probando en pequeño y sin gastar sin aprobación humana. Los montos de dinero los define el usuario.

## Prerrequisitos (Fase 0, antes de gastar)
1. Decisiones de Ana/Marbe: costo real por pieza de las ~48 piezas vendibles;
   exclusión de "Adelanto" y Falabella de la comisión, por escrito.
2. Limpieza de catálogo por fases con dry-run y confirmación de Marbe/Ana: catálogo muerto (819 archivados, 201 draft); ~40 SKUs fantasma ($0 y stock 10) a draft o colección excluida;
   conteo físico de los 12 SKUs con stock negativo; fusionar duplicados; fotografiar 9 SKUs sin imagen;
   cargar costo real (el campo de Shopify está vacío o errado).
3. Medición: píxel único, CAPI con event_id, EMQ, etiquetas de CRM (ver `ecom-catalogo-feed-shopify`, `ecom-ticket-alto-pieza-unica`).
   Meta Events Manager no está auditado: requiere acceso.
4. Economía: calcular MC, ROAS/CPA de equilibrio y comisión por pieza (`ecom-economia-roas-equilibrio-comision`).

## Fases (semanas aproximadas)
1. Semanas 1-2: Fase 0 y estructura mínima en borrador/pausa para aprobación.
2. Semanas 3-5, prueba pequeña: 1 campaña CTWA, 2-3 piezas ancla de buen margen, 2-3 conceptos por pieza;
   presupuesto [definido por el usuario]. Meta: aprender qué conversaciones califican, no vender.
3. Semanas 6-8: añadir eventos de calificación/cotización/venta por CAPI;
   comparar costo por conversación, por calificada y por venta;
   retargeting pequeño con exclusión de compradores y vendidas.
4. Semanas 9-12: ampliar a una familia de piezas y a un segundo ángulo; prueba on/off simple de incrementalidad;
   preparar calendario de campañas (CyberWow, Q4) [no verificado fechas].
5. Revisión semanal: MER (sin Adelanto/Falabella), CPA por etapa, tasa conversación -> venta, margen real y comisión, piezas vendidas/pausadas, tiempo de primera respuesta.

## Criterios de decisión (a calibrar por el usuario)
- Avanzar de fase solo si hay señal medible y el usuario aprueba el siguiente gasto.
- Pausar un anuncio que gasta >= 3x el CPA de equilibrio sin conversación calificada;
   rotar concepto si frecuencia sube, CTR baja y CPA sube a la vez [ejemplos ilustrativos del informe].
- Google: no activar Shopping/PMax hasta limpiar el feed; Search de marca solo tras validar Meta [Casa Soyer].

## Plantillas / prompts
- Prompt: "Genera el plan de las semanas [X-Y] con tareas, responsable, métrica de salida y los puntos que requieren mi aprobación de gasto.
   No uses montos: déjalos como [MONTO_A_DEFINIR]."
- Tabla de piezas: pieza | precio | costo real | MC | stock | estado de ficha | prioridad.

## Errores comunes
1. Pautar antes de cargar el costo real y de cerrar la exclusión de comisión.
2. Subir al feed SKUs fantasma o duplicados.
3. Editar o archivar en masa sin confirmación de los dueños (tienda de producción).
4. Esperar escala lineal: es "galería curada + venta consultiva"; el techo es el stock.
5. Mezclar Studio Soyer (servicios) con Casa Soyer (productos).

## Nivel de evidencia
Hechos de la tienda: [auditoría Casa Soyer 2026-09-19/20, no re-verificada]. Heurísticas de pruebas y corte: [un experto]/ilustrativas. No existe benchmark de piezas únicas en Meta [no verificado].

## Vigencia
2026-10-11. Reverificar el estado de la tienda antes de ejecutar cada fase.
