---
name: backend-supabase-login-leads
description: Usar para dar a una web login, dashboard, base de datos y captura de leads (Supabase, webhooks a CRM o email, Stripe en modo prueba). Gatillos - "Supabase", "login", "registro de usuarios", "dashboard con datos", "guardar leads", "webhook GoHighLevel", "RLS", "Stripe sandbox".
---

# Backend Supabase: login, dashboard y leads

## Objetivo
Añadir persistencia y cuentas a una web generada por IA con seguridad básica correcta, y reenviar leads a un CRM o email sin exponer claves en el navegador.

## Pasos
1. **Proyecto Supabase** (gratis para empezar). Conecta por MCP o CLI con un token de acceso personal de caducidad corta, o usa la URL y la clave pública (anon) solo en el front. La clave de servicio (service role) NUNCA va al front ni al chat; todas las claves en variables de entorno.
2. **Esquema.** Pide a Claude el SQL de tablas (usuarios/perfiles, datos del dashboard, leads) y que pida confirmación antes de ejecutar. Revisa el SQL; si da error de línea, devuélvelo al agente.
3. **Auth.** Email y contraseña. Desactiva "confirm email" solo en desarrollo; actívalo en producción.
4. **RLS (row level security) activo en todas las tablas**, con políticas por usuario. Verifica en Table Editor y prueba con dos usuarios y una ventana incógnita. Para rol admin: columna de rol y políticas específicas.
5. **Dashboard.** Primero propósito (problema, usuario, decisión), una métrica dominante, datos reales de Supabase (compara un registro en la BD con la UI), luego filtros y estados de carga/error.
6. **Leads.** Formulario -> función backend (edge function o ruta de servidor) que guarda en Supabase y reenvía a email/CRM. Los servicios que no admiten llamadas desde el navegador exigen este paso intermedio.
7. **CRM por webhook.** En el CRM crea un workflow con trigger de webhook entrante, copia la URL (guárdala como variable de entorno), envía una petición de prueba, mapea campos a "crear contacto" y encadena emails con esperas (día 1, 3, 7; idealmente 5 correos o más).
8. **Pagos (opcional).** Stripe solo en modo prueba (tarjeta de prueba publicada por Stripe) hasta validar; sincroniza el estado del plan a la BD; las claves live jamás en el repo.
9. Prueba de punta a punta: registro -> dato guardado -> lead en CRM -> email recibido.

## Prompts de ejemplo
- "Con el MCP de Supabase propón el esquema para usuarios, leads y métricas. Muéstrame el SQL y espera mi confirmación antes de ejecutarlo; activa RLS en cada tabla."
- "El formulario debe guardar el lead en Supabase y reenviarlo al webhook cuya URL está en la variable CRM_WEBHOOK_URL. Hazlo en una función de servidor, no en el navegador."
- "Audita las políticas RLS: intenta leer datos de otro usuario y dime si algo se filtra."

## Errores comunes
- Dejar RLS apagado "porque es interno".
- Pegar tokens o claves en el chat o el repo; rota las que expusiste.
- Probar solo con el admin; prueba como usuario normal.
- Olvidar poner las variables de entorno en Vercel y ver errores 401/404 en producción.

## Vigencia
Paneles de Supabase, nombres de claves y la UI del CRM cambian. Cifras de ingresos de sistemas de onboarding citadas por el creador: no verificado. Verifica la documentación vigente.

## Checklist de salida
- [ ] RLS activo en todas las tablas y probado con dos usuarios.
- [ ] "Confirm email" activado en producción.
- [ ] Clave de servicio fuera del front y del repo.
- [ ] URL de webhook y claves en variables de entorno.
- [ ] Lead de prueba llega a BD, CRM y email.
- [ ] Pagos solo en modo prueba hasta validar.
