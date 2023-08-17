print("hello")
import os
import json
import requests
from PIL import Image
from io import BytesIO

def get_pokemon_data(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/")
    if response.status_code == 404:
        return None
    data = response.json()
    return data

def save_to_json(data, folder_path, file_name):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    file_path = os.path.join(folder_path, f"{file_name}.json")
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def main():
    pokemon_name = input("Introduce el nombre de un Pokémon: ")
    pokemon_data = get_pokemon_data(pokemon_name)

    if pokemon_data is None:
        print("¡Error! Pokémon no encontrado.")
    else:
        pokemon_info = {
            "nombre": pokemon_data["name"],
            "imagen": pokemon_data["sprites"]["front_default"],
            "peso": pokemon_data["weight"],
            "tamaño": pokemon_data["height"],
            "movimientos": [move["move"]["name"] for move in pokemon_data["moves"]],
            "habilidades": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "tipos": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }

        print("\nInformación del Pokémon:")
        print(f"Nombre: {pokemon_info['nombre']}")
        print(f"Peso: {pokemon_info['peso']}")
        print(f"Tamaño: {pokemon_info['tamaño']}")
        print(f"Movimientos: {', '.join(pokemon_info['movimientos'])}")
        print(f"Habilidades: {', '.join(pokemon_info['habilidades'])}")
        print(f"Tipos: {', '.join(pokemon_info['tipos'])}")

        try:
            response = requests.get(pokemon_info["imagen"])
            img = Image.open(BytesIO(response.content))
            
            img_path = os.path.join("pokedex", f"{pokemon_info['nombre']}.jpg")
            img.convert("RGB").save(img_path, "JPEG")
            
            os.system(f"start {img_path}")
        except Exception as e:
            print("Error al mostrar la imagen:", e)

        save_to_json(pokemon_info, "pokedex", pokemon_info["nombre"])

if __name__ == "__main__":
    main()

#############################

