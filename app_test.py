import os
import json

def test_pokemon_database():
    path = os.path.expanduser("~/pokeapi/pokemon_data_base.json")
    
    if not os.path.exists(path):
        print("JSON database file not found.")
        return

    with open(path, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print("JSON file is not valid.")
            return

        if not data:
            print("JSON file is empty.")
        else:
            print("Pokémon database has entries.")

if __name__ == "__main__":
    test_pokemon_database()
