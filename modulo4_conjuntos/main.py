# Tiendas y recomendaciones de películas
# Combinación de análisis de catálogos con sets y operadores matemáticos

# Definir tienda_centro, tienda_norte y tienda_sur como sets de productos
tienda_centro = {"laptop", "tablet", "mouse", "teclado", "monitor"}
tienda_norte = {"mouse", "teclado", "auriculares", "webcam", "impresora"}
tienda_sur = {"tablet", "monitor", "impresora", "silla", "escritorio"}

print("=== ANÁLISIS DE CATÁLOGOS DE TIENDAS ===\n")

# Calcular catalogo_completo con union() y productos_comunes con intersection()
catalogo_completo = tienda_centro.union(tienda_norte, tienda_sur)
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

print(f"Catálogo completo (unión de las tres tiendas): {len(catalogo_completo)} productos")
print(f"Productos comunes en las tres tiendas: {productos_comunes if productos_comunes else 'Ninguno'}\n")

# Usar difference() para exclusivos de cada tienda e isdisjoint() para solapamientos
# Exclusivos de cada tienda: productos que solo están en esa tienda y no en las otras dos
exclusivos_centro = tienda_centro.difference(tienda_norte.union(tienda_sur))
exclusivos_norte = tienda_norte.difference(tienda_centro.union(tienda_sur))
exclusivos_sur = tienda_sur.difference(tienda_centro.union(tienda_norte))

print("Productos exclusivos por tienda:")
print(f"  Centro: {exclusivos_centro if exclusivos_centro else 'Ninguno'}")
print(f"  Norte:  {exclusivos_norte if exclusivos_norte else 'Ninguno'}")
print(f"  Sur:    {exclusivos_sur if exclusivos_sur else 'Ninguno'}")

# Verificar solapamientos (si comparten al menos un producto) con isdisjoint()
print("\nSolapamientos entre tiendas:")
print(f"  Centro y Norte comparten productos? -> {not tienda_centro.isdisjoint(tienda_norte)}")
print(f"  Centro y Sur comparten productos?  -> {not tienda_centro.isdisjoint(tienda_sur)}")
print(f"  Norte y Sur comparten productos?   -> {not tienda_norte.isdisjoint(tienda_sur)}")

# Definir usuario1, usuario2, usuario3 como sets de géneros cinematográficos
usuario1 = {"acción", "aventura", "ciencia ficción", "comedia"}
usuario2 = {"drama", "comedia", "romance", "documental"}
usuario3 = {"acción", "aventura", "fantasía", "terror"}

print("\n=== RECOMENDACIONES DE PELÍCULAS POR GÉNEROS ===\n")
print(f"Usuario 1: {usuario1}")
print(f"Usuario 2: {usuario2}")
print(f"Usuario 3: {usuario3}")

# Usar & | - ^ para comunes, universo, exclusivos y diferencias
comunes_1_2 = usuario1 & usuario2
comunes_1_3 = usuario1 & usuario3
comunes_2_3 = usuario2 & usuario3
universo_generos = usuario1 | usuario2 | usuario3
exclusivos_1 = usuario1 - usuario2 - usuario3
exclusivos_2 = usuario2 - usuario1 - usuario3
exclusivos_3 = usuario3 - usuario1 - usuario2
diff_simetrica_1_2 = usuario1 ^ usuario2  # géneros en uno pero no en el otro

print("\nAnálisis de intereses:")
print(f"  Géneros comunes entre usuario1 y usuario2: {comunes_1_2 if comunes_1_2 else 'Ninguno'}")
print(f"  Géneros comunes entre usuario1 y usuario3: {comunes_1_3 if comunes_1_3 else 'Ninguno'}")
print(f"  Géneros comunes entre usuario2 y usuario3: {comunes_2_3 if comunes_2_3 else 'Ninguno'}")
print(f"  Géneros que le gustan a al menos uno: {len(universo_generos)} distintos")
print(f"  Géneros exclusivos de usuario1: {exclusivos_1 if exclusivos_1 else 'Ninguno'}")
print(f"  Géneros exclusivos de usuario2: {exclusivos_2 if exclusivos_2 else 'Ninguno'}")
print(f"  Géneros exclusivos de usuario3: {exclusivos_3 if exclusivos_3 else 'Ninguno'}")
print(f"  Diferencia simétrica usuario1 vs usuario2: {diff_simetrica_1_2}")

# Usar <= para verificar subconjunto e imprimir el resumen final integrado
print("\nVerificaciones de subconjuntos:")
print(f"  ¿Los géneros de usuario1 son subconjunto de los de usuario2? -> {usuario1 <= usuario2}")
print(f"  ¿Los géneros de usuario2 son subconjunto de los de usuario1? -> {usuario2 <= usuario1}")
print(f"  ¿Los géneros de usuario1 son subconjunto del universo? -> {usuario1 <= universo_generos}")

print("\n--- RESUMEN FINAL ---")
print(f"Total de productos únicos en todas las tiendas: {len(catalogo_completo)}")
print(f"Cantidad de géneros cinematográficos considerados: {len(universo_generos)}")
print(f"Recomendación: Para usuario1 se sugiere explorar géneros como {exclusivos_1 if exclusivos_1 else 'todos ya cubiertos'}")