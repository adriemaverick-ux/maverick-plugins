---
name: enrutar-modelos-y-comite
description: Reparte el trabajo entre modelos por tarea (barato por defecto, potente solo para decidir) y usa un comité de modelos para preguntas estratégicas. Úsalo para reducir coste o evitar sesgo de un solo modelo; gatillos - elegir modelo, enrutar, OpenRouter, comité de expertos, mixture of agents, costes de tokens, Opus vs Sonnet.
---

# Enrutar modelos y comité de modelos

## Objetivo
Pagar el modelo caro solo donde su juicio cambia el resultado. Patrón: **comprimir, juzgar, ejecutar**. Cambia el motor, conserva el coche: el entorno (Claude Code, Cowork) se mantiene y el modelo se intercambia.

## Pasos
1. **Clasifica la tarea**: volumen/investigación, ejecución, diseño/gusto, decisión estratégica, revisión.
2. **Mapa de modelos** (documento reutilizable): modelo ligero para volumen y tareas de fondo; modelo medio para ejecución; modelo potente para planificar, arquitectura, estrategia y revisión final. Usa cuatro variables: rendimiento, velocidad, privacidad y coste.
3. **Comprime antes de escalar**: el modelo barato junta y resume en un brief corto; el potente recibe solo el brief.
4. **Disparadores para el modelo potente**: decisión de diseño/arquitectura, estrategia, revisión crítica, "codificar" una regla. Si no hay disparador, no se usa.
5. **Estimación y aprobación**: antes de llamar al caro, estima tokens y coste y pide tu visto bueno.
6. **Verifica** la salida barata con una muestra revisada por un modelo mejor o por ti.
7. **Controles de gasto**: límite mensual en el proveedor, fallback si se agotan tokens, iteraciones máximas, esfuerzo bajo para explorar y alto solo en builds.
8. **Comité (opcional)**: un agregador potente + 3 modelos de referencia de familias distintas responden el mismo prompt en paralelo con tope de tokens; el agregador sintetiza e indica qué aportó cada uno. Solo para preguntas donde un punto ciego cuesta caro.
9. **Privacidad**: antes de enviar datos a un modelo, decide si pueden salir; para lo sensible usa un modelo local o ninguno.
10. Revisa el mapa cuando salga un modelo nuevo: los benchmarks de la fuente cambian cada pocas semanas.

## Prompts de ejemplo
- "Crea un documento `mapa-modelos.md` con 5 tipos de tarea, el nivel de modelo recomendado para cada una, el disparador para escalar y un tope de gasto por tarea. Marca los precios como 'no verificado' hasta que los confirme."
- "Para esta pregunta estratégica: [pregunta]. Primero comprime el contexto en un brief de 300 palabras con un modelo ligero; luego dime cuánto costaría pasarlo al modelo potente y espera mi OK."
- "Convoca un comité: tres perspectivas independientes y distintas, límite 800 tokens cada una; luego sintetiza coincidencias, discrepancias y qué haría yo, explicando de dónde sale cada punto."

## Errores comunes
- Usar el modelo más caro por defecto "para estar seguros".
- Creer que "gratis" o barato equivale a calidad: verifica.
- Mismo modelo como ejecutor y revisor.
- Comité para preguntas triviales: multiplica el coste.
- Enviar datos sensibles a proveedores sin revisar su política.
- Fijarse en un solo benchmark de marketing en vez de probar con tu tarea real.

## Vigencia
Basado en videos de feb-sep 2026 con modelos de distintos proveedores; nombres, precios, límites y políticas de acceso cambian rápido. Todas las comparaciones de coste o rendimiento de la fuente: no verificado.

## Checklist de verificación
- [ ] Existe un mapa tarea-modelo con disparadores para escalar.
- [ ] Hay tope de gasto y fallback configurados.
- [ ] La salida del modelo barato se verifica por muestreo.
- [ ] Revisaste qué datos pueden salir a cada proveedor.
- [ ] Las cifras de precio están marcadas como no verificadas hasta confirmarlas.
