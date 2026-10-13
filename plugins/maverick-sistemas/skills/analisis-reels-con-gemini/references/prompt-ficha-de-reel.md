# Prompt para Gemini: ficha de análisis de un Reel

Copia todo lo que está debajo de la línea y pégalo **después** del video (la documentación de Gemini recomienda poner el texto tras el video).

---
Eres analista de edición de video corto. Mira el video completo (imagen y audio) y devuelve **solo un JSON válido**, sin texto antes ni después, con la estructura de abajo.

Reglas:
- Usa tiempos en formato MM:SS (con decimales si hace falta, por ejemplo 00:03.5).
- Describe lo que **observas**. Si algo es una deducción tuya, márcalo con el prefijo "(inferido)". No inventes: si no puedes determinar un dato, escribe null.
- Sé literal con el texto en pantalla y con lo que se dice (en el idioma original), **excepto** en `sistema_de_guion.plantilla_reutilizable`, que debe ser una plantilla abstracta con huecos, sin copiar las frases originales.
- **Este video es una grabación de pantalla SIN AUDIO.** No describas música, efectos de sonido ni voz: escribe null en todo el bloque `sonido` y en `texto_hablado`. Lo que se dice se deduce SOLO de los subtítulos visibles en pantalla; si no hay subtítulos, null. No inventes cierres ni llamados a la acción que no se vean escritos.
- **La grabación puede empezar con una pantalla de carga o con el final del video anterior y el Reel puede repetirse en bucle.** Analiza UNA sola pasada completa del Reel (desde que empieza el contenido) y pon en `reel.duracion_s` la duración de esa pasada.
- Cuenta los cortes con cuidado y di si el muestreo pudo perder cortes muy rápidos en "incertidumbres".

{
  "reel": {"duracion_s": 0, "formato": "talking_head | pantalla_dividida | b_roll_animado | grabacion_de_pantalla | mixto", "idioma": "", "tema": ""},
  "hook": {
    "t_inicio": "00:00", "t_fin": "00:03",
    "tipo": "curiosidad | contraste | promesa | error_comun | historia | demostracion | pregunta | dato | si_eres_X | polemica | prueba | otro",
    "texto_hablado": "", "texto_en_pantalla": "", "accion_visual": "",
    "promesa_implicita": "", "tiempo_hasta_primer_beneficio_s": 0
  },
  "beats": [
    {"t_inicio": "", "t_fin": "", "que_se_dice": "", "que_se_ve": "", "tipo_plano": "primer_plano | plano_medio | detalle | pantalla | grafico | otro", "movimiento_o_zoom": ""}
  ],
  "cortes": {"total": 0, "cortes_por_10s": 0, "duracion_media_plano_s": 0, "ritmo": "lento | medio | rapido"},
  "texto_en_pantalla": [
    {"t": "", "texto": "", "estilo": "subtitulo_palabra_por_palabra | titulo_cinetico | etiqueta | cifra_destacada | otro",
     "posicion": "", "animacion_entrada": "", "animacion_salida": "", "color_y_fuente": "", "palabra_resaltada": ""}
  ],
  "overlays_graficos": [
    {"t_inicio": "", "t_fin": "", "tipo": "tarjeta | diagrama_de_flujo | mockup_de_chat | contador | icono | lista | calendario | otro",
     "cobertura": "pantalla_completa | parcial | dividida", "elementos": "", "animacion": "", "relacion_con_lo_que_dice": ""}
  ],
  "transiciones": [{"t": "", "tipo": ""}],
  "sonido": {
    "musica": {"hay": false, "genero_o_energia": "", "volumen_relativo_a_la_voz": ""},
    "efectos": [{"t": "", "tipo": "whoosh | pop | click | impacto | riser | otro", "sincronizado_con": ""}],
    "voz": {"ritmo": "", "tono": ""}
  },
  "look": {"paleta": "", "contraste": "", "fondo": "", "grano_o_efecto": "", "encuadre_de_la_cara": ""},
  "retencion": {"rompe_patron": [{"t": "", "recurso": ""}], "bucle_abierto": "", "cierre": {"t": "", "cta": "", "tipo": ""}},
  "sistema_de_guion": {
    "formula_del_hook": "la fórmula abstracta con huecos, por ejemplo: [error común] + [a quién le pasa] + [consecuencia concreta]",
    "esqueleto_del_guion": ["beat 1: ...", "beat 2: ...", "beat 3: ..."],
    "palabras_totales_aprox": 0, "palabras_por_minuto_aprox": 0, "longitud_media_de_oracion_palabras": 0,
    "tipo_de_prueba": "demostracion | caso | dato | autoridad | ninguna",
    "bucle_abierto_y_cuando_se_cierra": "",
    "cierre_y_llamado_a_la_accion": {"tipo": "palabra_clave_en_comentarios | enlace_en_bio | dm | seguir | otro", "texto": ""},
    "tono_y_registro": "", "recursos_retoricos": ["contraste", "pregunta", "lista", "historia"],
    "plantilla_reutilizable": "el guion completo con huecos [ ], sin las palabras originales del creador"
  },
  "valoracion": {"fortalezas": [""], "debilidades": [""], "que_copiaria_como_tecnica": [""], "que_no_copiaria": [""]},
  "incertidumbres": [""]
}
