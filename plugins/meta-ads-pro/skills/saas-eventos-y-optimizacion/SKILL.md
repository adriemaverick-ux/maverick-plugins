---
name: saas-eventos-y-optimizacion
description: Define qué evento optimizar para un SaaS en Meta, cómo enviar CAPI desde backend/CRM y cómo manejar la regla de ~50 eventos por semana y los ciclos largos. Usar con "qué evento optimizar", "CAPI SaaS", "StartTrial Subscribe", "optimize for trial or paid", "ciclo de venta largo".
---

# SaaS: eventos y optimización

## Objetivo
Elegir el evento de optimización con el volumen que el presupuesto permite, alimentarlo con datos de backend/CRM y evitar juzgar antes de tiempo.

## Pasos
1. **Estimar volumen semanal** de cada evento a tu presupuesto. Meta necesita ~50 conversiones/semana/conjunto para salir de aprendizaje (consenso entre AdManage, Stackmatix, RocketShip) [un experto]. Optimización por valor: ~100 compras/semana/conjunto (RocketShip) [un experto].
2. **Presupuesto mínimo por conjunto** = (50 / tasa trial→pago) x costo por trial / 7 [un experto: RocketShip]. Ejemplo con marcadores: costo por evento X = USD 20 y 50 eventos/semana → ≈ USD 143/día ≈ USD 4.300/mes por conjunto [cálculo propio].
3. **Escalera**: si no alcanzas el volumen del pago, optimiza trial/activación y sube después. Pasar al evento profundo tras 3 semanas sostenidas con 50+ eventos/semana [un experto]. Regla RocketShip (apps de suscripción): < USD 1.000/día trial; 1.000-5.000 probar ambos; > 5.000 pago [un experto].
4. **Mapeo CAPI** [un experto; no pude abrir la doc oficial de Meta]: StartTrial, Subscribe (primer pago), Purchase (renovaciones, según Superwall), custom para cancelaciones y activación; enviar value, currency y predicted_ltv. Preferir evento estándar cuando exista.
5. **Deduplicar** pixel + CAPI con el mismo event_id [oficial, extracto].
6. **Match quality**: email/teléfono con hash, fbc/fbp. Con emails de trabajo el match puede ser ~20-30%; enriquecer con personal/teléfono puede duplicarlo [caso/un experto: SaaSrise].
7. **Leads de formulario nativo**: Conversion Leads/CRM devuelve estados a Meta (sync ~15 min según vendors) [un experto]. Cifras de Meta vía tercero: +44% tasa de lead de calidad y -15% costo por lead de calidad; -17,8% costo por resultado con CAPI [oficial, vía tercero]; son promedios de plataforma, no garantías.
8. **Ciclos largos**: trial de 14 días estabiliza el CPA en ~21-28 días; de 30 días "a menudo nunca estabiliza" [un experto]. No juzgar antes de 60-90 días. Ventana 7d vista + 30d clic para comparar [un experto, [no verificado] el 30-40% de subestimación].
9. **Señales de calidad**: costo por activado, trial→pago, retención 30/90 días, SQL/oportunidad.
10. **Aprobación humana**: cambiar evento de optimización o presupuesto es gasto; requiere confirmación explícita.

## Plantillas / prompts
```
Evento candidato | Eventos/semana esperados | Costo por evento | Presupuesto/día mínimo
StartTrial       | __                       | X                | (50 x X)/7
Subscribe        | __                       | X'               | (50 x X')/7
Decisión: optimizar __ ahora; migrar a __ cuando haya 3 semanas con >=50/sem.
```

## Errores comunes
- Optimizar a lead/registro y atraer curiosos y repetidores de trial.
- Sin UTMs hasta cierre ni CAPI: no se sabe qué anuncio trae pagadores.
- Valores de evento inconsistentes (empujan entrega a usuarios de bajo valor) [un experto].
- Juzgar a 7 días un ciclo de 60-90.
- Citar el caso de herramienta SEO (CAC ~EUR 420 a ~EUR 170) como prueba: es autorreportado en un foro [no verificado].

## Nivel de evidencia
Regla de ~50 eventos: consenso de [un experto]. Cifras de CAPI: [oficial, vía tercero], promedios. Doc oficial de Meta no verificada por el autor del informe.

## Vigencia
2026-10-11.

## Skills relacionados
- `saas-economia-cac-ltv-payback`: costo por evento aceptable según CAC objetivo.
- `saas-embudos`: escalera de eventos y calificación de leads.
- `saas-plan-de-validacion`: cómo usar esta regla en la prueba de 60-90 días.
