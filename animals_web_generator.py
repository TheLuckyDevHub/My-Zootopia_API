import json

# Basic color codes
RED = "\033[91m"
RESET = "\033[0m"  # This resets the color back to default


def load_data(file_path: str)-> dict[str, any]:
    """Loads a JSON file"""
    try:
        with open(file_path, "r") as handle:
            try:
                animals_data = json.load(handle)
            except json.decoder.JSONDecodeError as e:
                print(
                    f"{RED}Json file {file_path} could not be loaded JSON decoder error:{RESET} {e.msg}"
                )
            except Exception as e:
                """
                This general exception is here, which can give many other errors, e.g.memory full, no
                write permission etc.so that not so many exceptions have to be found here (bad code), a
                general exception is found at the end and then its error message is output
                """
                print(
                    f"{RED}Try to decode the json {file_path}, JSON decoder error:{RESET} {e}"
                )
    except IOError as e:
        print(f"{RED}Json file {file_path} could not be loaded IO error:{RESET} {e}")
    except Exception as e:
        """
        This general exception is here, which can give many other errors, e.g.memory full, no
        write permission etc.so that not so many exceptions have to be found here (bad code), a
        general exception is found at the end and then its error message is output
        """
        print(f"{RED}Try to load file {file_path}, system error:{RESET} {e}")

    return animals_data


def print_animals(animals: dict[str, any]):
    """Prints the list of animals"""
    for animal in animals:
        print(f"Name: {animal['name']}")
        characteristics = animal.get("characteristics", None)
        if characteristics:
            diet = characteristics.get("diet", None)
            if diet:
                print(f"Diet: {diet}")
        locations = animal.get("locations", None)
        if locations:
            if len(locations) == 1:
                print(f"Location: {locations[0]}")
            if len(locations) > 1:
                print(f"Locations: {", ".join(locations)}")
        if characteristics:
            charac_type = characteristics.get("type", None)
            if charac_type:
                print(f"Type: {charac_type}")
        print()


def main():
    animals_data = load_data("animals_data.json")
    print_animals(animals_data)


if __name__ == "__main__":
    main()
