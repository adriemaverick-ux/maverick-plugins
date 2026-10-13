---
name: higiene-de-claves
description: Auditar y ordenar tokens, claves y contraseñas en notas, archivos y repositorios - encontrarlos sin mostrarlos, moverlos a un gestor de secretos o variables de entorno, y rotar los expuestos. Usar al sospechar de claves en texto plano, antes de sincronizar la bóveda, o cuando Adrie diga "claves", "token", "seguridad", "rotar". Gatillos - "higiene de claves", "secretos", "rotar token", "API keys".
---

# Higiene de claves

## Objetivo
Que ningún secreto viva en texto plano en la bóveda, en el código ni en un repositorio, y que lo expuesto se rote.

## Casos conocidos (2026-10-11)
- La nota `GHL - Integracion privada.md` de la bóveda Maverick MP guarda un token privado y un Location ID de GHL en texto plano.
- La carpeta `~/Downloads/Rescate Migracion/Claves API/` contiene claves de la cuenta anterior (Anthropic, Apify, Cloudflare, GitHub, Vercel, Twilio, Kapso, Sperant, Supabase, `.env`). Pueden estar vencidas, rotadas o vigentes; no se sabe.

## Pasos
1. **Inventario sin exponer valores**: buscar patrones (por ejemplo prefijos conocidos de tokens, `.env`, "token", "api_key", "password") en la bóveda y carpetas indicadas. Reportar solo **archivo, línea y tipo**; nunca imprimir el valor.
2. **Clasificar** cada hallazgo: vigente / probablemente vencido / desconocido / ejemplo falso.
3. **Probar vigencia solo con permiso de Adrie**: hacer una llamada de solo lectura a la API correspondiente cuesta una petición y usa la clave; pedir confirmación antes y no registrar la respuesta completa.
4. **Rotar** lo vigente y expuesto: generar una clave nueva en el panel del proveedor y revocar la vieja. Es lo único que realmente cierra el riesgo.
5. **Guardar las nuevas** en un gestor de contraseñas o secretos, o en variables de entorno / `.env` fuera de la bóveda y fuera de git.
6. **Limpiar la nota**: reemplazar el valor por "ver gestor de secretos: nombre del ítem".
7. **Revisar el historial**: si la bóveda es un repositorio git (por ejemplo con Obsidian Git), un token ya confirmado queda en el historial; rotar es obligatorio aunque se borre de la nota.
8. **Prevenir**: `.gitignore` para `.env` y `Claves API/`; el hook del plugin avisa si se intenta escribir un token.
9. Registrar el resultado **sin valores** en la bóveda.

## Qué NO hacer
- Pegar una clave en un chat, en una nota o en un mensaje a otro asistente.
- Guardar claves "temporalmente" en la bóveda.
- Dar por seguras las claves viejas del zip sin revisarlas.

## Errores comunes
- Borrar la clave de la nota pero no rotarla.
- Olvidar el historial de git.

## Vigencia
2026-10-11.
