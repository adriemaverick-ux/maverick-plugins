---
name: prop-cotizar-un-piloto
description: Úsalo para calcular el precio de un piloto con marcadores y fórmulas, sin precios estándar, separando honorarios de costos de herramientas y verificando contra el valor que el dueño estima. Gatillos - "cotizar piloto", "cuánto cobrar", "precio del piloto", "price a pilot", "calcular honorarios".
---

# Cotizar un piloto

## Objetivo
Obtener un precio defendible y por escrito, sin cifras estándar: cada empresa se revisa por separado. Este skill entrega la lógica y los marcadores; Adrie pone los números y confirma.

## Pasos
1. **Fijar el alcance** del piloto: un cuello, canales, integraciones, quién prueba, cuánto dura ({{DURACION}}), qué queda fuera.
2. **Estimar horas** por bloque: descubrimiento y mapa ({{H_DIAG}}), configuración ({{H_CONFIG}}), mensajes y plantillas ({{H_MENSAJES}}), pruebas con el equipo ({{H_PRUEBAS}}), capacitación breve ({{H_CAPAC}}), soporte durante el piloto ({{H_SOPORTE}}) y medición ({{H_MEDICION}}). Añadir margen para imprevistos ({{PCT_IMPREVISTOS}}).
3. **Honorarios del piloto** = suma de horas x {{TARIFA_HORA}}. Es el piso de costo interno, no el precio.
4. **Costos de herramientas** (aparte, rotulados y verificados en la cuenta antes de cotizar): suscripción del CRM, número de WhatsApp y tarifas por mensaje, automatización (n8n o Make), IA si aplica, dominio o correo. Indicar quién contrata y paga ({{CUENTA_A_NOMBRE_DE}}).
5. **Contraste con el valor.** Pedir al dueño su estimación del costo de no actuar (rotulada "estimación del dueño"). Los videos sugieren cobrar una fracción acotada del valor medible; usar solo como contraste, no como cálculo automático.
6. **Decidir estructura:** piloto de pago único, o piloto más mensualidad de operación ({{MENSUALIDAD}}) si el sistema debe seguir funcionando. Pago por hitos o 50/50 como opción ({{ESQUEMA_PAGO}}). Aclarar moneda, IGV y comprobante con el contador ({{MONEDA}}, {{IGV}}).
7. **Preparar dos opciones por funciones, no por rebajar precio:** piloto base y piloto con un componente extra; la segunda sirve de ancla.
8. **Validar con Adrie** y registrar los supuestos. Ningún precio sale al cliente sin confirmación humana.

## Plantillas y prompts listos
**Tabla de cálculo**
| Concepto | Marcador | Quién lo paga | Recurrente |
|---|---|---|---|
| Honorarios piloto | {{HORAS}} x {{TARIFA_HORA}} + {{PCT_IMPREVISTOS}} | Cliente | No |
| Suscripción CRM | {{COSTO_CRM}} (verificar en cuenta) | {{QUIEN}} | Mensual |
| WhatsApp (número + mensajes) | {{COSTO_WA}} + tarifas Meta por mensaje | {{QUIEN}} | Mensual/uso |
| Automatización / IA | {{COSTO_AUTO}} | {{QUIEN}} | Mensual/uso |
| Operación posterior | {{MENSUALIDAD}} | Cliente | Mensual |

**Referencias de costo a verificar (no son precios de Maverick):** GHL Starter figura en USD 97 al mes y WhatsApp en USD 10 al mes por sub-cuenta más tarifas de Meta [oficial, leído 2026-10-11, confirmar en la cuenta]; desde 2026-10-01 los mensajes de servicio dentro de la ventana pasan a ser facturables, con un tramo gratis [oficial]. ManyChat: precios contradictorios entre fuentes [no verificado].

**Prompt:** "Con estos supuestos de horas y estos costos de herramientas, arma la tabla de cotización con marcadores sin rellenar los que no tengo. Marca cada supuesto como dato verificado o estimación y señala qué falta confirmar."

## Errores comunes
- Fijar un precio estándar o copiar cifras en dólares de los videos.
- Mezclar honorarios con costos de herramientas, o esconder los recurrentes.
- Regalar el piloto completo sin métrica ni alcance.
- Olvidar IGV, moneda, comprobante y costos por uso (mensajes, IA).
- Prometer resultado para justificar el precio.
- Cobrar por horas visibles en vez de explicar el alcance y lo medido.

## Nivel de evidencia
- Sin precios ni plazos estándar hasta revisar cada empresa: Oferta, 2026-10-10 [decisión].
- Costos de GHL y WhatsApp: informe 02 [oficial, con puntos [no verificado], por ejemplo la tarifa de utilidad para Perú desde 2026-10-01].
- Precio por valor, anticipo 50/50, ancla y mínimo de meses: videos de Jack Roberts, lotes 2 y 3 [video; todas las cifras no verificado y de otro mercado].

## Fuente
Maverick MP: Oferta; Decisiones consolidadas 2026-10-10. Maverick Research: 02_ghl_crm_y_redes (secciones 3, 4.3, 7); 01_manychat_dms_instagram (3.2). Jack Roberts: G_negocio_automatizacion_2 (videos 1, 9), _3 (módulo 6).

## Vigencia
2026-10-11. Los precios de herramientas cambian con frecuencia: reverificar antes de cada cotización.
