import file_operations


def animal_type_to_string(characteristics, string_output) -> str:
    if characteristics:
        charac_type = characteristics.get("type", None)
        if charac_type:
            string_output = f"{string_output}Type: {charac_type}"
    return string_output + '</br>\n'


def animal_locations_to_string(locations: list[str], string_output) -> str:
    """Streams the location/locations of an animal to the given output stream"""
    if locations:
        if len(locations) == 1:
            string_output = f"{string_output}Location: {locations[0]}"
        if len(locations) > 1:
            string_output = f"{string_output}Locations: {", ".join(locations)}"
    return string_output+ '</br>\n'


def animal_characteristics_to_string(
    characteristics: dict[str, any], string_output: str
) -> str:
    """Streams the characteristics of an animal to the given output stream"""
    if characteristics:
        diet = characteristics.get("diet", None)
        if diet:
            string_output = f"{string_output}Diet: {diet}"
    return string_output + '</br>\n'


def animal_data_output_to_string(animal: dict[str, any]) -> str:
    """Streams the animal data to the given output string"""
    string_output = f"Name: {animal['name']}</br>\n"
    characteristics = animal.get("characteristics", None)
    string_output = animal_characteristics_to_string(characteristics, string_output)
    locations = animal.get("locations", None)
    string_output = animal_locations_to_string(locations, string_output)
    string_output = animal_type_to_string(characteristics, string_output)
    return string_output

def animals_to_html_template(animals: dict[str, any], html_template: str) -> str:
    if animals is None:
        print("No animals data to display")
        return html_template
    string_output = ""
    for animal in animals:
        string_output +=f'<li class="cards__item">\n'
        string_output += animal_data_output_to_string(animal)
        string_output +=f'</li">\n'
    
    html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", string_output)
    return html_template

def main():
    animals_data = file_operations.load_data("animals_data.json")

    html_template = file_operations.read_template_html("animals_template.html")
    html_str = animals_to_html_template(animals_data, html_template)
    file_operations.save_html(html_str,'animals.html')


if __name__ == "__main__":
    main()
