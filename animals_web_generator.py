import requests

import file_operations
import serializer


def get_skin_types(animals: dict[str, any]) -> list[str]:
    """Extracts skin types from an animal's characteristics"""
    skin_types = set()
    for animal in animals:
        characteristics = animal.get("characteristics", None)
        if characteristics:
            skin_type = characteristics.get("skin_type", None)
            if skin_type:
                skin_types.add(skin_type)
    return list(skin_types)


def print_skin_type_options(skin_types: list[str]) -> None:
    """Prints available skin types from the animals data"""
    print("Available skin types:")
    print(f"0 - All skin types")
    for i, skin_type in enumerate(skin_types):
        print(f"{i+1} - {skin_type}")


def handle_user_input(skin_types: list[str]) -> int:
    max_number = len(skin_types)
    print_skin_type_options(skin_types)
    user_input = input(
        f"Select a skin type by entering the corresponding number [0-{max_number}]: "
    )
    try:
        selected_number = int(user_input)
        if selected_number < 0 or selected_number > max_number:
            print("Invalid selection. Serialize all skin types.")
            return 0
        elif selected_number == 0:
            print("Serialize all skin types.")
            return 0
        else:
            print(f"Serialize for skin type: {skin_types[selected_number-1]}.")
            return selected_number
    except ValueError:
        print("Invalid input. Serialize all skin types.")
        return 0


def create_html_by_skin_type(
    animals: dict[str, any], skin_types: list[str], selected: int, html_template: str
) -> str:
    """Creates an HTML file based on the selected skin type"""
    filtered_animals = animals
    selected_skin_type = "All"
    if selected != 0:
        selected_skin_type = skin_types[selected - 1]
        filtered_animals = [
            animal
            for animal in animals
            if animal.get("characteristics", {}).get("skin_type", None)
            == selected_skin_type
        ]

        # Serialize selected skin type
    html_str = serializer.serialized_animals_to_html_template(
        filtered_animals, html_template
    )
    file_operations.save_html(html_str, f"animals_{selected_skin_type}.html")


def get_animal_from_api_ninjas(to_search_animal):
    """_summary_

    Args:
        to_search_animal (_type_): _description_

    Returns:
        _type_: _description_
    """
    api_url = "https://api.api-ninjas.com/v1/animals?name={}".format(to_search_animal)
    response = requests.get(
        api_url, headers={"X-Api-Key": "tlObzwDKSlaOPwL9Dm0wlw==nejGIJLbqlJiyUHr"}
    )
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        
    return None


def main():
    """
    Main function to generate the animals HTML file from
    api-ninjas animals api and an HTML template
    """
    animals_data = get_animal_from_api_ninjas("fox")
    
    if not animals_data:
        print("No animals data to process!!")
        return

    skin_types = get_skin_types(animals_data)
    selected_skin_type = handle_user_input(skin_types)
    html_template = file_operations.loads_template_html("animals_template.html")
    create_html_by_skin_type(
        animals_data, skin_types, selected_skin_type, html_template
    )


if __name__ == "__main__":
    main()
