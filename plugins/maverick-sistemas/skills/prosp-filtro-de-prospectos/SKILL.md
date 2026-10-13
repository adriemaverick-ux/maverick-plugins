---
name: prosp-filtro-de-prospectos
description: Úsalo para decidir si un taller, empresa de saneamiento o de mantenimiento técnico en Lima merece entrar a una tanda de contacto. Gatillos: "filtrar prospectos", "¿vale la pena este taller?", "armar lista", "prospect filter", "qualify lead before outreach".
---

# Filtro de prospectos

## Objetivo
Evitar escribir a negocios que no encajan (ficha de Maps sin operación real, números equivocados, capacidad de compra dudosa) y dejar por escrito qué señal real justificó cada contacto. Una ficha de Google Maps no demuestra encaje.

## Pasos
1. Confirmar que el negocio está operativo: servicios visibles, web o perfil activo, reseñas recientes, reservas, varias sedes, recepción o flotas. Anotar la señal y su origen (URL o directorio).
2. Priorizar talleres integrales o multimarca con presencia activa y capacidad de compra. No afirmar "multimarca" si la web no lo confirma; escribir "por confirmar".
3. Verificar el canal: que el número o contacto corresponda a la empresa y no a un particular. Si parece persona natural (negocio unipersonal), marcar riesgo de dato personal y ver `prosp-cumplimiento-peru-consentimiento`.
4. Cruzar contra el registro (`prosp-registro-anti-duplicados`): por nombre normalizado, teléfono y dominio. Si ya fue contactado, es referencia de trabajo previo o pidió no contacto, se descarta.
5. Registrar quién parece decidir (dueño, administración, recepción) solo si el dato es público y profesional. No compilar datos personales de más.
6. Clasificar: **Encaja** (señal verificada), **Por confirmar** (falta una señal), **Descartar** (con motivo: inactivo, duplicado, otro rubro, sin canal empresarial, no contacto).
7. Entregar la tanda de a pocos (hasta cinco por tanda, como en el uso actual), cada uno con un ángulo de diagnóstico distinto.
8. Si el taller ya muestra respuesta automática con menú de cotización, anotarlo: ya automatiza la recepción; no ofrecerle eso como novedad.
9. Guardar fuente y fecha de verificación de cada dato.

## Plantillas
Ficha mínima por prospecto (sin copiar datos de contacto a notas públicas):

```
Empresa:
Sector: taller / saneamiento / mantenimiento técnico
Distrito:
Señal de encaje (frase + URL):
Fuente y fecha de verificación:
Canal empresarial publicado: sí / no (no escribir el número aquí si la nota se comparte)
Posible decisor (cargo, no datos personales):
Capacidad de compra (indicios):
Riesgo legal (persona natural / dato personal): bajo / revisar
Resultado del filtro: Encaja / Por confirmar / Descartar (motivo)
Ángulo asignado:
```

## Errores comunes
- Asumir encaje porque aparece en Maps o tiene muchas reseñas.
- Mandar la misma ráfaga a varios números del mismo negocio.
- Contactar talleres cuyo cuello de botella es la capacidad (falta de mecánicos): no necesitan más demanda, quizá filtrar y ordenar solicitudes.
- Mezclar prospectos de otros nichos archivados (diseño y obra) sin reetiquetar.
- Reciclar sin revisar registros marcados como contactados o pendientes.

## Nivel de evidencia
- Criterios de filtro (operación real, multimarca confirmado, número verificado): [decisión de Adrie, 2026-10-10].
- Que un ángulo concreto convierta mejor: [hipótesis], sin ganador aún.
- Mínimo 20-30 contactos por variante antes de comparar: [recomendación de método], no estadística del mercado.

## Fuente
Decisiones consolidadas de la conversación (2026-10-10), nota de outbound a talleres (2026-10-09), nota de nichos activos, y metodología de depuración de listas del archivo histórico (solo el método, no sus mensajes).

## Vigencia
2026-10-11. Revisar cuando cambie el nicho prioritario o la regla de canal.
