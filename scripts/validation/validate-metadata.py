import json
import jsonschema
from jsonschema import validate

def validate_metadata(metadata_file, schema_file):
    """
    Validates a JSON metadata file against a JSON schema.
    
    Args:
        metadata_file (str): Path to the JSON metadata file.
        schema_file (str): Path to the JSON schema file.
        
    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
            
        with open(schema_file, 'r') as f:
            schema = json.load(f)
            
        validate(instance=metadata, schema=schema)
        print(f"Success: {metadata_file} is valid against {schema_file}.")
        return True
        
    except jsonschema.exceptions.ValidationError as err:
        print(f"Validation Error: {err.message}")
        return False
    except FileNotFoundError as err:
        print(f"File Error: {err}")
        return False
    except json.JSONDecodeError as err:
        print(f"JSON Error: {err}")
        return False

if __name__ == "__main__":
    # Example usage
    # Create a dummy schema for demonstration
    schema = {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "identifier": {"type": "string"},
        },
        "required": ["name", "identifier"]
    }
    
    with open('schema.json', 'w') as f:
        json.dump(schema, f)
        
    # Create a dummy metadata file
    data = {
        "name": "My Dataset",
        "identifier": "10.5281/zenodo.12345"
    }
    
    with open('metadata.json', 'w') as f:
        json.dump(data, f)
        
    validate_metadata('metadata.json', 'schema.json')
