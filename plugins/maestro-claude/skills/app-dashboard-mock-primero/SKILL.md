---
name: app-dashboard-mock-primero
description: Construye dashboards y apps (login, panel, formularios, pagos) empezando con datos mock y buen diseño, y conecta backend después. Usar con "dashboard", "app con login", "Supabase", "mock data", "SaaS", "Stripe en sandbox" o "panel admin".
---

# Apps y dashboards: mock primero

## Objetivo
Acertar el diseño y el flujo con datos de prueba antes de gastar tiempo en infraestructura; luego conectar base de datos, auth y pagos con seguridad.

## Pasos
1. Moodboard y referencia: 3-5 capturas de apps que admiras y su design system. Pide el aspecto antes que la funcionalidad compleja: lo difícil es el diseño; la infraestructura básica la resuelve la IA con facilidad.
2. Primera versión con mock: tabla, gráficos, modales, estados hover, skeletons, vacíos y errores, con una capa de datos aislada para poder cambiarla.
3. Llega a ~80 %: login, navegación y 1-2 flujos clave. Itera con capturas y feedback visual concreto.
4. Copy y microcopy: pasa por anti-slop; las apps se escanean.
5. Backend: conecta una base de datos mediante el conector/MCP oficial con un token de caducidad corta, creado por ti y guardado en la configuración local de la herramienta, no en el repo. Pide que cree tablas faltantes con confirmación previa a cada cambio de esquema.
6. Seguridad desde el inicio: activa row-level security en cada tabla y verifícalo; ejecuta los advisors de la plataforma y corrige avisos. Para pruebas puedes desactivar la confirmación de email, pero reactívala en producción.
7. Pagos: usa solo modo de prueba/sandbox con tarjetas de prueba oficiales; sincroniza el estado del plan a tu base de datos; no pases a producción sin revisión humana.
8. Prueba el flujo real: registro, login, edición de un dato, cierre de sesión y reingreso para confirmar persistencia.
9. Publica vía GitHub y despliegue; guarda puntos de commit durante el proyecto.
10. Si reinicias el agente (p. ej. tras añadir un MCP), pide antes un prompt de continuación.

## Prompts de ejemplo
- "Construye un dashboard con datos mock que tenga el lenguaje visual del design system adjunto: tabla filtrable, 3 gráficos, modal de detalle, estados de carga y vacío. Aísla los datos en un módulo para sustituirlos luego por una base real."
- "Conecta la base de datos con el conector oficial. Antes de ejecutar cualquier migración, muéstrame el SQL y espera mi confirmación; activa RLS en todas las tablas y dime cómo lo verificaste."
- "Ejecuta los avisos de seguridad y rendimiento de la plataforma, resume los críticos y propón correcciones paso a paso."

## Errores comunes
- Conectar backend antes de validar el diseño.
- Tablas sin RLS.
- Pegar tokens o claves en el chat persistente, el repo o skills compartidas; usa variables de entorno y caducidad corta.
- Login "inválido" por confirmación de email pendiente.
- Pasar pagos a producción sin pruebas en sandbox.

## Vigencia
Interfaces de Supabase, Stripe, Vercel y conectores MCP cambian; confirma pasos en su documentación actual. Los planes gratuitos y límites mencionados por terceros: no verificado.

## Criterios de salida
- Diseño aprobado con mock antes de conectar backend.
- RLS activo en todas las tablas y avisos de seguridad revisados.
- Pagos solo en sandbox hasta revisión humana.
- Flujo registro, edición, cierre y reingreso probado de punta a punta.
