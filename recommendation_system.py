peliculas = [
    ("Cadena perpetua", "Drama", 9.3),
    ("El padrino", "Crimen", 9.2),
    ("El caballero oscuro", "Acción", 9.0),
    ("Pulp Fiction", "Crimen", 8.9),
    ("Origen", "Ciencia Ficción", 8.8),
    ("Interestelar", "Ciencia Ficción", 8.7),
    ("Matrix", "Ciencia Ficción", 8.7),
    ("Forrest Gump", "Drama", 8.8),
    ("El rey león", "Animación", 8.5),
    ("Toy Story", "Animación", 8.3),
    ("El viaje de Chihiro", "Animación", 8.6),
    ("El gran Hotel Budapest", "Comedia", 8.1),
    ("Muy loco por ella", "Comedia", 7.7),
    ("Déjame salir", "Terror", 7.8),
    ("El conjuro", "Terror", 7.5),
    ("El silencio de los corderos", "Suspenso", 8.6),
    ("Titanic", "Romance", 7.9),
    ("La La Land", "Musical", 8.0),
    ("Avatar", "Ciencia Ficción", 7.9),
    ("Parque Jurásico", "Aventura", 8.2),
    ("Harry Potter y la piedra filosofal", "Fantasía", 7.6),
    ("El señor de los anillos: La comunidad del anillo", "Fantasía", 8.8),
    ("El prestigio", "Suspenso", 8.5),
    ("Parásitos", "Drama", 8.5),
    ("Django desencadenado", "Crimen", 8.4),
    ("Del revés", "Animación", 8.1),
    ("Whiplash", "Drama", 8.5),
    ("Buscando a Nemo", "Animación", 8.2),
    ("No hay país para viejos", "Crimen", 8.1),
    ("Infiltrados", "Crimen", 8.5),
    ("Zootopia", "Animación", 8.0),
    ("La red social", "Drama", 7.8),
    ("Mad Max: Fury Road", "Acción", 8.1),
    ("Ex Machina", "Ciencia Ficción", 7.7),
    ("La bruja", "Terror", 6.8),
    ("Una voz silenciosa", "Drama", 8.2),
]

alias = {
    "accion": "Acción", "acción": "Acción",
    "drama": "Drama",
    "comedia": "Comedia",
    "terror": "Terror",
    "suspenso": "Suspenso",
    "romance": "Romance",
    "romántica": "Romance",
    "ciencia ficcion": "Ciencia Ficción",
    "ciencia ficción": "Ciencia Ficción",
    "animacion": "Animación",
    "animación": "Animación",
    "aventura": "Aventura",
    "fantasia": "Fantasía",
    "fantasía": "Fantasía",
    "crimen": "Crimen",
    "musical": "Musical"
}


def normalizar(genero):
    return alias.get(genero.strip().lower(), genero.strip().title())


def recomendar(genero):
    g = normalizar(genero)
    return sorted([(t, r) for t, ge, r in peliculas if ge == g], key=lambda x: x[1], reverse=True)[:5]

print("=== Recomendador de películas por género ===")

while True:
    print("\n1. Buscar otra película por género")
    print("2. Salir")
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        genero = input("¿Qué género quieres ver? ").strip()
        resultado = recomendar(genero)

        if resultado:
            print(f"\nLas mejores películas de {genero} son:")
            for i, (titulo, rating) in enumerate(resultado, 1):
                print(f"{i}. {titulo} - {rating}⭐")
        else:
            print("No encontré ese género en la lista.")

    elif opcion == "2":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida. Presiona 1 para buscar o 2 para salir.")
