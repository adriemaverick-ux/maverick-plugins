---
name: publicar-github-vercel
description: Usar para llevar una web a internet con repositorio GitHub y despliegue en Vercel, con dominio, variables de entorno, analítica y rollback. Gatillos - "publicar", "deploy", "subir a Vercel", "GitHub", "dominio", "poner online", "404 en producción".
---

# Publicar con GitHub + Vercel

## Objetivo
Dejar el sitio online con despliegue continuo: cada push a GitHub redespliega solo. Siempre con la confirmación explícita del usuario antes de desplegar.

## Pasos
1. **Pre-vuelo.** Corre build local, revisa móvil y consola, confirma que no hay claves en el código ni en `.env` versionado (`.gitignore` correcto). Pide a Claude: "voy a hospedar en Vercel, comprueba que el código está listo".
2. **Repositorio.** Crea el repo (privado por defecto) con GitHub CLI (`gh auth login`, código de un solo uso en el navegador) o desde la web, y haz commit y push. Haz commits frecuentes como puntos de guardado.
3. **Vercel.** Add New > Project > importar el repo > Deploy (plan gratuito para empezar). Next.js, Vite y similares se detectan solos. Si la web es HTML estático, la raíz debe tener `index.html`.
4. **Variables de entorno** en Vercel (Settings > Environment Variables), por entorno; después redespliega. Nunca en el código.
5. **Verifica la URL de producción:** formulario, imágenes, rutas y móvil. Si sale 404/401 o pantalla en blanco: inspecciona la consola del navegador, copia el error al agente y revisa los logs de build.
6. **Dominio.** Vercel > Domains: compra o conecta uno, asígnalo al proyecto y configura redirección permanente al dominio principal.
7. **Analítica.** Activa Web Analytics y Speed Insights, instala el paquete y el componente según las instrucciones y haz push.
8. **Ciclo de cambios.** Editar en local -> probar -> commit y push -> Vercel redespliega. Rollback desde la lista de deployments si algo sale mal.
9. Con MCP de Vercel: activa solo las herramientas necesarias (decenas de tools consumen contexto) y usa un token de caducidad corta.

## Prompts de ejemplo
- "Revisa que el proyecto esté listo para Vercel (build, rutas, variables, .gitignore) y dime qué falta. No hagas push todavía."
- "Crea un repo privado, sube el proyecto y prepara el deploy; antes de desplegar muéstrame el resumen y espera mi confirmación."
- "El deploy da 404 en /blog. Lee los logs de build, revisa la consola y propón la corrección."

## Errores comunes
- Subir `.env` o claves a un repo público.
- Publicar directo desde un builder online y obtener pantalla negra por dependencias.
- Olvidar las imágenes en el repo (no cargan en producción).
- Desplegar sin que el usuario lo haya confirmado.

## Vigencia
Planes y límites gratuitos de Vercel (analítica, vistas, historial) y precios de dominios cambian; verifica. Los comandos de CLI y menús pueden variar; consulta la documentación vigente.

## Checklist de salida
- [ ] Confirmación explícita del usuario antes de desplegar.
- [ ] `.gitignore` correcto y sin secretos en el historial.
- [ ] Variables de entorno cargadas en Vercel y redeploy hecho.
- [ ] Producción revisada: rutas, imágenes, formulario, móvil.
- [ ] Dominio con redirección permanente al principal.
- [ ] Analítica activa y rollback conocido.
