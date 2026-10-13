---
name: agentic-os-planificador-obrero-critico
description: Monta un Agentic OS (panel local con contexto, memoria, skills, costes y revisión nocturna) y usa el patrón planificador-obrero-crítico para decisiones e investigación profunda. Úsalo para unificar tus agentes o para tareas largas que necesitan verificación; gatillos - Agentic OS, mission control, dreaming, triad, planner worker critic, /goal.
---

# Agentic OS + patrón planificador-obrero-crítico

## Objetivo
Tener una vista única de lo que hacen tus agentes (Claude Code, Cowork, otros) y un patrón de trabajo donde un modelo planifica, otro ejecuta barato y otro critica. Principio: el OS solo vale si actúa, no solo si responde; y "no puedes mejorar lo que no puedes ver".

## Parte A: Agentic OS (versión mínima)
1. **Perfil**: entrevista para generar un documento de negocio y uno de vida (metas mensuales/trimestrales, valor de tu hora para estimar ROI).
2. **Reutiliza conexiones** ya hechas; no reconfigures cada herramienta.
3. **Un panel local** (localhost) con: gasto por plataforma, skills y su uso, tareas programadas, memoria, objetivos y documentos que genera el agente (para que no se pierdan en el chat).
4. **Dreaming / revisión nocturna** (1-2 veces al día, modelo barato): analiza 7 días de conversaciones; detecta tareas manuales repetidas 3+ veces para proponer skill; coste (Opus en trabajo simple, mala caché); skills sin uso; memoria obsoleta; entrega máximo 4 recomendaciones con ROI estimado.
5. **Añade funciones con "intención declarada"**: qué debe ser verdad al final; pide que confirme que entendió, que haga preguntas y que muestre un mockup en localhost antes de construir.
6. **Objetivos con contrato de finalización**: objetivo medible + cómo verificar + restricciones + límites de carpeta/permisos, acotado (~20 turnos); para metas de semanas, divide en mini-objetivos marcando cuáles son de IA y cuáles requieren a un humano.

## Parte B: planificador-obrero-crítico
1. **Planificador** (modelo frontier): interroga con 5-10 preguntas, define criterio de éxito y escribe el brief.
2. **Obrero** (modelo barato): ejecuta volumen (35 ángulos, investigación, borradores); puede correr horas.
3. **Crítico** (modelo de OTRA familia): "crítica brutal" hasta que sea publicable; no debe ser el mismo que planificó.
4. **Planificador valida** y sintetiza, explicando qué aportó cada rol.
5. Estima coste antes de iterar y pide aprobación si pasa un umbral.
6. Verifica siempre lo que produjo el modelo barato: es trabajador, no jefe.

## Prompts de ejemplo
- "Actúa como planificador. Interrógame con hasta 8 preguntas sobre [decisión], escribe un brief con criterio de éxito y estima el coste. Espera mi aprobación antes de lanzar al obrero."
- "Objetivo: [resultado medible]. Verificación: [cómo comprobarlo]. Restricciones: [lista]. Límites: solo la carpeta X, sin enviar ni publicar nada. Trabaja hasta 20 turnos y demuéstrame con evidencia que se cumplió."
- "Revisa mis chats de los últimos 7 días y propón máx. 4 mejoras: skills a crear, gasto innecesario en modelos caros y memorias obsoletas. Incluye ROI estimado como suposición, no como dato."

## Errores comunes
- Mismo modelo como planificador y crítico: confirma sus propios sesgos.
- Objetivos sin métrica ("hazme crecer"): nunca terminan.
- Dar al agente permisos amplios mientras duermes; usa aprobaciones y límites.
- Construir un panel gigante antes de tener datos; empieza por gasto y skills.
- Confiar en cifras de ahorro del panel sin contrastarlas.

## Vigencia
Basado en videos de may-sep 2026 sobre paneles propios y agentes de terceros; `/goal` y el dreaming nativo eran funciones recientes (preview). Cifras de ahorro y ROI de la fuente: no verificado.

## Checklist de verificación
- [ ] Cada objetivo tiene métrica y verificación.
- [ ] El crítico es de otra familia de modelos que el planificador.
- [ ] Hay aprobación humana antes de gasto o efectos externos.
- [ ] El panel muestra gasto y skills antes que adornos.
