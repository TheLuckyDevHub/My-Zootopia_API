import file_operations


def animal_type_to_string(characteristics, string_output) -> str:
    if characteristics:
        charac_type = characteristics.get("type", None)
        if charac_type:
            string_output = f"{string_output}Type: {charac_type}\n"
    return string_output


def animal_locations_to_string(locations: list[str], string_output) -> str:
    """Streams the location/locations of an animal to the given output stream"""
    if locations:
        if len(locations) == 1:
            string_output = f"{string_output}Location: {locations[0]}\n"
        if len(locations) > 1:
            string_output = f"{string_output}Locations: {", ".join(locations)}\n"
    return string_output


def animal_characteristics_to_string(
    characteristics: dict[str, any], string_output
) -> str:
    """Streams the characteristics of an animal to the given output stream"""
    if characteristics:
        diet = characteristics.get("diet", None)
        if diet:
            string_output = f"{string_output}Diet: {diet}\n"
    return string_output


def animal_data_output_to_string(animal):
    """Streams the animal data to the given output string"""
    string_output = f"Name: {animal['name']}\n"
    characteristics = animal.get("characteristics", None)
    string_output = animal_characteristics_to_string(characteristics, string_output)
    locations = animal.get("locations", None)
    string_output = animal_locations_to_string(locations, string_output)
    string_output = animal_type_to_string(characteristics, string_output)
    return string_output


def print_animals(animals: dict[str, any]) -> None:
    """Prints the list of animals"""
    if animals is None:
        print("No animals data to display")
    for animal in animals:
        string_output = animal_data_output_to_string(animal)
        print(string_output)
        print()


def animals_to_html_template(animals: dict[str, any], html_template: str) -> str:
    if animals is None:
        print("No animals data to display")
        return html_template
    string_output = ""
    for animal in animals:
        string_output += animal_data_output_to_string(animal)
    
    html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", string_output)
    return html_template

def main():
    animals_data = file_operations.load_data("animals_data.json")
    # print_animals(animals_data)

    html_template = file_operations.read_template_html("animals_template.html")
    html_str = animals_to_html_template(animals_data, html_template)
    file_operations.save_html(html_str,'animals.html')


if __name__ == "__main__":
    main()
