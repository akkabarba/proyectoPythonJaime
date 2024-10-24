import tkinter as tk
from tkinter import ttk, messagebox
import requests

BASE_URL = 'https://swapi.dev/api'

def obtener_personajes():
    """Obtiene una lista de los primeros 10 personajes de Star Wars."""
    response = requests.get(f'{BASE_URL}/people/')
    response.raise_for_status()
    return response.json()['results']

def obtener_naves():
    """Obtiene una lista de las primeras 10 naves de Star Wars."""
    response = requests.get(f'{BASE_URL}/starships/')
    response.raise_for_status()
    return response.json()['results']

def obtener_planetas():
    """Obtiene una lista de los primeros 10 planetas de Star Wars."""
    response = requests.get(f'{BASE_URL}/planets/')
    response.raise_for_status()
    return response.json()['results']

def info_personaje(nombre_personaje):
    """Obtiene toda la información de un personaje en función de su nombre"""
    response = requests.get(f'{BASE_URL}/people/?search={nombre_personaje}')
    response.raise_for_status()
    return response.json()['results']

def mostrar_info_personaje():
    """Busca y muestra la información del personaje ingresado."""
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Entrada inválida", "Por favor, introduce el nombre de un personaje.")
        return

    personaje = info_personaje(nombre)
    if personaje:
        personaje = personaje[0]  # Obtener el primer resultado
        info = f"Nombre: {personaje['name']}\n" \
               f"Altura: {personaje['height']} cm\n" \
               f"Peso: {personaje['mass']} kg\n" \
               f"Color de cabello: {personaje['hair_color']}\n" \
               f"Color de piel: {personaje['skin_color']}\n" \
               f"Color de ojos: {personaje['eye_color']}\n" \
               f"Año de nacimiento: {personaje['birth_year']}\n" \
               f"Género: {personaje['gender']}\n"
        messagebox.showinfo("Información del personaje", info)
    else:
        messagebox.showwarning("Personaje no encontrado", f"No se encontró ningún personaje con el nombre '{nombre}'.")

def listar_personajes():
    """Lista los primeros 10 personajes."""
    personajes = obtener_personajes()
    lista.delete(0, tk.END)  # Limpiar lista
    for personaje in personajes:
        lista.insert(tk.END, personaje['name'])

def listar_naves():
    """Lista las primeras 10 naves."""
    naves = obtener_naves()
    lista.delete(0, tk.END)  # Limpiar lista
    for nave in naves:
        lista.insert(tk.END, nave['name'])

def listar_planetas():
    """Lista los primeros 10 planetas."""
    planetas = obtener_planetas()
    lista.delete(0, tk.END)  # Limpiar lista
    for planeta in planetas:
        lista.insert(tk.END, planeta['name'])

# Crear la ventana principal
root = tk.Tk()
root.title("Star Wars Info")
root.geometry("400x400")

# Etiqueta e ingreso para buscar personajes por nombre
label_nombre = ttk.Label(root, text="Buscar personaje por nombre:")
label_nombre.pack(pady=10)

entry_nombre = ttk.Entry(root)
entry_nombre.pack(pady=5)

boton_buscar = ttk.Button(root, text="Buscar", command=mostrar_info_personaje)
boton_buscar.pack(pady=5)

# Botones para listar personajes, naves y planetas
boton_personajes = ttk.Button(root, text="Listar personajes", command=listar_personajes)
boton_personajes.pack(pady=5)

boton_naves = ttk.Button(root, text="Listar naves", command=listar_naves)
boton_naves.pack(pady=5)

boton_planetas = ttk.Button(root, text="Listar planetas", command=listar_planetas)
boton_planetas.pack(pady=5)

# Lista para mostrar resultados
lista = tk.Listbox(root, height=10, width=50)
lista.pack(pady=20)

# Iniciar el bucle principal de la interfaz
root.mainloop()
