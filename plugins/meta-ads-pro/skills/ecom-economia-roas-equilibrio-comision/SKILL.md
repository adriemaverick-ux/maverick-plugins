---
name: ecom-economia-roas-equilibrio-comision
description: Úsala para calcular margen de contribución, ROAS y CPA de equilibrio, y cómo la comisión sobre margen bruto cambia el equilibrio, excluyendo Adelanto y Falabella. Gatillos - "ROAS de equilibrio", "break-even ROAS", "margen de contribución", "comisión", "MER", "CPA máximo".
---

# Economía: ROAS de equilibrio y comisión

## Objetivo
Saber cuánto puede costar una venta antes de pautar, con el margen de contribución real (no el margen bruto) y con la comisión incluida como costo de adquisición.

## Pasos
1. Definir las variables como marcadores y pedirlas al usuario; no inventarlas: P = precio;
   C = costo real puesto en Lima (importación + flete); pas% = pasarela; env = envío asumido;
   dev% = devoluciones previstas; otros%.
2. Margen de contribución: MC = 1 - (COGS% + pas% + env% + dev% + otros%) [un experto, fuentes consistentes].
3. ROAS de equilibrio = 1 / MC. ROAS objetivo = 1 / (MC - margen deseado) [un experto].
4. CPA de equilibrio = contribución en moneda de la primera venta = P x MC. ROAS eq. = P / CPA eq.
5. Comisión sobre margen bruto: Com = c% x (P - C), con c% definido en el contrato (marcador [c%]).
   Para el dueño, costo de publicidad = gasto en Meta + comisión. MC tras comisión = MC - Com/P.
6. Ejemplo ILUSTRATIVO (no benchmark;
   cifras del informe): P = S/ 5.000, C = S/ 3.000, pasarela 3,5% (S/ 175), envío asumido S/ 250, devolución prevista S/ 250.
   Contribución = 5.000 - 3.000 - 175 - 250 - 250 = S/ 1.325 -> MC 26,5% -> ROAS eq. 3,77.
   Con un margen bruto de 40% el ROAS ingenuo sería 2,5: se subestima el equilibrio ~50% [un experto, ejemplo].
7. Con comisión ilustrativa de 15%: margen bruto S/ 2.000 -> Com = S/ 300 (6% del ingreso) -> MC 20,5% -> ROAS eq. 4,9.
   CPA de equilibrio = S/ 1.325 - 300 = S/ 1.025.
8. Casa Soyer: el markup x3 implica margen bruto ~67% del precio;
   el 40% mencionado es el EBITDA del negocio, no la base de comisión [Casa Soyer, nota 2026-09-20].
   Pregunta abierta: si el costo incluye flete y aduana; en sofás pesados cambia el margen real.
   El costo cargado en Shopify está vacío o es erróneo (87% vacío en muestra): usar el costo real que den Ana/Marbe.
9. Exclusiones de la comisión (acordar por escrito): líneas "Adelanto" (proyectos de Studio Soyer cobrados por Shopify) y ventas del canal Falabella;
   tampoco cuentan en el MER de pauta. Piezas sin costo cargado se marcan, no se asumen con 100% de margen.
10. Devoluciones y anulaciones descuentan la comisión;
   definir qué ventas son "generadas por pauta" (ventana, UTM, etiqueta CRM) [marco propio, sin estándar [no verificado]].
11. MER = ingresos totales (sin Adelanto/Falabella) / gasto total en publicidad. Revisar contribución por sol de pauta = MER x MC.

## Plantillas / prompts
- Prompt: "Con P=[..], C=[..], pas%=[..], env=[..], dev%=[..], c%=[..], calcula MC, ROAS eq., CPA eq. y ROAS eq.
   con comisión. Excluye Adelanto y Falabella. Marca los costos faltantes."
- Tabla: pieza | P | C | MC | ROAS eq. | CPA eq. | comisión.

## Errores comunes
1. Usar margen bruto como si fuera contribución.
2. Mezclar ROAS de ingresos y de margen entre casos ajenos (EZ Living 13,5-52,5 vs 6,5-30 según ventana) [caso].
3. Incluir Adelanto en ventas de pauta (84% de $51.058 en 90 días no eran catálogo).
4. Mezclar soles y USD (tienda en USD): incluir tipo de cambio si la cuenta de Meta cobra en otra moneda.
5. Comisión sin piso de margen por pieza: incentiva volumen de bajo margen.

## Nivel de evidencia
- Fórmulas: [un experto, fuentes consistentes]. Ejemplo numérico: ilustrativo.
   Devoluciones de mueble ~22,7% [benchmark, Eightx secundario]; usar tasa propia.
- Marco de comisión: criterio propio [no verificado].

## Vigencia
2026-10-11. Los porcentajes de comisión y costos los define y aprueba el usuario/dueños.
