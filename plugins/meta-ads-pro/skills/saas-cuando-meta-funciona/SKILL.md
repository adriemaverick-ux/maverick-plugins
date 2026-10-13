---
name: saas-cuando-meta-funciona
description: Decide si Meta Ads encaja con un SaaS y cómo repartir entre Meta, Google, LinkedIn y TikTok. Usar cuando pregunten "¿Meta sirve para mi SaaS?", "Meta vs Google vs LinkedIn", "does Meta work for SaaS", "channel mix", "dónde invertir primero".
---

# SaaS: cuándo funciona Meta (matriz de canales)

## Objetivo
Dar un veredicto razonado sobre si Meta es canal principal, complemento o descarte para un SaaS concreto, sin vender humo. Aviso previo: no existe benchmark independiente de "Meta Ads para SaaS"; casi todo viene de agencias con interés comercial y se contradicen entre sí. Para Perú no hay cifras de CPL/CAC de SaaS publicadas; el dato real saldrá de la cuenta propia.

## Pasos
1. **Clasificar el producto** (pedir datos, no suponer): consumo/prosumer, SMB pequeño autoservicio, B2B mid-market, B2B enterprise, dev tools.
2. **Aplicar la matriz de segmento** [un experto]:
   - Consumo/prosumer (creadores, freelancers, estudiantes): Meta como canal principal probable.
   - SMB muy pequeño (ticket < USD 50/mes, autoservicio): bueno si el CAC se mantiene bajo; churn SMB 3-7% mensual acota el LTV [benchmark vía tercero].
   - B2B mid-market (ACV USD 10-50k): complemento (demanda + retargeting); ciclo largo y comité de compra.
   - B2B enterprise (ACV > USD 100k): pobre como canal de leads; útil para retargeting por cuentas.
   - Dev tools/nicho técnico: mejor Google/YouTube/comunidad; Meta solo retargeting.
3. **Aplicar la matriz de canales** [un experto, cifras de agencias, globales]:
   - Meta: crea demanda, trial, retargeting. Es el CPL más bajo y el menos predictivo.
   - Google Search: captura intención ya formada (alguien busca la categoría). Reparto citado: Search 35-45%, retargeting Meta 15-25% en B2B [un experto: SaaS Hero].
   - LinkedIn: precisión de cargo/empresa, CPC mucho más alto; mejor para mid/enterprise.
   - TikTok: awareness, dev tools/consumo; sin CPL fiable [un experto, sin fuente primaria].
   - YouTube: mid-funnel con demo en video; una sola agencia afirma mejor calidad de lead [un experto].
4. **Pregunta de intención**: ¿la gente ya busca esta solución en Google? Si sí, Search primero; Meta si el mercado no sabe que necesita el producto.
5. **Pregunta de volumen**: Stackmatix dice que sobre ACV USD 100k las cuentas con menos de USD 50k/mes no dan volumen de conversión suficiente [un experto].
6. **Juzgar por CAC y payback en el CRM propio**, no por CPL.
7. **Veredicto en tres líneas**: rol de Meta (principal/complemento/descarte), canal alternativo, y qué dato propio lo confirmaría.

## Plantillas / prompts
```
Producto: __  Ticket mensual (S/ o USD): __  Segmento: __
¿Autoservicio o venta asistida?: __  ¿Hay búsqueda activa en Google?: __
Veredicto Meta: [principal | complemento | descarte]
Razón (matriz): __   Canal alterno: __   Dato propio que lo validaría: __
```

## Errores comunes
- Usar Meta para algo que se compra por búsqueda activa (ahí gana Google).
- Comparar canales por CPL; el CPL de Meta siempre se ve mejor.
- Tratar cifras de agencias (p. ej. CAC "USD 937 en Facebook") como benchmark; esa cifra es [no verificado] y se contradice con otras tablas del mismo autor.
- Asumir que los números de EE. UU. aplican a Perú.

## Nivel de evidencia
Débil en general. Matriz por segmento: [un experto]. Cifras por canal: [un experto]/[no verificado], de agencias. Reparto 35-45% / 15-25%: [un experto]. Ningún caso público verificable de SaaS B2B con CAC/LTV a escala. Perú: sin dato.

## Vigencia
2026-10-11. Revisar cuando haya datos propios de la cuenta o cambie el producto de segmentación de Meta.
