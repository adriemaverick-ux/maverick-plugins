---
name: estructura-de-cuenta-y-campanas
description: Diseña o corrige la estructura de cuenta de Meta Ads (campañas, conjuntos, anuncios, objetivos, CBO/ABO, amplio vs intereses). Usar cuando se pida "estructura de campañas", "account structure", "cuántos ad sets", "ABO vs CBO", "consolidar cuenta" o armar una cuenta desde cero.
---

# Estructura de cuenta y campañas

## Objetivo
Proponer una estructura consolidada que concentre señal, separe testeo de escala y no fragmente presupuesto.

## Pasos
1. **Elegir objetivo por campaña** entre los seis ODAX: Reconocimiento, Tráfico, Interacción, Clientes potenciales, Promoción de app, Ventas. Una campaña, un objetivo. Catálogo se conecta dentro de Ventas. [analista]
2. **Evento de optimización alineado al negocio** (compra si hay volumen). Si el evento es muy raro y aparece "aprendizaje limitado", subir a un evento más alto del embudo o consolidar. [analista]
3. **Consolidar.** Pocas campañas, pocos conjuntos, targeting amplio, varios creativos por conjunto. Regla de CTC: si hay más de 3-4 campañas y ninguna llega a 20+ conversiones/semana, consolidar. [consenso para consolidar; umbral: un experto]
4. **Separar testeo y escala**: una campaña/conjunto de testeo aparte y una de escala (Advantage+ sales o presupuesto de campaña, broad, ventana 7 días clic). [consenso]
5. **Presupuesto**: CBO se llama ahora "Advantage+ campaign budget"; apagarlo equivale a ABO. No mezclar presupuesto de campaña y de conjunto. [analista] Qué usar para testear es debate abierto (ver `testeo-y-escalado`). [un experto en cada postura]
6. **Audiencia**: Advantage+ audience y placements activados salvo razón fuerte. Audiencias originales obligatorias en categorías especiales. [analista]
7. **Agrupar anuncios por concepto o persona, no por formato.** [un experto: Manchi/Kruse]
8. **Clientes existentes**: usar la Customer Lifecycle Strategy (recomienda excluir clientes en adquisición) o dos conjuntos (nuevos/existentes), porque ya no existe el Existing Customer Budget Cap. [oficial / un experto: Loomer; verificar en Business Help]
9. **Retargeting**: pools pequeños rara vez ganan subastas; reparto sugerido por agencias (60-80% amplio, 10-20% retargeting, 5-10% test) no coincide entre fuentes. Validar con holdout. [no verificado]
10. **Señales**: Pixel + CAPI; EMQ de 7/10 o más; en CTWA devolver eventos con `ctwa_clid`. [un experto / analista]

## Plantillas / prompts
Esquema base (ajustar al negocio):
```
Campaña ESCALA (Ventas, presupuesto de campaña, 7d clic)
  Conjunto A: Advantage+ audience, placements Advantage+
    anuncios agrupados por concepto/persona
Campaña TEST (Ventas, ABO o CBO según decisión)
  Conjunto T1: conceptos nuevos distintos
```
Prompt: "Con estos datos (objetivo, evento, conversiones/semana, nº de campañas y conjuntos actuales) propón la estructura consolidada y lista qué fusionar o apagar. No ejecutes cambios: dame el plan para aprobación."

## Errores comunes
- Muchos conjuntos con poco presupuesto que no llegan a ~50 eventos/semana. [consenso]
- Mezclar testeo y escala en la misma campaña. [consenso]
- Separar conjuntos por formato. [un experto]
- Conjuntos con intereses retirados que dejan de entregar. [no verificado, verificar]
- Editar a diario: agrupar cambios en una edición semanal.

## Nivel de evidencia
Consolidar y separar test/escala: [consenso]. Estructura de CTC (evergreen vs momentos, 150 anuncios): [un experto]. Nombres y flujo Advantage+: [analista]. Repartos porcentuales: [no verificado]. Umbral de 25 conversiones: [no verificado]; usar 50/semana como referencia.

## Vigencia
2026-10-11. La unificación Advantage+ y los controles de placement cambian rápido; confirmar en la interfaz actual.
