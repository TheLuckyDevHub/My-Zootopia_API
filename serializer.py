def serialize_animal_type(characteristics: dict[str, any], string_output: str) -> str:
    """Adds the type of an animal form dict:characteristics to the given string"""
    if characteristics:
        charac_type = characteristics.get("type", None)
        if charac_type:
            string_output = (
                f"{string_output}      <li><strong>Type:</strong> {charac_type}</li>\n"
            )
    return string_output


def serialize_animal_location(locations: list[str], string_output: str) -> str:
    """Adds the location/locations of an animal from the locations list
    to the given string"""
    if locations:
        if len(locations) == 1:
            string_output = (
                f"{string_output}      <li><strong>Location:</strong> {locations[0]}</li>\n"
            )
        if len(locations) > 1:
            string_output = f"{string_output}      <li><strong>Locations:</strong> {", ".join(locations)}</li>\n"
    return string_output


def serialize_animal_characteristics(
    characteristics: dict[str, any], string_output: str
) -> str:
    """Add the diet from dict:characteristics of an animal to the given string"""
    if characteristics:
        diet = characteristics.get("diet", None)
        if diet:
            string_output = f"{string_output}      <li><strong>Diet:</strong> {diet}</li>\n"
        skin_type = characteristics.get("skin_type", None)
        if skin_type:
            string_output = f"{string_output}      <li><strong>Skin Type:</strong> {skin_type}</li>\n"
    return string_output


def serialize_animal(animal: dict[str, any]) -> str:
    """Add the data from a animal to the given string"""
    string_output = f'<div class="card__title">{animal['name']}</div>\n'

    characteristics = animal.get("characteristics", None)
    string_output += '<div class="card__text">\n'
    string_output += '  <ul>\n'

    string_output = serialize_animal_characteristics(characteristics, string_output)
    locations = animal.get("locations", None)
    string_output = serialize_animal_location(locations, string_output)
    string_output = serialize_animal_type(characteristics, string_output)

    string_output += '  </ul>\n'
    string_output += "</div>\n"
    return string_output


def serialized_animals_to_html_template(
    animals: dict[str, any], html_template: str
) -> str:
    """Generates an HTML string from the given template and animals data"""
    if animals is None:
        print("No animals data to display")
        return html_template

    string_output = ""
    for animal in animals:
        string_output += f'<li class="cards__item">\n'
        string_output += serialize_animal(animal)
        string_output += f'</li">\n'

    html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", string_output)
    return html_template

def serialize_animal_not_exist(animal_name, html_template: str) -> str:
    
    string_output = ""
    string_output += f'<li class="cards__item">\n'
    string_output += f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>'
    string_output += f'</li">\n'
    
    """
    <body>
        <h1>My Animal Repository</h1>
        <ul class="cards">
            __REPLACE_ANIMALS_INFO__
        </ul>
    </body>    
    """
    
    
    html_template = html_template.replace("__REPLACE_ANIMALS_INFO__", string_output)
    return html_template
