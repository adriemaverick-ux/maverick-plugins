---
name: prosp-registro-anti-duplicados
description: Úsalo al preparar una tanda, cuando Adrie dice "manda nuevos", o al actualizar estados de contacto, para no repetir mensajes a empresas ya contactadas. Gatillos: "manda nuevos", "nueva tanda", "ya le escribí", "evitar duplicados", "dedupe outreach log".
---

# Registro anti-duplicados

## Objetivo
Mantener una sola fuente de verdad de quién fue contactado, quién está pendiente y quién respondió, para no escribir dos veces al mismo negocio y no confundir un mensaje preparado con uno enviado.

## Pasos
1. Localizar el registro de outreach (nota "Registro de outreach - talleres automotrices" en la bóveda) y leerlo completo antes de proponer nada. Si hay un pool en CSV sincronizado, revisarlo también.
2. Aplicar la regla de Adrie: cuando dice **"manda nuevos"**, todo lo de la tanda anterior se considera **ya enviado**. Pasar esos contactos de "Pendiente de envío" a "Enviado" con la fecha del día y la nota "por regla acordada".
3. La tanda recién preparada queda como **Pendiente de envío**. Una tanda preparada no equivale a enviada: un enlace precargado no prueba entrega, respuesta ni interés.
4. Para cada candidato nuevo, comparar por nombre normalizado (sin mayúsculas, tildes ni razón social), teléfono normalizado y dominio. Si coincide con cualquier estado (Enviado, Pendiente, Referencia de trabajo previo, Propuesta enviada, No contactar), descartarlo.
5. Respetar estados especiales: clientes o trabajo previo no se tratan como prospecto nuevo; quien pidió no contacto no se vuelve a escribir.
6. Al registrar, guardar solo lo necesario: nombre, estado, fecha, ángulo, fuente de verificación. No pegar conversaciones completas.
7. Si un contacto responde, cambiar el estado y anotar la respuesta textual breve (ver `prosp-separar-respuestas-humanas-de-bots`).
8. Si Adrie confirma que algo no se envió, corregir a Pendiente o Descartado; la confirmación humana manda sobre la regla.
9. Informar al final: cuántos pasaron a Enviado por regla, cuántos quedan Pendiente, cuántos candidatos se descartaron por duplicado.

## Plantillas
Estados válidos: Pendiente de envío · Enviado · Respuesta automática · Respondió (humano) · Propuesta enviada · Referencia de trabajo previo · No contactar · Descartado (motivo).

```
| Negocio | Estado | Fecha | Ángulo | Verificado en (fuente) | Nota |
```

Resumen de cierre de tanda:
```
Pasaron a Enviado por regla "manda nuevos": N
Nueva tanda Pendiente de envío: N (ángulos: ...)
Descartados por duplicado: N
```

## Errores comunes
- Dar por enviada una tanda solo porque se preparó.
- Comparar solo por nombre: una misma empresa aparece con variantes de nombre o con dos números.
- Proponer registros marcados como contactados o pendientes porque estaban en un pool viejo.
- Tratar una respuesta automática como interés humano.
- Escribir teléfonos o datos personales en notas que se van a compartir.

## Nivel de evidencia
- Regla "manda nuevos" y estados: [decisión de Adrie, 2026-10-10].
- Que "Enviado por regla" equivale a entrega real: [no verificado]; es un supuesto operativo.

## Fuente
Registro de outreach (estructura y reglas, sin copiar contactos) y decisiones consolidadas (2026-10-10).

## Vigencia
2026-10-11.
