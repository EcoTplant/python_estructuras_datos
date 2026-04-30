# Definir catalogo como tupla de subtuplas (título, director, año, puntuación)
catalogo = (
    ("El Padrino", "Francis Ford Coppola", 1972, 9.2),
    ("Cadena Perpetua", "Frank Darabont", 1994, 9.3),
    ("El Caballero Oscuro", "Christopher Nolan", 2008, 9.0),
    ("Pulp Fiction", "Quentin Tarantino", 1994, 8.9),
    ("Inception", "Christopher Nolan", 2010, 8.8),
    ("Forrest Gump", "Robert Zemeckis", 1994, 8.8),
)

# Recorrer catalogo con for desempaquetando los cuatro campos
print("=== CATÁLOGO DE PELÍCULAS ===\n")
for titulo, director, año, puntuacion in catalogo:
    print(f" {titulo} ({año}) - Dirigida por {director} - Puntuación: {puntuacion}")

# Usar operador * para separar primera película del resto
primera_pelicula, *resto_peliculas = catalogo
print("\n" + "="*50)
print(f"\n Primera película del catálogo:\n   {primera_pelicula[0]} ({primera_pelicula[2]})")
print(f"\n Resto de películas ({len(resto_peliculas)}):")
for titulo, director, año, puntuacion in resto_peliculas:
    print(f"   - {titulo} ({año})")

# Implementar buscar_por_director() que devuelva tupla de coincidencias
def buscar_por_director(director):
    """Busca todas las películas de un director específico"""
    coincidencias = []
    for pelicula in catalogo:
        if pelicula[1] == director:
            coincidencias.append(pelicula)
    return tuple(coincidencias)

# Implementar obtener_estadisticas() retornando (min, max, promedio)
def obtener_estadisticas(peliculas):
    """Calcula la puntuación mínima, máxima y promedio de una lista de películas"""
    if not peliculas:
        return (0.0, 0.0, 0.0)
    
    puntuaciones = [pelicula[3] for pelicula in peliculas]
    min_punt = min(puntuaciones)
    max_punt = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)
    return (min_punt, max_punt, promedio)

# Llamar a buscar_por_director e imprimir coincidencias
print("\n" + "="*50)
director_buscar = "Christopher Nolan"
print(f"\n Películas de {director_buscar}:")
peliculas_nolan = buscar_por_director(director_buscar)

if peliculas_nolan:
    for titulo, director, año, puntuacion in peliculas_nolan:
        print(f"   • {titulo} ({año}) - {puntuacion}")
else:
    print(f"   No se encontraron películas de {director_buscar}")

# Desempaquetar retorno de obtener_estadisticas
print("\n" + "="*50)
print("\n ESTADÍSTICAS DEL CATÁLOGO COMPLETO:")

# Desempaquetamos el retorno de obtener_estadisticas
min_puntuacion, max_puntuacion, promedio_puntuacion = obtener_estadisticas(catalogo)

# Imprimir mínima, máxima y promedio
print(f" Puntuación más baja:  {min_puntuacion}")
print(f" Puntuación más alta: {max_puntuacion}")
print(f" Puntuación promedio: {promedio_puntuacion:.2f}")

# Bonus: Estadísticas de un director específico
print("\n" + "="*50)
print(f"\n ESTADÍSTICAS DE {director_buscar.upper()}:")
min_nol, max_nol, prom_nol = obtener_estadisticas(peliculas_nolan)
print(f"   Puntuación más baja:  {min_nol}")
print(f"   Puntuación más alta: {max_nol}")
print(f"   Puntuación promedio: {prom_nol:.2f}")