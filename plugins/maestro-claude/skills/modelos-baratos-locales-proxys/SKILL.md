---
name: modelos-baratos-locales-proxys
description: Usa modelos baratos, gratuitos o locales (OpenRouter, DeepSeek, Ollama, proxys) dentro o junto a Claude Code, con límites claros de privacidad y calidad. Úsalo para trabajo de volumen o respaldo. Triggers - OpenRouter, DeepSeek, Ollama, modelo local, proxy, claude code router, modelos gratis, cheaper model.
---

# Modelos baratos, locales y proxys

## Objetivo
Reducir coste en tareas repetitivas o privadas manteniendo el modelo fuerte para lo crítico, sin exponer datos ni claves.

## Pasos
1. Define qué va a cada lado. Regla orientativa 80/20: la mayoría de tareas rutinarias en modelo barato o local; lo difícil, el diseño con criterio, las decisiones y los datos de clientes en un modelo de confianza.
2. Elige la vía: (a) agregador de modelos (OpenRouter) con una clave por sistema, límite de gasto y caducidad; (b) API directa del proveedor del modelo barato (menos límites de tasa); (c) modelo local con Ollama para trabajo privado u offline; (d) proxy/router local que reparte según tarea.
3. Para local: indica a Claude tu hardware (captura de "Acerca de este equipo") y pide el modelo más grande que quepa dejando margen de RAM. Verifica contexto mínimo suficiente (decenas de miles de tokens) para el arnés.
4. Configura mediante los ajustes oficiales (variables de entorno o settings.json del proyecto, no global si puedes evitarlo). Antes de tocar nada, guarda copia y escribe el procedimiento de reversión.
5. Las claves: variable de entorno o gestor de secretos; nunca en el chat, nunca en el repo. Una clave dedicada con tope de gasto.
6. Verifica el modelo real consultando la configuración (/model, panel del proveedor); no te fíes de lo que el modelo diga de sí mismo.
7. Aplica límites de uso: no mandes a modelos de terceros datos personales, regulados, secretos, código propietario ni información de clientes salvo que sus términos lo permitan. Si no estás seguro, usa local o el modelo de confianza.
8. Revisa los resultados: modelos baratos alucinan más y fallan en tool use, skills/MCP y tareas multiarchivo. Haz que un modelo fuerte o un subagente revise lo importante.
9. Mide: tiempo y retrabajo cuentan; "gratis" no siempre sale más barato. Ten varias claves de respaldo porque los tiers gratuitos cambian.
10. Documenta en CLAUDE.md qué tareas van a qué modelo.

## Prompts de ejemplo
- "Según mi equipo (adjunto captura), recomiéndame el modelo local más grande que corra con margen y explícame cómo instalarlo con Ollama. No cambies ninguna configuración todavía."
- "Prepara la configuración para enrutar tareas de lint, tests y refactors repetitivos a un modelo barato vía OpenRouter, guardando primero copia de mi settings actual y el comando de reversión."
- "Revisa como segundo modelo este cambio hecho con un modelo barato y lista errores y alucinaciones."

## Errores comunes
- Enviar datos de clientes o secretos a un proveedor sin revisar sus términos.
- Pegar la clave en el chat.
- Usar el modelo barato para diseño desde cero o verificación de hechos.
- No guardar la reversión de la configuración.
- Esperar que skills y MCP funcionen igual con cualquier modelo.

## Checklist de cierre
- Reparto de tareas por modelo documentado.
- Clave dedicada con tope de gasto.
- Reversión de configuración guardada.
- Datos sensibles excluidos de terceros.

## Vigencia
- Nombres de modelos, variables de configuración, precios, promociones y tiers gratuitos cambian; todas las cifras de ahorro del creador: no verificado.
- Proxys y repos de terceros: aplica antes auditoria-repos-seguridad.
