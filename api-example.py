import requests
import json

def connect_to_api(url, method='GET', params=None, headers=None):
    """
    Connect to an API and return the response

    Args:
        url (str): The URL of the API
        method (str): The HTTP method to use
        params (dict): The parameters to send
        headers (dict): The headers to send

    Returns:
        dict: The JSON response
        response (requests.Response): The response object
    """

    try:
        response = requests.request(method, url, params=params, headers=headers)
        response.raise_for_status() # Raise an exception for 4xx and 5xx status codes
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
# Example usage
if __name__ == '__main__':
    url = "https://fake-json-api.mock.beeceptor.com/companies"
    response = connect_to_api(url)

    if response:
        print("API Response:")
        print(json.dumps(response.json(), indent=4))