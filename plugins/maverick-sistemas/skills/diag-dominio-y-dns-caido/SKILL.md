---
name: diag-dominio-y-dns-caido
description: Diagnóstico de un dominio o web que no abre (NXDOMAIN, dominio sin registrar, dominio registrado con DNS sin zona) con host, dig y WHOIS, qué significa cada resultado y cómo se arregla. Usar cuando la web de un prospecto o cliente no carga. Gatillos - "web caída", "no abre", "DNS", "dominio", "NXDOMAIN", "whois".
---

# Diagnóstico de dominio y DNS caído

Caso trabajado: `spectank.pe` (Spektank Perú), 2026-10-13. No tocar el DNS ni el dominio de nadie sin permiso del titular y de Adrie.

## Pasos
1. **Escritura exacta del dominio:** probar variantes (con y sin letra repetida, `.com`, `.pe`, `.com.pe`); en el caso real, `specktank.pe` no existía y `spectank.pe` sí.
2. `host dominio` y `dig NS dominio` (y contra un servidor público, por ejemplo `@8.8.8.8`) para separar un problema local de uno global.
3. **WHOIS por extensión:** `.pe` → `whois -h kero.yachay.pe dominio.pe`; `.com` → `whois -h whois.verisign-grs.com "domain dominio.com"`. "No match" o "No Object Found" = **no registrado**.
4. Si está registrado: titular, contacto administrativo y **servidores de nombres**. Consultar directamente a esos servidores (`dig A dominio @ns1...`): si responden **NXDOMAIN**, **no tienen zona** para el dominio.

## Interpretación
- **No registrado:** venció, nunca existió con ese nombre o está en otra dirección; riesgo de que otro lo registre; se registra **a nombre del dueño**.
- **Registrado, NS de estacionamiento (ej. `dns-parking.com`) sin registros:** hosting vencido, cambio sin actualizar el DNS o zona borrada; se arregla quien tenga el acceso al dominio (a menudo la agencia que lo montó): decidir el hosting, apuntar el DNS y reconstruir la web.

## Preguntas al dueño
¿Qué dirección usaban? ¿Quién la hizo y quién paga dominio y hosting? ¿Quién tiene el acceso? ¿Usan correos con ese dominio? ¿Tienen ficha de Google y redes?
