---
name: crm-ghl-configuracion-para-maverick
description: Úsalo para decidir y configurar GoHighLevel (GHL) como CRM único de Maverick: plan, pipelines, WhatsApp, calendarios y workflows. Gatillos: "configurar GHL", "GoHighLevel", "elegir CRM", "plan Starter", "set up GHL pipeline".
---

# GHL como CRM único: configuración

## Objetivo
Usar GHL como única fuente de verdad (contactos, pipeline, calendario, bandeja, WhatsApp, cotizaciones) sin duplicar sistemas. Recomendación del informe: Starter a US$97/mes, que cubre 3 sub-cuentas con contactos y usuarios ilimitados; una para la empresa y dos de reserva o pruebas.

## Pasos
1. Antes de pagar, confirmar los precios en la cuenta (Agency View > Billing); HighLevel los cambia a menudo. Hay prueba de 14 días con cobro automático al terminar.
2. Crear la sub-cuenta "Maverick". Confirmar en Settings > Private Integrations si el plan permite tokens privados; qué incluye "API básica" en Starter es [no verificado].
3. Configurar email con dominio propio (SPF/DKIM/DMARC) y datos de la empresa.
4. Crear el pipeline con las cinco etapas acordadas y los campos mínimos (ver `crm-pipeline-etapas-y-datos-minimos`). Añadir un campo de consentimiento (sí/no, fecha, canal).
5. Conectar Instagram (Business o Creator), Facebook y Google Business Profile; LinkedIn requiere reconectar cada cierto tiempo. YouTube y Threads en Social Planner: [no verificado], confirmar en la cuenta. No usar la cuenta personal.
6. WhatsApp: elegir ruta (coexistencia con la app Business, número nuevo, o migrar). Costo: US$10/mes por sub-cuenta más tarifas de Meta por mensaje. Desde 2026-10-01 GHL quitó su recargo del 5 % y los mensajes de servicio son facturables (primeros 1.000 por número y mes gratis). Cargar la wallet y activar alerta de saldo. Con coexistencia, las plantillas solo se envían desde el CRM.
7. Crear 3-5 plantillas (bienvenida, confirmación de demo, seguimiento de cotización, recordatorio de visita) clasificadas correctamente. Una respuesta automática puede funcionar con reglas; no activar envíos masivos.
8. Calendarios: "Diagnóstico/Demo" y "Visita técnica" con recordatorios.
9. Workflows iniciales: lead nuevo, seguimiento de cotización, recordatorio de próxima visita, reseña post-servicio, baja/opt-out. Todo envío saliente a prospectos queda en revisión humana hasta tener consentimiento y criterio legal.
10. Facturación: GHL no emite comprobantes SUNAT; usar un facturador peruano enlazado por webhook, con revisión humana al inicio.
11. Seguridad: no guardar tokens ni IDs de integración en notas de texto plano ni pegarlos en chats; si ya están en una nota, rotarlos y moverlos a un gestor de secretos.
12. Revisar costos semanalmente el primer mes y exportar contactos y oportunidades periódicamente.

## Plantillas
Checklist de verificación previa:
```
Plan y precio confirmados en Billing: sí/no
PIT permitido en este plan: sí/no/no verificado
Pipeline real tiene las 5 etapas: sí/no
Wallet con alerta: sí/no
Canal WhatsApp: ruta elegida y número
Revisión legal de plantillas: pendiente/ok
```

## Errores comunes
- Dar por configurado en GHL lo que solo está definido en una nota.
- Duplicar bandeja con otra herramienta de DM sobre la misma cuenta; ManyChat está descartado (decisión de Adrie, 2026-10-21).
- Confiar en blogs para precios de IA o WhatsApp.
- Enviar WhatsApp promocional fuera de ventana sin plantilla aprobada ni consentimiento.
- Prometer chat desde Google (Business Messages ya no existe) o cobro online sin verificar pasarelas en Perú.

## Nivel de evidencia
- Starter US$97/mes, 3 sub-cuentas, WhatsApp US$10/mes y cambios del 2026-10-01: [oficial] según el informe 02 (leído 2026-10-11).
- Alcance exacto de la API en Starter, pasarelas de pago en Perú, tarifa de utilidad de Perú desde octubre: [no verificado].
- Que GHL esté ya configurado para envíos automatizados: [no consta en el vault].

## Fuente
Informe 02 (GHL, CRM y redes), nota GHL (solo existencia de credenciales; no se copian), pipeline comercial y decisiones consolidadas.

## Vigencia
2026-10-11. Precios y políticas cambian; reconfirmar antes de contratar.
