---
name: testeo-creativo-y-fatiga
description: Usar para planear pruebas de creativos en Meta (conceptos vs ángulos vs variaciones, cantidad y cadencia), leer resultados por anuncio y detectar o refrescar fatiga creativa. Gatillos - "testeo de creativos", "creative testing", "fatiga", "refresh", "qué anuncio ganó", "Andromeda", "diversificación".
---

# Testeo creativo y fatiga

## Objetivo
Decidir qué probar, cuánto lanzar, cómo leer resultados sin engañarse con la distribución de gasto y cuándo refrescar.

## Pasos
1. **Separa niveles**: concepto (idea/argumento), ángulo (marco emocional o racional), variación (ejecución: hook, creador, corte, CTA). Prueba primero conceptos muy distintos; luego optimiza ejecución. [consenso en la distinción; vocabulario un experto]
2. **Qué cuenta como distinto**: concepto, escena inicial, persona/voz, formato, estructura, emoción, oferta. No cuenta: mismo video con otro color o titular. Heurística: si dos anuncios se describen con la misma frase, son uno. [consenso; umbrales 40%/60% de similitud: no verificado]
3. **Cuántos**: rango práctico 8-15 distintos por ad set/campaña de prueba. Para presupuesto pequeño/mediano (inferencia): 5-8 conceptos de entrada con 1-2 variaciones y sumar 3-5 nuevos por semana. [consenso blando + inferencia]
4. **Estructura consolidada**: pocas campañas y ad sets, muchos creativos distintos; texto principal único y formatos mixtos. [consenso / dato oficial vía Jon Loomer, verificar]
5. **Cadencia semanal**: lunes lectura; mar-mié briefs y producción (>=2 conceptos nuevos); jueves subir con QA; vie-dom dejar correr sin editar presupuesto >20%. [inferencia consistente con fuentes]
6. **Lectura por anuncio** (ver orden abajo).
7. **Prueba limpia**: herramienta oficial Creative Testing (2-5 anuncios duplicados, Highest Volume, sin Cost Cap/Bid Cap/ROAS goal, <=20% del presupuesto, ~7 días por defecto). Limitaciones: duplica anuncios, muestra pequeña. [dato oficial de la herramienta, descrito por Jon Loomer]
8. **Refresco**: ver sección de fatiga.

## Orden de lectura
1. % de gasto e impresiones por anuncio antes de mirar CPA; que gaste más no prueba que sea mejor. [posiciones opuestas entre fuentes]
2. Embudo: hook -> hold -> CTR enlace -> costo por mensaje -> % calificados -> cita/visita -> venta (cruza con CRM).
3. Mínimos heurísticos: >=2-3x CPA objetivo de gasto por variante; 48-72 h o un gasto bajo para descartar claramente malos. [consenso débil]
4. No juzgar por CTR temprano.
5. Aplica la tabla de decisión de `anatomia-anuncio-ganador`.

## Fatiga y refresco
- Señales (combinar al menos 2): frecuencia semanal 2,5-3,0 en prospección (alerta), >4 mala; CTR cae 15-20% semana a semana; hook rate <25%; CPA sube con valor de pedido estable. Retargeting se agota antes. [un experto, proveedores]
- Fatiga es sobreexposición; similitud es falta de diversidad. [formulación de proveedor, no confirmada en Meta]
- Ritmo de partida: revisar cada 2-4 semanas; en mobiliario la mitad se retira en ~26 días. [un experto]
- Mezcla de refresco sugerida: ~50% conceptos nuevos, 30% variantes refinadas, 20% ganadores probados. [un experto]
- Refresca hook y escena inicial, creador/voz, formato u oferta; no solo recolorear.

## Plantilla lista para pegar (registro de prueba)
```
Ronda #: __  Fecha: __  Hipótesis: "Si [cambio], entonces [métrica] porque [razón]"
Variable que cambia: __   Anuncios (convención concepto_ángulo_hook_formato_versión): __
Regla de corte: __   Lectura el día: __
Resultados: anuncio | % gasto | hook | hold | CTR | costo/mensaje | % calificados | decisión
Aprendizaje: __   Siguiente ronda: __
```

## Errores comunes
- Declarar ganador sin mirar el reparto de gasto.
- Editar presupuesto o anuncios constantemente (reinicia aprendizaje). [consenso]
- Pocos conceptos y meses sin refresco.
- Medir solo CPL de Meta sin cruzar con calificación en CRM.
- Variar solo hooks y creer que es diversidad.

## Nivel de evidencia
Principio de diversidad [dato oficial: Meta Engineering sobre Andromeda, y guía vía Loomer] y [consenso]. Cantidades, tasa de ganadores (~5%), ritmos y señales de fatiga [un experto] (Motion, Segwise, Superads; proveedores con interés comercial). Umbral de 50 eventos semanales [no verificado] si cambió a 25. Calibra con tu histórico.

## Vigencia
2026-10-11.
