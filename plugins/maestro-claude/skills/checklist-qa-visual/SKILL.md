---
name: checklist-qa-visual
description: Checklist de QA visual y funcional antes de entregar un diseño, web o app: cinco revisores especializados, glance test, móvil, accesibilidad, SEO y seguridad. Usar con "revisar diseño", "QA", "auditar", "antes de entregar", "accesibilidad", "responsive" o "glance test".
---

# Checklist de QA visual

## Objetivo
Aprobar solo lo que pasa una revisión sistemática. Un diseño se entrega cuando todos los revisores aprueban, no cuando "se ve bien".

## Pasos
1. Reúne el entregable real renderizado (URL local o export) y el brief, el design system y la referencia.
2. Revisor 1, fidelidad visual: espaciado, alineación, jerarquía, interlineado, desbordes de texto, consistencia con la referencia.
3. Revisor 2, claridad y simplicidad: glance test (¿se entiende en 3-5 segundos?), una idea por pantalla, un CTA, baja densidad de texto. Genera varias versiones y quédate con la más simple.
4. Revisor 3, móvil y accesibilidad: prueba en 390 px y en teléfono real, tamaño táctil de objetivos, contraste, orden de foco por teclado, texto alternativo, movimiento reducido.
5. Revisor 4, copy: pasa por anti-slop, sin placeholders ni cifras sin fuente, tono de marca.
6. Revisor 5, marca y sistema: solo tokens permitidos, una sola familia de iconos, licencias de fuentes y assets anotadas.
7. Rendimiento y SEO: peso de imágenes y video, velocidad de carga, títulos, meta, encabezados, formularios funcionales.
8. Si hay backend: sesión nueva y limpia para auditoría de seguridad desde la óptica de un usuario externo; segunda revisión cruzada en otra sesión; confirma RLS y que no hay claves en el código.
9. Prueba flujos con un agente de navegador o a mano: entrar, completar acción clave, verificar el resultado final.
10. Consolida hallazgos por severidad y responsable, corrige y vuelve a pasar a los revisores que fallaron.
11. Aprueba solo con todos en verde y guarda el informe.

## Prompts de ejemplo
- "Actúa como cinco revisores independientes (fidelidad visual, claridad, móvil y accesibilidad, copy, marca). Cada uno entrega hallazgos con severidad y evidencia; no corrijas hasta que yo apruebe la lista."
- "Haz glance test de esta pantalla: ¿qué entiende un visitante en 5 segundos? Si no es la oferta principal, propón dos versiones más simples."
- "Revisa este código como un atacante externo sin acceso: lista vulnerabilidades, secretos expuestos y tablas sin protección, con orden de prioridad."

## Errores comunes
- Dejar que el mismo contexto que construyó revise todo.
- Revisar solo en escritorio.
- Aprobar por captura sin ver interacción.
- Olvidar contraste, foco de teclado y movimiento reducido.
- Entregar con licencias o placeholders pendientes.

## Vigencia
Criterios de accesibilidad (por ejemplo WCAG) y herramientas de QA con agentes evolucionan; confirma versión de la norma y límites de planes de las herramientas. Para clientes complejos, considera un experto humano en seguridad.

## Criterios de salida
- Informe con hallazgos por severidad y responsable.
- Todos los revisores en verde tras la última corrección.
- Pruebas en móvil real y flujo clave verificadas.
- Evidencia (capturas o medidas) adjunta a cada hallazgo cerrado.
