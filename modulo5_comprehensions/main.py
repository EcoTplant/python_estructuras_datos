# Analizador de ventas con las 3 comprehensions

# Definir ventas con 6 productos (producto, unidades, precio, categoría)
ventas = [
    {"producto": "Laptop", "unidades": 15, "precio": 800, "categoria": "Electrónica"},
    {"producto": "Teclado", "unidades": 50, "precio": 25, "categoria": "Accesorios"},
    {"producto": "Mouse", "unidades": 100, "precio": 15, "categoria": "Accesorios"},
    {"producto": "Monitor", "unidades": 8, "precio": 350, "categoria": "Electrónica"},
    {"producto": "Silla", "unidades": 12, "precio": 120, "categoria": "Muebles"},
    {"producto": "Webcam", "unidades": 20, "precio": 60, "categoria": "Electrónica"},
]

print("=== ANALIZADOR DE VENTAS ===\n")

# List comp: valor_total (unidades * precio) por cada producto
valores_totales = [v["unidades"] * v["precio"] for v in ventas]
print("1. Valores totales por producto (unidades * precio):")
for i, val in enumerate(valores_totales):
    print(f"   {ventas[i]['producto']}: ${val:,.2f}")

# List comp con filtro: nombres de productos con valor_total > 1000
productos_destacados = [v["producto"] for v in ventas if v["unidades"] * v["precio"] > 1000]
print(f"\n2. Productos con valor total > 1000: {productos_destacados if productos_destacados else 'Ninguno'}")

# Dict comp: producto_info mapeando nombre → {valor, unidades}
producto_info = {
    v["producto"]: {"valor": v["unidades"] * v["precio"], "unidades": v["unidades"]}
    for v in ventas
}
print("\n3. Información por producto (valor total y unidades):")
for prod, info in producto_info.items():
    print(f"   {prod}: ${info['valor']:,.2f} ({info['unidades']} unidades)")

# Dict comp con filtro: ranking_premium (precio > 50), ordenado por valor desc
ranking_premium = {
    v["producto"]: v["unidades"] * v["precio"]
    for v in ventas
    if v["precio"] > 50
}
# Ordenar por valor descendente
ranking_ordenado = dict(sorted(ranking_premium.items(), key=lambda x: x[1], reverse=True))
print("\n4. Ranking de productos premium (precio > 50) ordenados por valor total:")
for prod, valor in ranking_ordenado.items():
    print(f"   {prod}: ${valor:,.2f}")

# Set comp: categorías_unicas y productos_baratos (precio ≤ 50)
categorias_unicas = {v["categoria"] for v in ventas}
productos_baratos = {v["producto"] for v in ventas if v["precio"] <= 50}
print(f"\n5. Categorías únicas: {categorias_unicas}")
print(f"   Productos baratos (precio ≤ 50): {productos_baratos if productos_baratos else 'Ninguno'}")

# Combina las tres: resumen_formateado + gran_total con sum()
# Resumen formateado usando dict comprehension filtrada (productos con valor > 500)
resumen_formateado = {
    v["producto"]: f"${v['unidades'] * v['precio']:,.2f} ({v['categoria']})"
    for v in ventas
    if v["unidades"] * v["precio"] > 500
}
gran_total = sum(valores_totales)

print("\n6. Resumen final (productos con valor > 500):")
for prod, detalle in resumen_formateado.items():
    print(f"   {prod}: {detalle}")
print(f"\n   Gran total de ventas: ${gran_total:,.2f}")