---
name: gestion-claves-entorno
description: Guarda API keys y tokens en variables de entorno o gestores seguros, nunca en el chat ni en archivos versionados. Úsalo cuando debas añadir una clave a un agente, skill o MCP; gatillos - API key, token, secreto, variable de entorno, .env, rotar clave, límite de gasto.
---

# Gestión de claves en variables de entorno

## Objetivo
Que ninguna credencial pase por el chat, el historial, los skills ni los repositorios. El chat se registra y a veces se respalda; una clave pegada ahí debe considerarse expuesta. Este skill nunca pide ni muestra valores: guía el procedimiento.

## Pasos
1. **Pregunta por el mecanismo, no por el valor**: pide al agente "dame el comando de terminal para guardar esta clave como variable de entorno" y ejecútalo tú en tu terminal, pegando la clave solo ahí.
2. **Dónde guardar**: variables de entorno del sistema o del servicio, archivo `.env` local con permisos restringidos, o gestor de contraseñas. En los dashboards de agentes, usa el campo de variables de entorno, no el chat.
3. **El código/skill lee el nombre, no el valor**: en el skill escribe `NOMBRE_DE_VARIABLE`; documenta cómo obtener la clave en el proveedor, sin incluirla.
4. **Excluye del control de versiones**: añade `.env` y archivos de claves a `.gitignore` antes del primer commit; los respaldos en repos privados tampoco deben llevar secretos.
5. **Mínimo alcance**: crea claves con permisos limitados (solo lectura si basta) y una clave por proyecto.
6. **Límites de gasto**: configura tope semanal o mensual en el proveedor del modelo y en agregadores; así una fuga o un bucle no vacía la cuenta.
7. **Rotación**: rota claves periódicamente y tras cualquier sospecha; revoca las antiguas. Si una clave llegó a un chat, revócala y genera otra.
8. **Recarga**: tras cambiar una variable, reinicia o recarga el servicio/MCP para que la tome.
9. **Verifica sin revelar**: prueba con una llamada simple y comprueba que funciona; nunca imprimas la variable.

## Prompts de ejemplo
- "Necesito añadir la clave de [servicio] para tu skill. No me pidas la clave. Dame el comando de terminal para guardarla como variable de entorno llamada [NOMBRE] y cómo comprobar que existe sin mostrarla."
- "Revisa este proyecto y dime si hay claves, tokens o contraseñas escritas en archivos, skills o historial. Lista solo ubicaciones, no los valores, y propón cómo moverlas."
- "Prepara un `.gitignore` y un `.env.example` con los nombres de variables que usa el proyecto, sin valores."

## Errores comunes
- Pegar la clave en el chat "solo esta vez".
- Subir `.env` a un repositorio, incluso privado.
- Una sola clave con permisos totales para todo.
- No poner tope de gasto: un error puede costar mucho.
- Compartir un skill o plugin con la clave incrustada.
- Olvidar revocar claves de pruebas o de servicios que ya no usas.
- Dar a un agente acceso a tu gestor de contraseñas o a archivos de claves por defecto.

## Vigencia
Las prácticas son estables; las interfaces de cada proveedor (dónde se crean claves, cómo se ponen topes) cambian. Verifica en la documentación vigente del servicio.

## Checklist de verificación
- [ ] Ninguna clave aparece en el chat, skills o archivos versionados.
- [ ] .env está en .gitignore y existe un .env.example sin valores.
- [ ] Cada clave tiene alcance mínimo y tope de gasto.
- [ ] Sabes cómo rotar y revocar cada una.
- [ ] Probaste que funciona sin imprimir el valor.
