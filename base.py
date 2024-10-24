import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading

BASE_URL = 'https://swapi.dev/api'

def obtener_personajes():
    """Obtiene una lista de todos los personajes de Star Wars."""
    personajes = []
    url = f'{BASE_URL}/people/'
    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        personajes.extend(data['results'])
        url = data['next']  # Avanzar a la siguiente página
    return personajes

def obtener_naves():
    """Obtiene una lista de todas las naves de Star Wars."""
    naves = []
    url = f'{BASE_URL}/starships/'
    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        naves.extend(data['results'])
        url = data['next']  # Avanzar a la siguiente página
    return naves

def obtener_planetas():
    """Obtiene una lista de todos los planetas de Star Wars."""
    planetas = []
    url = f'{BASE_URL}/planets/'
    while url:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        planetas.extend(data['results'])
        url = data['next']  # Avanzar a la siguiente página
    return planetas

def obtener_nombre_habitante(url_habitante):
    """Obtiene los habitantes de un planeta a partir de su URL"""
    response = requests.get(url_habitante)
    response.raise_for_status()
    return response.json()['name']

def info_personaje(nombre_personaje):
    """Obtiene toda la información de un personaje en función de su nombre"""
    response = requests.get(f'{BASE_URL}/people/?search={nombre_personaje}')
    response.raise_for_status()
    return response.json()['results']

def info_nave(nombre_nave):
    """Obtiene toda la información de una nave en función de su nombre"""
    response = requests.get(f'{BASE_URL}/starships/?search={nombre_nave}')
    response.raise_for_status()
    return response.json()['results']

def info_planeta(nombre_planeta):
    """Obtiene toda la información de un planeta en función de su nombre"""
    response = requests.get(f'{BASE_URL}/planets/?search={nombre_planeta}')
    response.raise_for_status()
    return response.json()['results']

def mostrar_info_personaje(ventana, entry_nombre):
    """Busca y muestra la información del personaje ingresado."""
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Entrada inválida", "Por favor, introduce el nombre de un personaje.", parent=ventana)
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
        messagebox.showinfo("Información del personaje", info, parent=ventana)
    else:
        messagebox.showwarning("Personaje no encontrado", f"No se encontró ningún personaje con el nombre '{nombre}'.", parent=ventana)

def mostrar_info_nave(ventana, entry_nombre):
    """Busca y muestra la información de la nave ingresada."""
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Entrada inválida", "Por favor, introduce el nombre de una nave.", parent=ventana)
        return

    nave = info_nave(nombre)
    if nave:
        nave = nave[0]  # Obtener el primer resultado
        info = f"Nombre: {nave['name']}\n" \
               f"Modelo: {nave['model']}\n" \
               f"Fabricante: {nave['manufacturer']}\n" \
               f"Coste en créditos: {nave['cost_in_credits']}\n" \
               f"Longitud: {nave['length']} m\n" \
               f"Velocidad máxima: {nave['max_atmosphering_speed']} km/h\n" \
               f"Capacidad de carga: {nave['cargo_capacity']} kg\n"
        messagebox.showinfo("Información de la nave", info, parent=ventana)
    else:
        messagebox.showwarning("Nave no encontrada", f"No se encontró ninguna nave con el nombre '{nombre}'.", parent=ventana)

def mostrar_info_planeta(ventana, entry_nombre):
    """Busca y muestra la información del planeta ingresado, incluyendo habitantes populares."""
    nombre = entry_nombre.get().strip()
    if not nombre:
        messagebox.showwarning("Entrada inválida", "Por favor, introduce el nombre de un planeta.", parent=ventana)
        return

    planeta = info_planeta(nombre)
    if planeta:
        planeta = planeta[0]  # Obtener el primer resultado
        info = f"Nombre: {planeta['name']}\n" \
               f"Periodo de rotación: {planeta['rotation_period']} horas\n" \
               f"Periodo orbital: {planeta['orbital_period']} días\n" \
               f"Diámetro: {planeta['diameter']} km\n" \
               f"Clima: {planeta['climate']}\n" \
               f"Gravedad: {planeta['gravity']}\n" \
               f"Terreno: {planeta['terrain']}\n" \
               f"Superficie acuática: {planeta['surface_water']} %\n" \
               f"Población: {planeta['population']}\n"

        # Obtener y mostrar habitantes populares
        if planeta['residents']:
            info += f"\nHabitantes populares de {planeta['name']}:\n"
            for habitante in planeta['residents']:
                nombre_habitante = obtener_nombre_habitante(habitante)
                info += f"- {nombre_habitante}\n"
        else:
            info += f"No hay habitantes registrados para {planeta['name']}.\n"

        messagebox.showinfo("Información del planeta", info, parent=ventana)
    else:
        messagebox.showwarning("Planeta no encontrado", f"No se encontró ningún planeta con el nombre '{nombre}'.", parent=ventana)

def listar_elementos(ventana, obtener_func):
    """Lista los elementos obtenidos (personajes, naves, planetas)."""
    resultado_texto = tk.Text(ventana, height=15, width=60)
    resultado_texto.pack(pady=10)

    # Ejecutar la obtención de datos en un hilo separado
    def obtener_y_mostrar():
        try:
            elementos = obtener_func()
            resultado_texto.config(state=tk.NORMAL)  # Habilitar el campo de texto
            resultado_texto.delete(1.0, tk.END)  # Limpiar texto anterior
            for elemento in elementos:
                if ventana.winfo_exists():
                    resultado_texto.insert(tk.END, f"- {elemento['name']}\n")
            resultado_texto.config(state=tk.DISABLED)  # Desactivar el campo de texto para evitar ediciones
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener datos: {str(e)}", parent=ventana)

    # Iniciar el hilo
    threading.Thread(target=obtener_y_mostrar, daemon=True).start()

# Ventanas para Personajes, Naves y Planetas
def ventana_personajes():
    """Crea una subventana para las opciones de personajes."""
    ventana = tk.Toplevel()
    ventana.title("Opciones de personajes")
    ventana.geometry("500x500")
    
    # Botón para listar personajes
    boton_listar = ttk.Button(ventana, text="Listar todos los personajes", command=lambda: listar_elementos(ventana, obtener_personajes))
    boton_listar.pack(pady=5)

    # Entrada y búsqueda de personajes
    label_nombre = ttk.Label(ventana, text="Buscar personaje por nombre:")
    label_nombre.pack(pady=10)

    entry_nombre = ttk.Entry(ventana)
    entry_nombre.pack(pady=5)

    boton_buscar = ttk.Button(ventana, text="Buscar personaje", command=lambda: mostrar_info_personaje(ventana, entry_nombre))
    boton_buscar.pack(pady=5)

    # Botón para salir de la ventana
    boton_salir = ttk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack(pady=5)

def ventana_naves():
    """Crea una subventana para las opciones de naves."""
    ventana = tk.Toplevel()
    ventana.title("Opciones de naves")
    ventana.geometry("500x500")

    # Botón para listar naves
    boton_listar = ttk.Button(ventana, text="Listar todas las naves", command=lambda: listar_elementos(ventana, obtener_naves))
    boton_listar.pack(pady=5)

    # Entrada y búsqueda de naves
    label_nombre = ttk.Label(ventana, text="Buscar nave por nombre:")
    label_nombre.pack(pady=10)

    entry_nombre = ttk.Entry(ventana)
    entry_nombre.pack(pady=5)

    boton_buscar = ttk.Button(ventana, text="Buscar nave", command=lambda: mostrar_info_nave(ventana, entry_nombre))
    boton_buscar.pack(pady=5)

    # Botón para salir de la ventana
    boton_salir = ttk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack(pady=5)

def ventana_planetas():
    """Crea una subventana para las opciones de planetas."""
    ventana = tk.Toplevel()
    ventana.title("Opciones de planetas")
    ventana.geometry("500x500")

    # Botón para listar planetas
    boton_listar = ttk.Button(ventana, text="Listar todos los planetas", command=lambda: listar_elementos(ventana, obtener_planetas))
    boton_listar.pack(pady=5)

    # Entrada y búsqueda de planetas
    label_nombre = ttk.Label(ventana, text="Buscar planeta por nombre:")
    label_nombre.pack(pady=10)

    entry_nombre = ttk.Entry(ventana)
    entry_nombre.pack(pady=5)

    boton_buscar = ttk.Button(ventana, text="Buscar planeta", command=lambda: mostrar_info_planeta(ventana, entry_nombre))
    boton_buscar.pack(pady=5)

    # Botón para salir de la ventana
    boton_salir = ttk.Button(ventana, text="Salir", command=ventana.destroy)
    boton_salir.pack(pady=5)

# Crear la ventana principal
root = tk.Tk()
root.title("Star Wars Info")
root.geometry("400x400")

# Botones principales que abren las subventanas
boton_personajes = ttk.Button(root, text="Personajes", command=ventana_personajes)
boton_personajes.pack(pady=10)

boton_naves = ttk.Button(root, text="Naves", command=ventana_naves)
boton_naves.pack(pady=10)

boton_planetas = ttk.Button(root, text="Planetas", command=ventana_planetas)
boton_planetas.pack(pady=10)

# Botón para salir
boton_salir = ttk.Button(root, text="Salir", command=root.quit)
boton_salir.pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()
