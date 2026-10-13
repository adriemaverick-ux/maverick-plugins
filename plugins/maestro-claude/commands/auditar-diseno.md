---
description: Audita el diseño de una web, app o pieza (slop, brechas contra una referencia, móvil, accesibilidad, copy) y entrega un informe priorizado.
argument-hint: <URL o ruta del diseño> [URL de referencia]
---

Usa el subagente `disenador-claude-design` para auditar este diseño: $ARGUMENTS

Flujo a seguir:
1. Obtener el entregable (URL pública o archivos locales) y, si se indicó, la referencia.
2. Aplicar `anti-ai-slop-tipografia-copy-color`: inventario de señales por categoría.
3. Si hay referencia, aplicar `extraer-adn-diseno` y producir el informe de brechas con valores lado a lado y las 3 correcciones de mayor impacto.
4. Aplicar `checklist-qa-visual` con revisores independientes: fidelidad visual, claridad (glance test), móvil y accesibilidad, copy, marca.
5. Entregar informe con hallazgos por severidad, evidencia y correcciones concretas, más un plan de cambios ordenado por impacto.

No modifiques el diseño sin confirmación del usuario. No pidas claves; las cifras de terceros van como "no verificado".
