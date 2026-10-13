---
description: Crea una web o landing de punta a punta (estrategia, plan, diseño, copy, build local) con el pipeline del plugin. No publica.
argument-hint: "[negocio o idea] [objetivo: leads | ventas | reservas] [URL de referencia opcional]"
---

Crea una web para: $ARGUMENTS

Sigue este flujo, usando las skills `pipeline-web-completo`, `copy-por-pain-points` y, si aplica, `clonar-estructura-web-por-referencia`, `web-3d-scroll-animado` y `backend-supabase-login-leads`. Delega la construcción en el agente `constructor-web` si está disponible.

1. Si falta información, pregunta en una sola tanda: avatar, tipo de tráfico (frío, cálido, outbound), 3 problemas del visitante, objetivo de conversión, marca (colores, tipografía, logo) y si hay referencia visual. No inventes datos del negocio.
2. Entra en modo plan y propón: estructura de secciones, páginas, copy base por pain points, integraciones (formulario, CRM, base de datos) y estilo. Espera aprobación.
3. Construye en una carpeta nueva, instala dependencias y corre en localhost. Revisa móvil.
4. Configura secretos solo con variables de entorno y un `.env.example` sin valores; nunca pegues claves en archivos ni en el chat.
5. Pasa una auditoría rápida con `auditor-qa-web` y presenta un resumen: qué se creó, qué falta y qué decisiones necesito de mí.
6. Termina aquí. No hagas push ni despliegue; para publicar, ofrece `/publicar-web`.
