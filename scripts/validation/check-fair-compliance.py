import json

def check_fair_compliance(metadata_file):
    """
    Performs a basic check of FAIR compliance based on metadata fields.
    
    Args:
        metadata_file (str): Path to the JSON metadata file.
    """
    try:
        with open(metadata_file, 'r') as f:
            metadata = json.load(f)
            
        score = 0
        total_checks = 4
        
        print(f"Checking compliance for: {metadata_file}")
        
        # F1: Identifier check
        if "identifier" in metadata and metadata["identifier"]:
            print("[PASS] F1: Identifier present.")
            score += 1
        else:
            print("[FAIL] F1: Identifier missing.")
            
        # F2: Rich metadata (simplified check for description)
        if "description" in metadata and len(metadata["description"]) > 50:
            print("[PASS] F2: Description is rich (>50 chars).")
            score += 1
        else:
            print("[FAIL] F2: Description missing or too short.")
            
        # R1.1: License check
        if "license" in metadata and metadata["license"]:
            print("[PASS] R1.1: License information present.")
            score += 1
        else:
            print("[FAIL] R1.1: License information missing.")
            
        # I1: Format check (simplified)
        if "@context" in metadata:
            print("[PASS] I1: JSON-LD context present.")
            score += 1
        else:
            print("[FAIL] I1: JSON-LD context missing.")
            
        print(f"\nFAIR Score: {score}/{total_checks}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    # Example usage
    # Create a dummy metadata file
    data = {
        "@context": "http://schema.org/",
        "identifier": "10.5281/zenodo.12345",
        "description": "This is a very comprehensive description of the dataset that is definitely longer than fifty characters.",
        "license": "https://creativecommons.org/licenses/by/4.0/"
    }
    
    with open('fair_metadata.json', 'w') as f:
        json.dump(data, f)
        
    check_fair_compliance('fair_metadata.json')
