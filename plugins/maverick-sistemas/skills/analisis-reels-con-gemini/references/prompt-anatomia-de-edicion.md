Eres un analista de edición de video corto. Te paso un Reel vertical de un creador de marketing, **ralentizado 4 veces** (un segundo real dura 4 segundos en lo que ves) para que se distingan las animaciones. **Reporta TODOS los tiempos en segundos del video que ves (ralentizado)**; yo los divido entre 4. El video **no tiene audio**: no inventes voz, música ni efectos; no transcribas nada hablado.

Tu trabajo es describir con precisión CÓMO está editado, para que alguien lo pueda reproducir. Sé concreto y numérico. Si algo no se puede determinar, escribe "no determinable" en vez de adivinar. No juzgues ni recomiendes.

Devuelve SOLO un JSON válido con esta estructura:
{
 "escenas": [
  {
   "n": 1, "t_inicio_s": 0.0, "t_fin_s": 0.0,
   "layout": "split | cara_completa | solo_grafico | otro",
   "titular": {"texto": "", "estilos_tipograficos": "", "palabra_de_acento_y_como_se_resalta": "", "entrada": {"tipo": "", "palabra_por_palabra": true, "duracion_total_s": 0.0}, "cambia_en_esta_escena": true},
   "grafico": {"descripcion": "", "tipo": "tarjeta|telefono|documento|cuadricula|diagrama|logotipo|pantalla_de_app|collage|otro", "fondo": "claro|oscuro", "imita_una_pantalla_real": true},
   "animaciones": [
     {"elemento": "", "tipo": "entrada con desenfoque|deslizamiento|escala|escritura letra por letra|contador numerico|trazo que se dibuja|aparicion escalonada|cambio de contenido|zoom o paneo|resaltado|otro", "t_inicio_s": 0.0, "duracion_s": 0.0, "detalle": ""}
   ],
   "cursor": {"presente": true, "comportamiento": ""},
   "transicion_de_salida": {"tipo": "", "duracion_s": 0.0}
  }
 ],
 "subtitulos": {"estilo": "", "palabras_por_segundo_aprox": 0.0, "como_entra_cada_palabra": "", "posicion_vertical_relativa": "", "color_y_peso_en_layout_split": "", "color_y_peso_en_cara_completa": ""},
 "cara": {"forma": "", "ancho_relativo_pct": 0, "alto_relativo_pct": 0, "posicion": "", "cambios_de_tamano": [{"t_s": 0.0, "pasa_a": "", "duracion_s": 0.0}], "elementos_extra": ""},
 "ritmo": {"duracion_total_video_s": 0.0, "numero_de_escenas": 0, "eventos_visuales_por_10_s": 0.0, "duracion_media_de_escena_s": 0.0, "porcentaje_tiempo_split": 0, "porcentaje_tiempo_cara_completa": 0},
 "paleta_y_tipografia": {"fondos": "", "color_de_acento": "", "tipografias": ""},
 "recursos_que_se_repiten": [""],
 "incertidumbres": [""]
}
