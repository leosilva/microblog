from flask_babel import _
import requests

# URL to retrieve the list of endpoints
endpoints_url = 'https://raw.githubusercontent.com/Uncover-F/TAS/Uncover/.data/endpoints.json'


# Function to send GET request to an endpoint
def _send_request(url, params):
    try:
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f'Error at {url}: {response.status_code} - {response.text}')
            return None
    except requests.RequestException as e:
        print(f'Request exception at {url}: {e}')
        return None


def translate(post, source_language, target_language):
    # Parameters for translation (customize as needed)
    params = {
        'text': post,
        'source_lang': source_language,  # Source language code
        'target_lang': target_language   # Target language code
    }

    # Get the list of endpoints
    try:
        endpoints_response = requests.get(endpoints_url)
        if endpoints_response.status_code == 200:
            endpoints = endpoints_response.json()
        else:
            print(f'Error fetching endpoints: {endpoints_response.status_code} - {endpoints_response.text}')
            endpoints = []
    except requests.RequestException as e:
        print(f'Request exception fetching endpoints: {e}')
        endpoints = []

    # Try each endpoint until one works
    result = None
    for endpoint in endpoints:
        result = _send_request(endpoint, params)
        if result is not None:
            break

    # Print the result or an error message
    if result is not None:
        return result['response']['translated_text']
    else:
        return _('Error: the translation service is not configured.')