---
description: Publica una web con GitHub y Vercel tras un pre-vuelo y SIEMPRE con confirmación explícita antes de desplegar.
argument-hint: "[carpeta del proyecto] [dominio opcional]"
---

Prepara la publicación de: $ARGUMENTS (si está vacío, usa el proyecto actual).

Usa la skill `publicar-github-vercel`.

1. **Pre-vuelo (sin efectos externos).** Ejecuta build local, revisa `.gitignore`, busca claves o `.env` versionados (reporta solo archivo y línea, nunca el valor), lista las variables de entorno necesarias (solo nombres) y comprueba móvil y rutas. Si procede, pide una pasada del agente `auditor-qa-web`.
2. **Resumen para confirmar.** Muestra: repo a crear o actualizar y su visibilidad (privado por defecto), proyecto de Vercel, variables que habrá que cargar, dominio (y si implica una compra, el costo según la cotización oficial) y el último commit.
3. **Pide confirmación explícita al usuario y espera un "sí" claro.** No ejecutes push, creación de repo, despliegue, cambio de DNS ni compra de dominio antes. Una confirmación vale solo para lo listado.
4. Tras el "sí": crea o actualiza el repo, haz push, despliega en Vercel y pide al usuario cargar las variables de entorno (no pegues ni pidas valores de claves en el chat).
5. **Verifica producción:** URL, formulario, imágenes, rutas, móvil y consola. Si falla, lee logs y propón la corrección antes de redesplegar.
6. Entrega: URL, estado, pendientes (dominio, analítica, SEO) y cómo volver atrás (rollback desde la lista de deployments).
