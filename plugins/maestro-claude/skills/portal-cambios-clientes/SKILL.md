---
name: portal-cambios-clientes
description: Usar al entregar una web a un cliente y querer controlar sus peticiones de cambio con un formulario propio conectado a Notion u otra base, en vez de chats sueltos. Gatillos - "portal de cambios", "peticiones del cliente", "client requests", "mantenimiento de web", "retainer".
---

# Portal de cambios para clientes

## Objetivo
Dar al cliente una página sencilla para pedir cambios, guardarlos en una base de datos y procesarlos con revisión humana según el riesgo. Ordena el mantenimiento y sostiene un servicio recurrente.

## Pasos
1. **Elige modelo de cambios:** retainer con horas, CMS para que edite solo, o portal intermedio (este skill). Acuerda por escrito qué entra y qué es trabajo extra.
2. **Crea la página** `/cambios` (puede ir protegida) con el mismo estilo del sitio: formulario con tipo de cambio (diseño, bug, funcionalidad, copy, otro), descripción, URL afectada, adjunto opcional y contacto.
3. **Base de datos.** Crea una base "Client requests" en Notion (o Supabase) con campos: fecha, tipo, descripción, página, estado (nuevo, en curso, hecho), prioridad y quién lo revisó. Conecta con una integración cuyo secreto vive en variable de entorno; en Notion comparte la base con esa integración.
4. **Envío seguro.** El formulario llama a una ruta de servidor que valida y escribe en la base; nunca expone el secreto en el navegador; añade anti-spam básico y límite de envíos.
5. **Procesado diario.** Un agente (tarea programada o skill) revisa solicitudes nuevas, resume, clasifica y propone el cambio. Regla de ejemplo: cambios de copy pueden aplicarse en una rama y previsualizarse; cambios estructurales o de pago pasan por revisión manual.
6. **Entrega.** Preview de Vercel, aprobación del cliente, merge, estado "hecho" y aviso.
7. **Mide:** tiempo de respuesta y número de cambios por mes para ajustar la tarifa recurrente (importes: no verificado; fíjalos con tu mercado).

## Prompts de ejemplo
- "Crea la página /cambios con el estilo del sitio y un formulario (tipo, descripción, URL, adjunto). Guarda cada envío en la base Notion 'Client requests' desde una ruta de servidor usando NOTION_TOKEN de las variables de entorno."
- "Revisa las solicitudes en estado 'nuevo', clasifícalas por riesgo y propón un plan de cambio por cada una. No apliques nada estructural sin mi aprobación."
- "Aplica la solicitud 12 en una rama, genera la preview y déjame el resumen del diff."

## Errores comunes
- Aplicar cambios automáticos directo a producción.
- Olvidar compartir la base de Notion con la integración (da error de permisos).
- Formularios sin validación ni límite: spam y datos personales sin protección.
- No acordar alcance con el cliente.

## Vigencia
API de Notion y planes cambian. Los precios o resultados de agencias citados por el creador: no verificado. Trata los datos del cliente conforme a la normativa de privacidad aplicable.

## Checklist de salida
- [ ] Alcance del servicio acordado por escrito con el cliente.
- [ ] Secreto de la integración en variable de entorno, nunca en el navegador.
- [ ] Base compartida con la integración y campos de estado creados.
- [ ] Validación y límite de envíos en el formulario.
- [ ] Regla de riesgo definida (copy automático en rama, estructura manual).
- [ ] Aviso al cliente al cerrar cada solicitud.
