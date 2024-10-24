import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

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

def obtener_planetas(): # Nos devuelve una lista de los primeros 10 planetas, es así por defecto y así no sobrecargamos
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