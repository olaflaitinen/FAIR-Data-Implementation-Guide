import json
from datetime import date

def generate_dataset_metadata(title, author, description, keywords):
    """
    Generates a JSON-LD metadata object for a dataset.
    
    Args:
        title (str): Title of the dataset.
        author (str): Name of the author.
        description (str): Description of the dataset.
        keywords (list): List of keywords.
        
    Returns:
        dict: The metadata object.
    """
    metadata = {
        "@context": "http://schema.org/",
        "@type": "Dataset",
        "name": title,
        "creator": {
            "@type": "Person",
            "name": author
        },
        "description": description,
        "keywords": keywords,
        "datePublished": str(date.today()),
        "license": "https://creativecommons.org/licenses/by/4.0/"
    }
    return metadata

if __name__ == "__main__":
    # Example usage
    title = input("Enter dataset title: ")
    author = input("Enter author name: ")
    description = input("Enter dataset description: ")
    keywords_input = input("Enter keywords (comma separated): ")
    keywords = [k.strip() for k in keywords_input.split(',')]
    
    metadata = generate_dataset_metadata(title, author, description, keywords)
    
    filename = "generated_metadata.json"
    with open(filename, 'w') as f:
        json.dump(metadata, f, indent=2)
        
    print(f"Metadata saved to {filename}")
