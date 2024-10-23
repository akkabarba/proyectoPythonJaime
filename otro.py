import requests

BASE_URL = 'https://swapi.dev/api'

def obtener_personajes():
    """Obtiene una lista de personajes de Star Wars."""
    response = requests.get(f'{BASE_URL}/people/')
    response.raise_for_status()
    return response.json()['results']

def info_personaje():
    """Obtiene toda la información de un personaje en función de su nombre"""
    response = requests.get(f'{BASE_URL}/people/')
    response.raise_for_status()
    return response.json()['results']

def obtener_naves():
    """Obtiene una lista de naves de Star Wars."""
    response = requests.get(f'{BASE_URL}/starships/')
    response.raise_for_status()
    return response.json()['results']

def obtener_planetas():
    """Obtiene una lista de planetas de Star Wars."""
    response = requests.get(f'{BASE_URL}/planets/')
    response.raise_for_status()
    return response.json()['results']

def opciones_personajes():
    """Opciones para los personajes"""
    print("\n--- Personajes ---")
    print("1. Listar todos los personajes") # 83 personajes hay en la API
    print("2. Buscar personaje por nombre")
    print("3. Peliculas en las que aparecen")
    print("4. Salir")

def opciones_naves():
    """Opciones para las naves"""
    print("\n--- Naves ---")
    print("1. Listar todas las naves") # 43 naves hay en la API
    print("2. Buscar nave por nombre")
    print("3. Precio de una nave en créditos de la república")
    print("4. Salir") 

def opciones_planetas():
    """Opciones para los planetas"""
    print("\n--- Planetas ---")
    print("1. Listar todos los planetas") # 60 planetas hay en la API
    print("2. Buscar planeta por nombre")
    print("3. Habitantes populares de un planeta")
    print("4. Salir")   

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
                choice_personajes = input("Elige una opción (1-4): ")
                if choice_personajes == '1':
                    personajes = obtener_personajes()
                    print("\nPersonajes de Star Wars:")
                    for personaje in personajes:
                        print(f"- {personaje['name']}")
                
                elif choice_personajes == '2':
                    nombre_personaje = input("Introduce el nombre del personaje a buscar")
                    
                    personaje = info_personaje()
        
        elif choice == '2':
            naves = obtener_naves()
            print("\nNaves de Star Wars:")
            for nave in naves:
                print(f"- {nave['name']}")
        
        elif choice == '3':
            planetas = obtener_planetas()
            print("\nPlanetas de Star Wars:")
            for planeta in planetas:
                print(f"- {planeta['name']}")
        
        elif choice == '4':
            print("Saliendo de la aplicación...")
            break
        
        else:
            print("Opción no válida. Por favor, elige nuevamente.")

if __name__ == '__main__':
    main()
