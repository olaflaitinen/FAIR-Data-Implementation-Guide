import requests
import json

def create_zenodo_deposition(token, metadata):
    """
    Creates a new deposition in Zenodo (sandbox) to reserve a DOI.
    
    Args:
        token (str): Zenodo API token.
        metadata (dict): Metadata for the deposition.
        
    Returns:
        dict: The response from Zenodo.
    """
    headers = {"Content-Type": "application/json"}
    params = {'access_token': token}
    
    # Use sandbox for testing
    url = 'https://sandbox.zenodo.org/api/deposit/depositions'
    
    response = requests.post(url, params=params, json={}, headers=headers)
    
    if response.status_code == 201:
        print("Deposition created successfully.")
        return response.json()
    else:
        print(f"Error creating deposition: {response.status_code}")
        print(response.json())
        return None

if __name__ == "__main__":
    # NOTE: This is an example script. You need a valid API token.
    # TOKEN = "YOUR_ZENODO_TOKEN"
    
    print("This script demonstrates how to create a DOI using the Zenodo API.")
    print("Please obtain an API token from https://sandbox.zenodo.org/account/settings/applications/tokens/new/")
