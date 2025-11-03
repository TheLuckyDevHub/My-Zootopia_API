import os
import requests


def fetch_data(to_search_animal):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics': {
        ...
        }
    },
    """
    api_url = "https://api.api-ninjas.com/v1/animals?name={}".format(to_search_animal)

    API_KEY = os.getenv("API_KEY")
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)

    return None
