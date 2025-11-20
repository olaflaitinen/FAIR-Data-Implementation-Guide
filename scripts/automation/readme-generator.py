import json
import argparse

def generate_readme(metadata_file, output_file):
    """
    Generates a README.md file from a JSON-LD metadata file.
    """
    try:
        with open(metadata_file, 'r') as f:
            meta = json.load(f)
            
        content = f"# {meta.get('name', 'Dataset Title')}\n\n"
        
        # Description
        content += "## Description\n"
        content += f"{meta.get('description', 'No description provided.')}\n\n"
        
        # Author
        if 'creator' in meta:
            creators = meta['creator']
            if isinstance(creators, list):
                names = [c.get('name', 'Unknown') for c in creators]
                content += f"**Author(s):** {', '.join(names)}\n\n"
            elif isinstance(creators, dict):
                content += f"**Author:** {creators.get('name', 'Unknown')}\n\n"
                
        # License
        content += "## License\n"
        content += f"This dataset is licensed under: {meta.get('license', 'Unknown')}\n\n"
        
        # Keywords
        if 'keywords' in meta:
            keywords = meta['keywords']
            if isinstance(keywords, list):
                content += f"**Keywords:** {', '.join(keywords)}\n\n"
            else:
                content += f"**Keywords:** {keywords}\n\n"
                
        # Citation
        content += "## Citation\n"
        content += "Please cite this dataset as:\n"
        content += "```\n"
        content += f"{meta.get('identifier', 'DOI')}\n"
        content += "```\n"
        
        with open(output_file, 'w') as f:
            f.write(content)
            
        print(f"Successfully generated {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate README from Metadata')
    parser.add_argument('metadata', help='Path to JSON metadata file')
    parser.add_argument('--output', default='README.md', help='Output file path')
    
    args = parser.parse_args()
    generate_readme(args.metadata, args.output)
