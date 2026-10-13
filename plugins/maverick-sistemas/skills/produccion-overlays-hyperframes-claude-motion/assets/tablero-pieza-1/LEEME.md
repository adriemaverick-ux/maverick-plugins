# Tablero estático de la pieza 1 (Formato C)

Pizarra digital larga y **estática** (sin animación) de 1080 px de ancho y 7 pantallas de 800 px, con una línea de hilo a la izquierda. Adrie **desliza mientras explica**.
- `tablero.html` (usa `?rubro=plagas`, `?rubro=refrigeración`, etc.): se exporta a imagen larga (1080×5600) con Chrome en modo headless.
- `visor-pieza1.html`: escenario 1080×1920 con la ventana de la pizarra (y 480 a 1280) desplazable con el trackpad y la burbuja de cara marcada arriba a la derecha; se graba la pantalla mientras se desliza.
Cambiar textos y secciones editando el HTML; una pantalla por idea.

**Teclas del visor:** flecha abajo, barra espaciadora o Re Pág pasan **una pantalla** (800 px) con desplazamiento suave; flecha arriba vuelve una; Inicio regresa al comienzo. El trackpad también funciona y se ajusta a cada pantalla.

**Estudio todo en uno (`estudio-pieza1.html`, recomendado):** se abre en Chrome, tiene el guion por pantalla al lado (no se graba), la cámara en la burbuja redonda y un botón de grabar. Pide cámara, micrófono y compartir la pestaña; al detener descarga el video 9:16 con pizarra, cara y voz. Si el recorte de la pestaña no es compatible, graba la pestaña completa y se recorta en CapCut. No requiere instalar nada.
