import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data("animals_data.json")

print(animals_data)

for animal in animals_data:
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    type = animal.get("characteristics", {}).get("type")
    location_list = animal.get("locations")
    # location = location_list[0] if location_list else ""
    if name:
        print(f"Name: {name}")
    if diet:
        print(f"Diet: {diet}")
    if location_list:
        print(f"Location: {location_list[0]}")
    if type:
        print(f"Type: {type}")
    print()
