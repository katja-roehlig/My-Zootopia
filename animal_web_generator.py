import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_data():
    animal_data = load_data("animals_data.json")
    output = ""
    for animal in animal_data:
        name = animal.get("name", 0)
        diet = animal.get("characteristics", {}).get("diet", 0)
        type = animal.get("characteristics", {}).get("type", 0)
        location_list = animal.get("locations", 0)
        output += "<li class='cards__item'>"
        if name:
            output += f"<div class='card__title'> Name: {name}</div>"
        output += "<p class='card__text'>"
        if diet:
            output += f"<strong>Diet:</strong> {diet}<br/>"
        if location_list:
            output += f"<strong>Location:</strong> {location_list[0]}<br/>"
        if type:
            output += f"<strong>Type:</strong> {type}<br/>"
        output += "</p>"
        output += "</li>"
    return output


def create_new_html():
    with open("animals_template.html", "r") as page_file:
        web_data = page_file.read()
    animal_string = get_animal_data()
    new_web_data = web_data.replace("__REPLACE_ANIMALS_INFO__", animal_string)
    with open("animals.html", "w") as new_file:
        new_file.write(new_web_data)


create_new_html()
