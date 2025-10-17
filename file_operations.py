import json

# Basic color codes
RED = "\033[91m"
RESET = "\033[0m"  # This resets the color back to default


def load_data(file_path: str) -> dict[str, any]:
    """Loads a JSON file"""
    animals_data = None
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


def read_template_html(file_path: str) -> str:
    """Reads an HTML template file and returns its content as a string"""
    try:
        with open(file_path, "r") as handle:
            return handle.read()
    except IOError as e:
        print(f"{RED}HTML template file {file_path} could not be loaded IO error:{RESET} {e}")
    except Exception as e:
        print(f"{RED}Try to load file {file_path}, system error:{RESET} {e}")
    return ""

def save_html(html_str: str, file_path: str) -> None:
    """Saves the given HTML string to a file"""
    try:
        with open(file_path, "w") as handle:
            handle.write(html_str)
    except IOError as e:
        print(f"{RED}HTML file {file_path} could not be saved IO error:{RESET} {e}")
    except Exception as e:
        print(f"{RED}Try to save file {file_path}, system error:{RESET} {e}")

