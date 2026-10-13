---
name: handoff-claude-design-a-code
description: Lleva un diseño de Claude Design (o Stitch, AI Studio, Open Design) a una app o sitio real en Claude Code, con localhost, GitHub y despliegue. Usar con "handoff", "pasar de Design a Code", "exportar zip", "abrir en localhost", "publicar en Vercel" o cuando se acaben los límites de Claude Design.
---

# Handoff Claude Design a Claude Code

## Objetivo
Cerrar el ciclo: la herramienta de diseño es el diseñador, Claude Code es el desarrollador. Convertir HTML exportado en un proyecto mantenible, verificado en local y publicado.

## Pasos
1. Congela el diseño: termina las iteraciones en Design (comentarios, ajustes en lienzo, tweaks) y confirma qué pantallas se exportan.
2. Exporta de la forma más fiable: Share > project HTML / project archive > descarga del zip. El comando de handoff directo a veces no trae todos los archivos (p. ej. video); si falta algo, usa el zip.
3. Usa la app de escritorio de Claude Code (pestaña Code), no la versión web, en una carpeta nueva y vacía.
4. Pide: "familiarízate con este export y ábrelo en localhost"; adjunta el zip y, aparte, el design system exportado.
5. Verifica en el navegador local: responsive, interacciones, fuentes, assets. Pide a Claude listar qué es HTML estático y qué conviene migrar.
6. Migra a un framework frontend cuando necesites animación compleja, rutas o estado; conserva los tokens del design system como fuente única.
7. Añade componentes puntuales (21st.dev, CodePen) pegando el código y diciendo dónde y con qué estilo adaptarlo.
8. Versiona: crea repo, haz commits frecuentes como puntos de guardado y publica en GitHub tras cada cambio relevante.
9. Despliega (p. ej. Vercel conectado a GitHub, redeploy automático). Las credenciales van por login interactivo o variables de entorno; nunca las pegues en archivos versionados ni en prompts reutilizables.
10. Si se agotan los límites, retoma con Open Design u otro CLI: revisa primero el repo con Claude antes de clonarlo o ejecutarlo; importa el zip y continúa con otro modelo.
11. Cierra con QA (ver checklist-qa-visual).

## Prompts de ejemplo
- "Abre este zip exportado de Claude Design, instala lo necesario y levántalo en localhost. Dime qué archivos son estáticos, qué falta y qué riesgos ves antes de migrarlo a un framework."
- "Convierte este HTML en un proyecto con componentes reutilizables y un archivo de tokens (color, tipo, espaciado) tomado del design system. No cambies el aspecto."
- "Crea repo, sube el proyecto y prepara el despliegue; indícame qué variables de entorno necesito definir yo, sin escribir valores secretos en el repositorio."

## Errores comunes
- Usar Claude Code web para el handoff.
- Confiar en el handoff por comando sin comprobar que llegaron videos o fuentes.
- Clonar repos recién creados sin revisarlos.
- Perder el design system al no exportarlo.
- Subir claves al repositorio.

## Vigencia
Menús (Share, Export, Handoff), límites de tamaño y la calidad de la integración Design-Code cambian por versión; Open Design es un proyecto joven que puede tener errores y no exporta a PowerPoint. Comprueba la UI actual.

## Criterios de salida
- El proyecto corre en localhost con todos los assets y fuentes.
- Repo creado, sin secretos versionados, con README mínimo de arranque.
- Despliegue probado y enlace compartido.
- El design system exportado queda archivado junto al código.
