import requests

BASE_URL = 'https://swapi.dev/api' # API que estamos utilizando

def obtener_personajes(): # Nos devuelve una lista de los primeros 10 personajes, es así por defecto y así no sobrecargamos
    """Obtiene una lista de personajes de Star Wars."""
    response = requests.get(f'{BASE_URL}/people/')
    response.raise_for_status()
    return response.json()['results']

def obtener_naves(): # Nos devuelve una lista de las primeros 10 naves, es así por defecto y así no sobrecargamos
    """Obtiene una lista de naves de Star Wars."""
    response = requests.get(f'{BASE_URL}/starships/')
    response.raise_for_status()
    return response.json()['results']

def obtener_planetas(): # Nos devuelve una lista de los primeros 10 personajes, es así por defecto y así no sobrecargamos
    """Obtiene una lista de planetas de Star Wars."""
    response = requests.get(f'{BASE_URL}/planets/')
    response.raise_for_status()
    return response.json()['results']

def info_personaje(nombre_personaje):
    """Obtiene toda la información de un personaje en función de su nombre"""
    response = requests.get(f'{BASE_URL}/people/?search={nombre_personaje}')
    response.raise_for_status()
    resultados = response.json()['results']
    if resultados:
        return resultados[0]  # Devuelve el primer personaje encontrado
    return None

def info_nave(nombre_nave):
    """Obtiene toda la información de una nave en función de su nombre"""
    response = requests.get(f'{BASE_URL}/starships/?search={nombre_nave}')
    response.raise_for_status()
    resultados = response.json()['results']
    if resultados:
        return resultados[0]  # Devuelve la primera nave encontrada
    return None

def info_planeta(nombre_planeta):
    """Obtiene toda la información de un planeta en función de su nombre"""
    response = requests.get(f'{BASE_URL}/planets/?search={nombre_planeta}')
    response.raise_for_status()
    resultados = response.json()['results']
    if resultados:
        return resultados[0] # Devuelve el primer planeta encontrado
    return None

def mostrar_info_personaje(personaje):
    """Muestra toda la información disponible de un personaje."""
    print(f"\nInformación del personaje:")
    print(f"Nombre: {personaje['name']}")
    print(f"Altura: {personaje['height']} cm")
    print(f"Peso: {personaje['mass']} kg")
    print(f"Color de cabello: {personaje['hair_color']}")
    print(f"Color de piel: {personaje['skin_color']}")
    print(f"Color de ojos: {personaje['eye_color']}")
    print(f"Año de nacimiento: {personaje['birth_year']}")
    print(f"Género: {personaje['gender']}")
    print(f"\nPelículas en las que aparece {personaje['name']}:")
    for pelicula in personaje['films']: # Este for nos devuelve los nombre de las películas en las que aparece el personaje introducido
        titulo_pelicula = obtener_titulo_pelicula(pelicula)
        print(f"- {titulo_pelicula}")

def obtener_titulo_pelicula(url_pelicula):
    """Obtiene el título de una película a partir de su URL."""
    response = requests.get(url_pelicula)
    response.raise_for_status()
    return response.json()['title']

def mostrar_info_planeta(planeta):
    """Muestra toda la información disponible de un planeta."""
    print(f"Nombre: {planeta['name']}")
    print(f"Periodo de rotación: {planeta['rotation_period']}")
    print(f"Periodo orbital: {planeta['orbital_period']}")
    print(f"Diametro: {planeta['diameter']}")
    print(f"Clima: {planeta['climate']}")
    print(f"Gravedad: {planeta['gravity']}")
    print(f"Terreno: {planeta['terrain']}")
    print(f"Superficie acuática: {planeta['surface_water']}")
    print(f"Población: {planeta['population']}")
    print(f"\nHabitantes populares de {planeta['name']}:")
    for habitante in planeta['residents']: # Este for nos devuelve los nombre de los habitantes más importantes del planeta introducido
        nombre_habitante = obtener_nombre_habitante(habitante)
        print(f"- {nombre_habitante}")

def obtener_nombre_habitante(url_habitante):
    """Obtiene los habitantes de un planeta a partir de su URL"""
    response = requests.get(url_habitante)
    response.raise_for_status()
    return response.json()['name']

def mostrar_info_nave(nave):
    """Muestra toda la información disponible de una nave."""
    print(f"\nInformación de la nave:")
    print(f"Nombre: {nave['name']}")
    print(f"Modelo: {nave['model']}")
    print(f"Manufacturador: {nave['manufacturer']}")
    print(f"Precio: {nave['cost_in_credits']}")
    print(f"Longitud: {nave['length']}")
    print(f"Máxima velocidad atmosféreica: {nave['max_atmosphering_speed']}")
    print(f"Tripulantes: {nave['crew']}")
    print(f"Pasajeros: {nave['passengers']}")
    print(f"Capacidad de carga: {nave['cargo_capacity']}")
    print(f"Consumibles: {nave['consumables']}")
    print(f"Hipervelocidad: {nave['hyperdrive_rating']}")
    print(f"Megaluz por hora: {nave['MGLT']}")
    print(f"Clase de nave: {nave['starship_class']}")

def opciones_personajes():
    """Opciones para los personajes"""
    print("\n--- Personajes ---")
    print("1. Listar todos los personajes") # 83 personajes hay en la API, pero solo muestra 10 por defecto(para no sobrecargar)
    print("2. Buscar personaje por nombre") # Nos da información general sobre un personaje introducido
    print("3. Salir")

def opciones_naves():
    """Opciones para las naves"""
    print("\n--- Naves ---")
    print("1. Listar todas las naves") # 43 naves hay en la API, pero solo muestra 10 por defecto(para no sobrecargar)
    print("2. Buscar nave por nombre") # Nos da información general sobre una nave introducida
    print("3. Salir") 

def opciones_planetas():
    """Opciones para los planetas"""
    print("\n--- Planetas ---")
    print("1. Listar todos los planetas") # 60 planetas hay en la API, pero solo muestra 10 por defecto(para no sobrecargar)
    print("2. Buscar planeta por nombre") # Nos da información general sobre un planeta introducido
    print("3. Salir")   

def mostrar_opciones():
    """Muestra las opciones del menú."""
    print("\n--- Menú ---")
    print("1. Personajes")
    print("2. Naves")
    print("3. Planetas")
    print("4. Salir")

def main():
    """Función principal para interactuar con el usuario."""
    while True:
        mostrar_opciones()
        choice = input("Elige una opción (1-4): ")

        if choice == '1':
            while True:
                opciones_personajes()
                choice_personajes = input("Elige una opción (1-3): ")
                if choice_personajes == '1':
                    personajes = obtener_personajes()
                    print("\nPersonajes de Star Wars:")
                    for personaje in personajes:
                        print(f"- {personaje['name']}")
                
                elif choice_personajes == '2':
                    nombre_personaje = input("Introduce el nombre del personaje a buscar: ")
                    personaje = info_personaje(nombre_personaje)
                    if personaje:
                        mostrar_info_personaje(personaje)
                    else:
                        print(f"No se encontró ningún personaje con el nombre '{nombre_personaje}'.")

                elif choice_personajes == '3':
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, elige nuevamente.")
        
        elif choice == '2':
            while True:
                opciones_naves()
                choice_naves = input("Elige una opción (1-3): ")
                if choice_naves == '1':
                    naves = obtener_naves()
                    print("\nNaves de Star Wars:")
                    for nave in naves:
                        print(f"- {nave['name']}")
                elif choice_naves == '2':
                    nombre_nave = input("Introduce el nombre de la nave a buscar: ")
                    nave = info_nave(nombre_nave)
                    if nave:
                        mostrar_info_nave(nave)
                    else:
                        print(f"No se encontró ninguna nave con el nombre '{nombre_nave}'.")
                elif choice_naves == '3':
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, elige nuevamente.")
        
        elif choice == '3':
            while True:
                opciones_planetas()
                choice_planetas = input("Elige una opción (1-3): ")
                if choice_planetas == '1':
                    planetas = obtener_planetas()
                    print("\nPlanetas de Star Wars:")
                    for planeta in planetas:
                        print(f"- {planeta['name']}")
                elif choice_planetas == '2':
                    nombre_planeta = input("Introduce el nombre del planeta a buscar: ")
                    planeta = info_planeta(nombre_planeta)
                    if planeta:
                        mostrar_info_planeta(planeta)
                    else:
                        print(f"No se encontró ningun planeta con el nombre '{nombre_planeta}'.")
                elif choice_planetas == '3':
                    print("Volviendo al menú principal...")
                    break
                else:
                    print("Opción no válida. Por favor, elige nuevamente.")

        
        elif choice == '4':
            print("Saliendo de la aplicación...")
            break
        
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

if __name__ == '__main__':
    main()
