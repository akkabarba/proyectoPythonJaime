import requests
import tkinter as tk
from tkinter import messagebox, scrolledtext

# URL de la API de PokeAPI
url = 'https://pokeapi.co/api/v2/pokemon'

def descargar_datos(url):
    """Descarga los datos JSON de la API, gestionando la paginación."""
    pokemon_list = []
    next_url = url

    while next_url:
        response = requests.get(next_url)
        response.raise_for_status()  # Lanza un error si la respuesta es un error HTTP
        data = response.json()
        
        # Agrega los Pokémon de la página actual a la lista
        pokemon_list.extend(data['results'])

        # Actualiza next_url para la próxima página
        next_url = data['next']

    return pokemon_list

class PokeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PokeAPI App")
        
        self.pokemon_list = descargar_datos(url)

        # Etiquetas y entradas
        self.label_search = tk.Label(master, text="Buscar Pokémon:")
        self.label_search.pack()
        self.entry_search = tk.Entry(master)
        self.entry_search.pack()

        self.button_search = tk.Button(master, text="Buscar", command=self.buscar_pokemon)
        self.button_search.pack()

        self.label_filter = tk.Label(master, text="Filtrar Pokémon por inicial:")
        self.label_filter.pack()
        self.entry_filter = tk.Entry(master)
        self.entry_filter.pack()

        self.button_filter = tk.Button(master, text="Filtrar", command=self.filtrar_pokemon)
        self.button_filter.pack()

        self.text_area = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=15)
        self.text_area.pack()

    def buscar_pokemon(self):
        name = self.entry_search.get().lower()
        pokemon = next((p for p in self.pokemon_list if p['name'] == name), None)
        if pokemon:
            self.text_area.insert(tk.END, f"Pokémon encontrado: {pokemon['name']}\n")
        else:
            messagebox.showinfo("No encontrado", "Pokémon no encontrado.")

    def filtrar_pokemon(self):
        initial = self.entry_filter.get().lower()
        filtered = [p for p in self.pokemon_list if p['name'].startswith(initial)]
        
        self.text_area.delete(1.0, tk.END)  # Limpiar el área de texto
        if filtered:
            for pokemon in filtered:
                self.text_area.insert(tk.END, f"{pokemon['name']}\n")
        else:
            messagebox.showinfo("No encontrado", "No se encontraron Pokémon que comiencen con esa letra.")

# Crear la ventana principal
if __name__ == '__main__':
    root = tk.Tk()
    app = PokeApp(root)
    root.mainloop()
