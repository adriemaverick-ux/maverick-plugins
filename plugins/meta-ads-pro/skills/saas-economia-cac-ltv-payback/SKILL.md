---
name: saas-economia-cac-ltv-payback
description: Calcula LTV, CAC objetivo, CAC payback, CPL máximo y ROAS de equilibrio para una suscripción SaaS, con ejemplo numérico y marcadores. Usar con "CAC LTV SaaS", "payback", "ROAS de equilibrio suscripción", "cuánto puedo pagar por cliente", "unit economics".
---

# SaaS: economía (CAC, LTV, payback, ROAS de equilibrio)

## Objetivo
Fijar cuánto se puede pagar por cliente antes de abrir la cuenta de anuncios. Los números del dueño van en marcadores; nunca inventar ARPA, margen ni churn.

## Pasos
1. **Pedir datos**: ARPA mensual (P), margen bruto (m), churn mensual (c), tasa lead→cliente (t). Si faltan, marcarlos como pendientes.
2. **Fórmulas** [cálculo estándar; reglas de pulgar: un experto]:
   - LTV = P x m / c.
   - CAC objetivo ≈ LTV / 3 (regla 3:1, Skok); en negocios de creadores ≈ 1/6 del LTV (SaaSrise) [un experto].
   - Payback (meses) = CAC / (P x m).
   - CPL máximo = CAC objetivo x t (AdManage: USD 12.000 x 2% = USD 240) [un experto].
   - Churn anual = 1 - (1 - c)^12 (3% mensual ≈ 31%; 5% ≈ 46%).
3. **ROAS de equilibrio para suscripción**:
   - Primer mes (caja): ROAS_1 = P / CAC. Cubrir CAC en el primer cobro exige ROAS ≥ 1/m sobre esa factura, o prepago anual.
   - Sobre vida: ROAS_LTV = LTV / CAC; como este LTV ya incluye el margen bruto, el equilibrio económico es LTV:CAC = 1 (si el LTV se calculara con ingresos, sería LTV x margen = CAC). Escalar sano con LTV:CAC > 3.
4. **Ejemplo con marcadores** (del informe, [cálculo propio], no es dato de mercado): P = 30, m = 80%, c = 5% → LTV = 30 x 0,8 / 0,05 = 480; CAC objetivo a 3:1 = 160; payback = 160 / 24 = 6,7 meses; ROAS del primer mes = 30/160 = 0,19. Moneda: el informe usa USD; para Perú rehacer en soles con el ARPA real y recordar que ticket más bajo reduce LTV.
5. **Reglas de corte de referencia** [un experto]: escalar solo con payback < 12 meses y LTV:CAC > 3; pausar escala si payback > 12, LTV:CAC < 3 o costo marginal > CAC objetivo por 2 semanas. Payback por segmento citado: SMB 8-12 meses [un experto vía tercero].
6. **Un ROAS "de e-commerce" (2-4x) no aplica**: el de suscripción se mide en ventana larga o con planes anuales.
7. **Sensibilidad**: recalcular con churn el doble y ARPA -35/45% (descuento PPP sugerido por Fungies, [un experto]) para ver si el CAC objetivo sobrevive.
8. **No mezclar LTV orgánico con pagado**: el cliente de pago puede retener peor [un experto: SaaSrise].

## Plantillas / prompts
```
P=__  m=__%  c=__%/mes  t=__% (lead->cliente)
LTV = P*m/c = __     CAC obj = LTV/3 = __     Payback = CAC/(P*m) = __ meses
CPL max = CAC obj * t = __     ROAS_1 = P/CAC = __
Decisión: ¿payback < 12 y LTV:CAC > 3? -> si/no (supuestos listados)
```

## Errores comunes
- No definir CAC objetivo antes de escalar (caso SaaSrise: CAC USD 166 a USD 350-400 al subir gasto) [caso].
- Usar benchmarks (LTV:CAC mediano 4,1x, payback mediano 15 meses) como metas propias; son [benchmark vía tercero].
- Confundir CAC con costo por lead.
- Ignorar el churn de pago fallido en Perú (sin dato de tasa de rechazo).

## Nivel de evidencia
Fórmulas: [cálculo estándar]. Ejemplo: [cálculo propio]. Reglas 3:1 y payback < 12: [un experto]. Benchmarks de CAC: [benchmark vía tercero]/[no verificado]. Sin cifras de Perú.

## Vigencia
2026-10-11.
