import json


def load_data(file_path):
    """
    loads data from json file

    :param file_path
    :return content of json file
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_html_string_for_all_animals(data):
    """
    Takes the data list of dictioniaries from the JSON file
    and generates a string from every dictionary
    :return: the html string for all animals
    """

    animals_html_string = ""
    for animal in data:
        animals_html_string += get_html_string_for_one_animal(animal)
    return animals_html_string


def get_html_string_for_one_animal(animal):
    """
    Takes a dictionary and generates a string with HTML elements from specific data within it.
    :param animal -  dictionary
    :return string for one animal
    """
    output = ""
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    type = animal.get("characteristics", {}).get("type")
    distinctive_feature = animal.get("characteristics", {}).get(
        "distinctive_feature",
        animal.get("characteristics", {}).get("most_distinctive_feature"),
    )
    color = animal.get("characteristics", {}).get("color")
    skin_type = animal.get("characteristics", {}).get("skin_type")
    lifespan = animal.get("characteristics", {}).get("lifespan")

    location_list = animal.get("locations")
    output += "<li class='cards__item'>"
    if name:
        output += f"<div class='card__title'> Name: {name}</div>"
    output += "<div class='card__text'>"
    output += "<ul class='card__list'>"
    if diet:
        output += f"<li><strong>Diet:</strong> {diet}</li>"
    if location_list:
        output += f"<li><strong>Location:</strong> {location_list[0]}</li>"
    if type:
        output += f"<li><strong>Type:</strong> {type}</li>"
    if distinctive_feature:
        output += (
            f"<li><strong>Distinctive feature:</strong> {distinctive_feature}</li>"
        )
    if color:
        output += f"<li><strong>Color:</strong> {color}</li>"
    if skin_type:
        output += f"<li><strong>Skin type:</strong> {skin_type}</li>"
    if lifespan:
        output += f"<li><strong>Lifespan:</strong> {lifespan}</li>"
    output += "</ul>"
    output += "</div>"
    output += "</li>"
    return output


def create_new_html_page(html_string):
    """
    Replaces text from the HTML file with a string and saves the page in a new HTML page
    """
    with open("animals_template.html", "r") as page_file:
        web_data = page_file.read()
    new_web_data = web_data.replace("__REPLACE_ANIMALS_INFO__", html_string)
    with open("animals.html", "w") as new_file:
        new_file.write(new_web_data)


def main():
    animals_data = load_data("animals_data.json")
    animals_html_string = get_html_string_for_all_animals(animals_data)
    create_new_html_page(animals_html_string)


if __name__ == "__main__":
    main()
