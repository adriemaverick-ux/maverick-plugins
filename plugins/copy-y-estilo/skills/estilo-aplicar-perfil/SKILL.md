---
name: estilo-aplicar-perfil
description: Úsala cuando haya que escribir una pieza (mensaje, guion, caption, propuesta) siguiendo un perfil de estilo ya definido. Gatillos - "escribe con mi perfil", "en mi voz", "apply style profile", "write in this voice".
---

# Escribir con un perfil de estilo

## Objetivo
Producir un borrador que suene a la persona o marca del perfil, con datos reales, y pasarlo por un bucle corto de revisión antes de entregarlo.

## Pasos
1. Cargar el perfil desde la bóveda (`Perfiles de estilo`). Si no hay uno, usar `perfiles-iniciales` y avisar que es provisional.
2. Armar el prompt con cuatro bloques: perfil, 3 a 5 ejemplos dorados variados (canal, longitud, tema), brief de la pieza y restricciones.
3. Escribir las restricciones en positivo: qué hacer. Ejemplo: "empieza con la situación del dueño" en vez de "no empieces con presentaciones". Explicar el porqué mejora el cumplimiento.
4. Añadir una lista corta de léxico prohibido (máximo 10 a 15 términos, con alternativa al lado).
5. Pedir mismo estilo con contenido nuevo: no reutilizar frases de los ejemplos.
6. Los datos y pruebas los pone la persona. Si falta uno, el borrador lleva `[DATO PENDIENTE]`. Nunca inventar cifras, clientes ni garantías.
7. Bucle de revisión: (a) borrador; (b) auditoría contra perfil y `antiia-en-espanol`, listando cada incumplimiento con su línea; (c) reescribir solo esas líneas; (d) lectura humana de datos, promesas y tono. Si sale en cámara, leerlo en voz alta.
8. Si la pieza sale buena, sumarla a los ejemplos dorados con fecha, cuidando no sobreajustar a un solo tema.

## Plantilla de prompt
```
<rol>Eres el redactor de [marca/persona]. Escribes en español de Perú para [público].</rol>
<perfil_de_estilo>[pegar]</perfil_de_estilo>
<examples>
  <example canal="..." por_que_funciona="...">[texto real]</example>
  <no_asi>[versión genérica y por qué falla]</no_asi>
</examples>
<brief>Objetivo / quién lee y qué sabe ya / dato verificable / un solo siguiente paso / canal y longitud</brief>
<instrucciones>Borrador con las reglas del perfil. Luego audítalo y entrega la versión corregida.</instrucciones>
```

## Léxico prohibido de arranque (ajustar por perfil)
lead, pipeline, onboarding, dashboard, "solución integral", "garantizado", "estimado cliente", "no dude en contactarnos", "en el mundo actual". Alternativas en `../../references/glosario-icp.md`.

## Errores comunes
- Deriva a tono neutro a mitad de pieza: repetir dos reglas medibles al final del prompt.
- Caricatura: exagerar muletillas y localismos. Poner topes (un localismo por pieza).
- Muchas prohibiciones: un experimento aislado sugiere que prohibir estructuras lógicas destruye contrastes útiles; preferir instrucciones positivas y limpieza posterior.
- Ejemplos todos del mismo tema: la pieza copia el contenido, no el estilo.
- Dar por terminado sin revisión humana de cifras y promesas.

## Nivel de evidencia
- Few-shot supera a zero-shot; de 2 a 10 ejemplos aporta poco más; lo informal se imita peor [estudio con limitaciones, arXiv 2509.14543].
- Anthropic recomienda 3 a 5 ejemplos, etiquetas XML y decir qué hacer en vez de qué no hacer [consenso en fuente primaria; revisar la guía del modelo vigente].
- Efecto de restricciones negativas: [un experimento, no concluyente].
- Umbral de calidad y número de iteraciones: [mi criterio].

## Fuente
Informe 01, secciones 4.1 a 4.4 y 9. Regla del dueño: nada de cifras sin respaldo.

## Vigencia
2026-10-12
