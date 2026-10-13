---
name: estructura-de-boveda
description: Dónde va cada tipo de nota en la bóveda de Obsidian (Maverick MP y Casa Soyer), cómo nombrarla y enlazarla. Usar antes de crear o mover una nota. Gatillos - "dónde guardo esto", "estructura de la bóveda", "carpeta", "naming", "frontmatter".
---

# Estructura de la bóveda

## Maverick MP (`~/Downloads/Maverick MP`)
- `00 - Inicio.md`: enfoque vigente y reglas. Fuente de verdad.
- `01 - Negocio/`: oferta, precios, propuestas.
- `02 - Mercado/`: nichos, competencia, investigación de mercado.
- `03 - Go-to-market/`: marca, contenido, canales, prospección, pipeline, registro de outreach.
- `99 - Archivo/`: trabajo histórico que ya no define el enfoque (por ejemplo "2026-10 Diseño y obra"). No reciclar sus mensajes.
- `AGENTS.md`, `Bitácora IA.md`, `GHL - Integracion privada.md` (esta última contiene secretos: ver `higiene-de-claves`).

## Casa Soyer (`~/Downloads/Casa Soyer`)
Notas del ecommerce: auditoría de Shopify, comisión, campañas, creativos, reportes.

## Dónde va lo que sale de una conversación
| Tipo | Destino |
|---|---|
| Investigación de mercado, plataformas, leyes | `02 - Mercado/` |
| Decisión de marca, contenido, canal | `03 - Go-to-market/` |
| Cambio de oferta o precio | `01 - Negocio/` |
| Resultado de un plugin o herramienta nueva | `03 - Go-to-market/` o nota "Herramientas" |
| Lo de Casa Soyer | bóveda Casa Soyer |
| Lo ya obsoleto | `99 - Archivo/` (mover solo si Adrie lo pide) |

## Convenciones
- Nombre: claro y con fecha cuando sea un registro (`Tema - AAAA-MM-DD`).
- Frontmatter: `creado_por: Claude | Codex | Dueño` y `actualizado: AAAA-MM-DD`.
- Enlaces con `[[wikilinks]]`; enlazar desde el índice del área.
- Una nota por tema; ampliar antes que duplicar.

## Errores comunes
- Guardar un hallazgo en la carpeta de archivo por costumbre.
- Crear una carpeta nueva cuando ya hay una adecuada.

## Vigencia
2026-10-11. Basado en la estructura actual de Maverick MP.
