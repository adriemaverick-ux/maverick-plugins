---
name: comision-margen
description: Calcula la comisión de Adrie sobre margen bruto de Casa Soyer por venta, por pieza y por periodo, aplicando exclusiones (Adelantos, Falabella) y marcando costos faltantes. Usar al evaluar rentabilidad de pauta, cerrar el mes o negociar el % de comisión.
---

# Comisión sobre margen bruto

## Fórmula
- Margen bruto = precio de venta − costo real (importación + logística hasta Lima).
- Con markup x3, margen ≈ 67% del precio. **Dato aproximado**: usar costo real cuando exista.
- Comisión = % pactado × margen bruto de ventas **elegibles**.

## Elegibles
- Incluye: ventas cerradas por Adrie / originadas por su pauta (tag de cierre).
- Excluye: line items "Adelanto…" (tags `EB01-2XX`), canal Falabella, ventas orgánicas no atribuibles (si así se pacta).

## Reglas
1. Si falta el costo o es mayor al precio → marcar "costo inválido" y NO inventar: pedir costo real a Ana/Marbe.
2. Nunca usar el EBITDA (40%) como base.
3. Mostrar siempre: venta, costo, margen, % pactado, comisión, y fila de excluidos con motivo.
4. Calcular también la rentabilidad de pauta: margen bruto − gasto en ads, por campaña.
5. Dejar explícito que el % pactado aún debe confirmarse por escrito.
