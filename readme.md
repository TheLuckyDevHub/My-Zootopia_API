# My-Zootopia_API

My-Zootopia_API is a small Python utility that generates static HTML pages for animals by fetching data from an external animals API (via the project data fetcher). The repository includes simple helpers to load JSON data, serialize it into an HTML template, and save the generated files into the `_static/` folder.

This project is intended as a lightweight example of:

- Fetching data from an external API
- Serializing JSON data into an HTML template
- Generating static HTML files for quick local viewing

## Key files

- `animals_web_generator.py` — CLI entry point. Prompts the user for an animal name, fetches data, filters by skin type, and writes an HTML file.
- `file_operations.py` — Utilities for reading JSON and HTML template files and saving generated HTML.
- `serializer.py` — Functions that convert animal JSON objects into the HTML string fragments used in the template.
- `_static/` — Contains HTML templates and target output files.
- `data/` — (Used by data fetcher) contains cached or local data files.

## Prerequisites

- Python 3.8+
- pip

Dependencies are minimal; at least `requests` is required for external data fetching. Install dependencies with:

```powershell
pip install -r requirements.txt
```

## Usage

1. (Optional) Create a virtual environment and activate it.
2. Install dependencies (see above).
3. Run the generator from the repository root:

```powershell
python animals_web_generator.py
```

4. Enter the animal name when prompted (e.g. "elephant").
5. Follow the menu to choose a skin type to filter by (or select 0 for all skin types).
6. The generated HTML file will be saved to `_static/animals_<SkinType>.html` (or `_static/animals_All.html`). If no data is found for the specified animal, `animals_not_exist.html` will be written instead.

## Configuration

- Environment variables: `animals_web_generator.py` calls `load_dotenv()` which will load environment variables from a `.env` file if present. If the data fetcher needs an API key or other credentials, place them in a `.env` file at the project root (for example `API_KEY=your_key`).

## Data flow

1. User inputs an animal name.
2. `data.data_fetcher.fetch_data(animal_name)` is called to retrieve the animals data.
3. The HTML template `_static/animals_template.html` is loaded via `file_operations.loads_template_html()`.
4. `serializer.serialized_animals_to_html_template()` converts fetched JSON into HTML fragments and replaces placeholder tags in the template.
5. The final HTML is saved to `_static/` using `file_operations.save_html()`.

## Development notes

- The serializer assumes each animal JSON object may have keys like `name`, `characteristics` (with `diet`, `skin_type`, `type`) and `locations`.
- Input validation is basic: names shorter than 2 characters are rejected.
- The project includes a minimal `requirements.txt` with `requests`.

## License

Check the repository license (if present) before reusing code.

