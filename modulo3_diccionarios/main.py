# Análisis de ventas por región
# Definir ventas_por_región como dict anidado { region: { Q1, Q2, Q3, Q4 } }
ventas_por_region = {
    "Norte": {"Q1": 12000, "Q2": 13500, "Q3": 14200, "Q4": 15800},
    "Sur": {"Q1": 9800, "Q2": 10400, "Q3": 11200, "Q4": 11900},
    "Este": {"Q1": 15200, "Q2": 14800, "Q3": 16300, "Q4": 17100},
    "Oeste": {"Q1": 8700, "Q2": 9100, "Q3": 9500, "Q4": 10200},
}

print("=== REPORTE DE VENTAS POR REGIÓN ===\n")

# Calcular el total anual de cada región con items() y sum(values())
totales_anuales = {}
for region, trimestres in ventas_por_region.items():
    total = sum(trimestres.values())
    totales_anuales[region] = total
    print(f"Ventas totales en {region}: ${total:,.2f}")

# Usar max() con key=lambda para la región con mayores ventas
region_max = max(totales_anuales.items(), key=lambda x: x[1])
print(f"\nRegión con mayores ventas: {region_max[0]} (${region_max[1]:,.2f})")

# Acumular ventas por trimestre con iteración anidada
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
for region, trimestres in ventas_por_region.items():
    for trimestre, venta in trimestres.items():
        totales_por_trimestre[trimestre] += venta

# Calcular gran_total
gran_total = sum(totales_anuales.values())

# Generar porcentajes con dict comprehension sobre el gran total
porcentajes = {trim: (venta / gran_total) * 100 for trim, venta in totales_por_trimestre.items()}

print("\n--- Ventas por Trimestre ---")
for trimestre in ["Q1", "Q2", "Q3", "Q4"]:
    print(f"{trimestre}: ${totales_por_trimestre[trimestre]:,.2f} ({porcentajes[trimestre]:.1f}%)")

# Imprimir reporte ordenado de mayor a menor con sorted() + items()
print("\n--- Ranking de Regiones (mayor a menor ventas) ---")
regiones_ordenadas = sorted(totales_anuales.items(), key=lambda x: x[1], reverse=True)
for i, (region, total) in enumerate(regiones_ordenadas, 1):
    porcentaje = (total / gran_total) * 100
    print(f"{i}. {region}: ${total:,.2f} ({porcentaje:.1f}%)")
