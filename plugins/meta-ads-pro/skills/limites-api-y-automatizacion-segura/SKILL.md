---
name: limites-api-y-automatizacion-segura
description: Usar al automatizar Meta Ads con IA, MCP o la Marketing API, para respetar límites de tasa y diseñar escrituras seguras con aprobación humana. Gatillos - "rate limit", "Marketing API", "automatizar con MCP", "System User", "throttling", "cambios de presupuesto por API".
---

# Límites de API y automatización segura

## Objetivo
Automatizar lectura y cambios sin provocar throttling, abuso de cuota ni acciones masivas descontroladas.

## Pasos numerados
1. Conocer niveles de acceso [oficial]: Limited (antes Standard) y Full (antes Advanced). Full requiere más de 500 llamadas en 15 días con error menor a 15 % en las últimas 500.
2. Conocer límites oficiales [oficial, con discrepancias entre páginas]: puntuación lectura 1 punto, escritura 3; Limited máx 60 con bloqueo de 300 s; Full máx 9000 con bloqueo de 60 s. BUC por hora: `ads_management` = (100 000 Full / 300 Limited) + 40 x anuncios activos; `ads_insights` = (190 000 Full / 600 Limited) + 400 x anuncios activos. Mutaciones: 100 QPS por app+cuenta. Spend cap: 10 cambios/día. Presupuesto de ad set: 4 cambios/hora con bloqueo de 1 h si se excede.
3. Leer cabeceras `X-Business-Use-Case`, `X-Ad-Account-Usage`, `X-FB-Ads-Insights-Throttle`; confiar en las de tu cuenta ante cifras distintas. Códigos de throttling típicos: 17, 613, 4, 80000/80003/80004/80014.
4. Crear un System User con permisos mínimos; token en gestor de secretos con rotación. No usar el login de un usuario personal compartido con el bot.
5. Modo por defecto solo lectura. Escrituras (pausar, presupuesto, crear anuncios) detrás de aprobación humana.
6. Fijar en tu propio código topes de cambios por hora/día por debajo de los límites de Meta; backoff exponencial; sin acciones masivas simultáneas (duplicar cientos de anuncios, mover todos los presupuestos a la vez).
7. Registrar cada escritura (quién, qué, cuándo, valor previo y nuevo).
8. Todo contenido generado con IA pasa por revisión de políticas (salud, finanzas, claims) antes de publicarse; no usar IA para fabricar testimonios o resultados.
9. Datos de conversiones: ver `pixel-y-capi-setup`; el token de CAPI también va en secretos.

## Checklists
- [ ] System User con permisos mínimos y token rotado.
- [ ] Solo lectura por defecto; aprobación humana para escribir.
- [ ] Topes propios y backoff.
- [ ] Log de cada escritura.
- [ ] Revisión de políticas del contenido generado.

## Errores comunes
- Ráfagas de escrituras que provocan throttling; Meta puede reducir temporalmente la cuota ante tráfico anómalo [oficial].
- Cambiar presupuesto de ad set más de 4 veces por hora o spend cap más de 10 veces al día.
- Token de un usuario real embebido en scripts.
- Ignorar cabeceras de uso.

## Ejemplo de política de aprobación
- Lectura de insights: automática.
- Pausar un anuncio: requiere visto bueno humano.
- Cambios de presupuesto o creación de anuncios: aprobación humana y registro en log.

## Nivel de evidencia
- [oficial] Cifras de rate limiting citadas (Marketing API Rate Limiting), reducción de cuota por abuso.
- [analista] Reglas de seguridad de automatización (criterio propio, sin cifras de Meta).
- [no verificado] Mínimo de llamadas de Full Access en WhatsApp (500 vs 1 500); cifras BUC/Score varían según la versión de la página.

## Vigencia
2026-10-11.
