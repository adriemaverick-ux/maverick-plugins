---
name: saas-peru-pagos-y-mercado
description: Contexto de pagos y mercado en Perú para vender SaaS: Yape/billeteras vs tarjeta, pasarelas, impuestos a servicios digitales, mypes y precios. Usar con "cobrar en Perú", "Yape suscripción", "Culqi Niubiz recurrente", "SaaS Perú", "pagos recurrentes Perú".
---

# SaaS: Perú, pagos y mercado

## Objetivo
Ajustar oferta, precio y cobro a cómo paga el mercado peruano, marcando lo que no está verificado. Nada aquí sustituye asesoría tributaria o contractual.

## Pasos
1. **Bancarización y tarjetas**: cuentas de adultos de 20% (2011) a 59% (2024), dinero móvil 42% (Findex 2025, vía tercero) [oficial vía tercero]. Crédito 13% de adultos y débito 36% (Findex 2021) [oficial, datos de 2021; no hallé el dato 2025].
2. **E-commerce por medio de pago** (1S 2026): billeteras 37,6%, débito 32,4%, crédito 27,9% del volumen; ticket promedio billetera S/ 50 vs crédito S/ 340; Yape 87% de las transacciones en billeteras [oficial/gremio, Capece; hay inconsistencias entre periodos].
3. **Implicancia de diseño**: no depender solo de tarjeta de crédito. Combinar débito, Yape recurrente y transferencia/PagoEfectivo; considerar facturación anual con descuento si el pago fallido es alto [cálculo propio, inferencia].
4. **Yape recurrente**: Canva permite autorizar cobro recurrente con Yape con una autorización inicial [oficial de Canva]. Si el SaaS propio puede hacerlo depende de la pasarela: [no verificado].
5. **Pasarelas**: Culqi soporta recurrentes por API (tokenización); Niubiz recurrente en algunos planes empresariales; comisiones citadas Culqi 3,99% + S/ 0,60 nacional y 4,99% + S/ 0,60 internacional; Niubiz 3,5-4,5% + IGV negociable [un experto, guías 2026]. Verificar tarifarios vigentes con cada proveedor.
6. **Tasa de rechazo en recurrentes**: sin dato. Medirla desde el primer mes.
7. **Impuestos**: D. Leg. 1623, servicios digitales de no domiciliados: RUC y IGV 18%, o percepción por el banco emisor desde 1-oct-2024; alcance inicial personas naturales [oficial/PE]. Confirmar con contador.
8. **Mercado**: 2.346.592 empresas formales al cierre de 2024, 99,1% mypes, Lima 43,8% [oficial, PRODUCE]; ComexPerú estima 801.134 mypes formales en 2025 con metodología distinta [benchmark/PE]. Facturación electrónica obligatoria para mypes desde junio 2022: software por obligación legal [oficial/PE]. ERP en 65% de medianas y grandes (2023) no aplica a mypes [benchmark/PE].
9. **Precio**: Fungies sugiere descuento PPP de 35-45% para Perú, referencia de tercero sin elasticidad local [un experto]. Precios en soles; ticket bajo reduce LTV, por tanto CAC objetivo más bajo (ver `saas-economia-cac-ltv-payback`).
10. **WhatsApp** como probable canal de cierre; la cifra de 80-89% de uso es de 2022-2023 [no verificado para 2026].
11. **Competidores**: Alegra y Siigo citan SEO, contenido y email; no hay prueba pública de su gasto en Meta [caso/un experto].

## Plantillas / prompts
```
Medios de cobro a ofrecer: [debito | tarjeta | Yape recurrente | transferencia | PagoEfectivo]
Plan mensual S/ __ | plan anual S/ __ (descuento __%)
Pasarela candidata: __  Comisión confirmada por escrito: [si/no]
Pendiente verificar: __
```

## Errores comunes
- Asumir que el público paga con tarjeta de crédito.
- Fijar precio en USD sin ver el ticket local de billetera (S/ 50 promedio).
- Dar por válidas las comisiones de blogs sin cotización.
- Ignorar IGV y facturación electrónica.

## Nivel de evidencia
Datos de Findex/PRODUCE/Capece: [oficial]/[oficial vía tercero]/[gremio] con inconsistencias señaladas. Pasarelas y PPP: [un experto]. Rechazo recurrente, Yape recurrente propio y uso de WhatsApp 2026: [no verificado] o sin dato.

## Vigencia
2026-10-11. Normativa y tarifas cambian; reverificar antes de decidir.

## Skills relacionados
- `saas-economia-cac-ltv-payback`: ajustar LTV y CAC objetivo al ticket en soles.
- `saas-escala-y-techos`: techo de audiencia en Perú y expansión regional.
- `saas-embudos`: WhatsApp como destino y canal de cierre.
