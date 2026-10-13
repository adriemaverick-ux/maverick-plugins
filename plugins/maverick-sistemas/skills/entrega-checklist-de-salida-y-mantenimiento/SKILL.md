---
name: entrega-checklist-de-salida-y-mantenimiento
description: Úsalo al cerrar un piloto o antes de dar por entregado un sistema, para revisar permisos, propiedad de cuentas, costos recurrentes, mantenimiento, documentación y qué queda fuera. Gatillos - "entrega final", "checklist de salida", "handoff", "mantenimiento mensual", "quién paga qué después del piloto".
---

# Checklist de salida y mantenimiento

## Objetivo
Dejar por escrito qué se entregó, quién es dueño de qué, qué cuesta cada mes, quién lo mantiene y qué no está incluido. Evita sorpresas y define una continuación clara (seguir, ajustar o parar).

## Pasos
1. **Revisar el alcance entregado** contra la propuesta, punto por punto, y anotar diferencias.
2. **Propiedad y permisos:** las cuentas (CRM, WhatsApp, calendario, dominio) deben estar a nombre del cliente o con acuerdo escrito de titularidad. Accesos con mínimo privilegio; quitar accesos temporales; el cliente conoce quién tiene qué.
3. **Credenciales y tokens:** guardar en gestor de contraseñas; no compartir por chat; integraciones con tokens de alcance limitado, con rotación periódica (90 días en el caso de los tokens privados de GHL [oficial]) y revocación al terminar.
4. **Costos recurrentes:** tabla con cada herramienta, monto vigente verificado, moneda, fecha de cobro, quién paga y a nombre de quién; incluir costos por uso (mensajes, IA) y alertas de saldo.
5. **Respaldo y salida:** exportación periódica de contactos y oportunidades; el cliente puede llevarse sus datos.
6. **Documentación simple:** una hoja de cómo funciona, qué mensajes salen, cuándo se deriva a una persona, cómo pausar el sistema y a quién avisar de un problema.
7. **Capacitación breve** al equipo y registro de quién queda como responsable del proceso.
8. **Mantenimiento acordado:** qué incluye (revisión de errores, ajuste de mensajes, cambios de plataformas), canal de incidencias y tiempo de respuesta ({{SLA}}), precio ({{MENSUALIDAD}}) o "sin mantenimiento" explícito.
9. **Qué queda fuera:** lista final (nuevos canales, web, anuncios, facturación SUNAT, IA abierta, nuevos flujos).
10. **Cierre del piloto:** resultados contra la línea base, aprendizajes y decisión (continuar, ajustar, parar). Autorización por escrito para citar el caso; sin ella, no usar nombre, logo, capturas ni métricas.

## Plantillas y prompts listos
**Checklist rápido**
- Cuentas a nombre del cliente / acuerdo de titularidad
- Accesos mínimos y temporales retirados
- Tokens con alcance y fecha de rotación
- Tabla de costos recurrentes verificada
- Alertas de saldo configuradas
- Exportación de datos probada
- Documento "cómo pausar y a quién llamar"
- Mantenimiento: incluido / opcional / no incluido
- Permiso de uso del caso: sí / no
- Privacidad: aviso, consentimiento y baja funcionando

**Prompt:** "Con este alcance propuesto y esta lista de lo entregado, arma el acta de entrega con: lo cumplido, lo pendiente, costos recurrentes por herramienta con los marcadores sin completar, qué queda fuera y qué decide el cliente. No incluyas resultados que no estén medidos contra la línea base."

## Errores comunes
- Dejar cuentas a nombre de Maverick sin acuerdo ni plan de traspaso.
- No avisar de costos por uso que crecen con el volumen.
- Prometer cumplimiento legal; Maverick no da asesoría legal ni tributaria.
- Entregar sin cómo pausar el sistema ni responsable interno.
- Pegar tokens en chats o documentos.
- Usar el nombre o métricas del cliente como caso público sin permiso.
- Olvidar revisar cambios de políticas de Meta y de precios de la plataforma.

## Nivel de evidencia
- Propuesta con costos de herramientas, mantenimiento, permisos y qué queda fuera: Oferta, 2026-10-10 [decisión].
- Rotación de tokens, mínimo privilegio, riesgos de inyección de instrucciones desde mensajes entrantes: informe 02 [oficial/comunidad].
- Socio tecnológico con respaldo y canal de incidencias; mantenimiento para evitar sustitución interna: videos de Jack Roberts, lotes 1 y 4 [video; no verificado].
- Mensajería y datos: ver auto-cumplimiento-peru (nota corta de riesgo, no bloqueante).

## Fuente
Maverick MP: Oferta; Decisiones consolidadas 2026-10-10 (sección 1, uso de casos). Maverick Research: 02_ghl_crm_y_redes (6.2, 6.4, 7, 9, 12); 01_manychat_dms_instagram (8). Jack Roberts: G_negocio_automatizacion_1 (video 5), _4 (E), _5.

## Vigencia
2026-10-11. Revisar trimestralmente costos y políticas de plataformas.
