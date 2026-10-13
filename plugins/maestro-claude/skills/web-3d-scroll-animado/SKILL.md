---
name: web-3d-scroll-animado
description: Usar para webs con hero impactante - animación ligada al scroll (imagen inicial, final y video de transición) o un asset 3D (Spline). Gatillos - "hero animado", "scroll animation", "web 3D", "Spline", "start/end frame", "video en scroll".
---

# Web 3D y hero con scroll animado

## Objetivo
Crear un hero memorable (transición antes/después o asset 3D) sin sacrificar velocidad, móvil ni claridad del mensaje. El hero es el activo principal: merece más iteración que el resto.

## Pasos
1. **Propósito y marca.** Define qué debe comunicar el hero (servicio: gancho, propuesta, prueba, CTA; producto: qué lo diferencia). Extrae paleta, tipografía y logo de la marca. Mira 3-5 competidores para evitar clichés.
2. **Variante A, scroll por frames.** (a) Genera la imagen inicial 16:9 en 2K o más, fondo muy oscuro o blanco limpio para fundirse con la web, con logo y producto como referencia; 4 iteraciones. (b) Usa esa imagen como referencia para la versión final ("antes/después" o "exploded"). (c) Con ambas como start/end frame genera un video corto (5-8 s, sin audio) en un generador de video; itera 2-3 veces. (d) Convierte el video a secuencia de frames o úsalo con control por scroll.
3. **Variante B, asset 3D.** Elige un asset de Spline (Community), remix, edita, exporta (code export; pregunta a Claude qué formato conviene). Integra a pantalla completa en un solo viewport del hero.
4. **Construcción.** Crea la landing con el hero vacío, luego integra el asset o los frames en `images/` o `assets/` y refiérelos por ruta. Una idea y una acción por sección.
5. **Rendimiento.** Comprime video e imágenes, carga diferida fuera del primer viewport, `prefers-reduced-motion` respetado, fallback estático.
6. **Móvil.** Versión cuadrada o vertical del asset y un breakpoint propio; prueba en dispositivo real o emulado.
7. **Componentes extra** (Magic UI, 21st.dev) con moderación; después `seo-multipagina-auditoria` y publicar.

## Prompts de ejemplo
- "Escribe tres prompts: imagen inicial (estado 'antes'), imagen final (estado 'después') con la misma cámara y fondo, y prompt de transición para start/end frame de 6 s."
- "Integra el video en el hero con efecto ligado al scroll: avanza al bajar y retrocede al subir. Fondo blanco, texto legible, fallback con imagen estática y compresión del peso."
- "Integra el asset de Spline a pantalla completa en el hero; mide el peso y propón una versión ligera para móvil."

## Errores comunes
- Resolución baja (1K se ve amateur) o fondos que no combinan con la web.
- Varios elementos protagonistas en el mismo viewport.
- Video pesado que hunde la velocidad; sin versión móvil.
- Usar marcas o personajes de terceros como material propio sin permiso.

## Vigencia
Generadores de imagen y video (Nano Banana, Kling, Veo, etc.), Spline y sus planes cambian rápido; verifica modelos y costes. Cifras de precio o ventas citadas por el creador: no verificado.

## Checklist de salida
- [ ] Imágenes en 2K o más con fondo coherente con la web.
- [ ] Video corto comprimido y con fallback estático.
- [ ] `prefers-reduced-motion` respetado.
- [ ] Versión móvil probada en dispositivo real o emulado.
- [ ] Un solo elemento protagonista por viewport.
- [ ] Activos con derechos claros (sin marcas ajenas).
