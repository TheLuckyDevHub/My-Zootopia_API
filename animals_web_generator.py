import file_operations
import serializer


def main():
    """Main function to generate the animals HTML file from JSON data and an HTML template"""
    
    animals_data = file_operations.load_data("animals_data.json")
    if not animals_data:
        print("No animals data to process!!")
        return
    html_template = file_operations.loads_template_html("animals_template.html")
    html_str = serializer.serialized_animals_to_html_template(
        animals_data, html_template
    )
    file_operations.save_html(html_str, "animals.html")


if __name__ == "__main__":
    main()
