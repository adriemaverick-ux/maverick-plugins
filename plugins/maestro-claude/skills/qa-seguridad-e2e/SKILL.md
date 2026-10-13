---
name: qa-seguridad-e2e
description: Usar antes de publicar o entregar una web o app, para probar de punta a punta y revisar seguridad con contexto limpio. Gatillos - "QA", "probar la web", "E2E", "revisión de seguridad", "checklist de lanzamiento", "pre-launch", "pruebas".
---

# QA y seguridad E2E

## Objetivo
Detectar fallos funcionales, visuales y de seguridad antes de que los vea un usuario, con revisiones independientes: quien construye no debería ser el único que audita.

## Pasos
1. **Lista de casos.** Pide a Claude 10 casos de uso reales (visitante, registro, login, formulario, compra de prueba, error de red, móvil). Cada caso con resultado esperado verificable.
2. **Pruebas E2E en navegador.** Usa un agente de navegador (Playwright vía MCP, la extensión de Chrome u otra herramienta de QA con lenguaje natural): URL, pasos y una aserción final. Prueba en móvil y escritorio; repite tras cada corrección. Si la herramienta es de pago, valora el costo-beneficio.
3. **Bucle de autocorrección.** Cada fallo: captura o log al agente, corrección, nueva prueba. Para errores de producción, consola del navegador y logs de build/runtime.
4. **Revisión de seguridad con contexto limpio.** Abre una sesión nueva y pide revisar la app como un atacante externo sin acceso: autenticación, RLS/permisos, inyección, XSS, exposición de claves, CORS, validación de formularios, rate limiting, dependencias vulnerables.
5. **Segunda revisión cruzada** en otra sesión o con otro modelo/CLI de revisión: pega el informe de la primera y pide encontrar lo que falte. Para clientes con datos sensibles, suma un experto humano.
6. **Secretos.** Busca claves en el repo y su historial; rota las expuestas; confirma que todo vive en variables de entorno y que `.env` no está versionado.
7. **Datos.** Verifica RLS probando con dos usuarios distintos; confirma que un usuario normal no lee ni edita datos ajenos.
8. **Checklist final:** accesibilidad básica, velocidad, enlaces rotos, formularios entregan a CRM, pagos solo en modo prueba, copias de seguridad, plan de rollback.
9. Registra resultados en `findings.md` y publica solo con visto bueno del usuario.

## Prompts de ejemplo
- "Propón 10 casos de prueba end-to-end para esta app con resultado esperado. Luego ejecútalos en el navegador uno por uno y reporta capturas de los fallos."
- "Nueva sesión: revisa esta app como un atacante externo sin cuenta. Lista vulnerabilidades por severidad, ruta afectada y corrección sugerida."
- "Busca claves o tokens en el código y en el historial de git y dime cuáles hay que rotar."

## Errores comunes
- Probar solo el camino feliz y solo en escritorio.
- Pegar claves reales en prompts o reportes de prueba.
- Fiarse de una sola revisión del mismo modelo que escribió el código.
- Declarar "seguro" sin pruebas: el resultado es una revisión, no una garantía.

## Vigencia
Herramientas de QA con IA y revisores de código de pago cambian de nombre y precio; verifica. Límites de uso de terceros citados por el creador: no verificado.

## Checklist de salida
- [ ] 10 casos E2E ejecutados en escritorio y móvil.
- [ ] Revisión de seguridad hecha en sesión de contexto limpio.
- [ ] Segunda revisión cruzada realizada.
- [ ] Secretos rotados si hubo exposición.
- [ ] RLS verificado con usuarios distintos.
- [ ] Hallazgos y veredicto registrados en `findings.md`.
