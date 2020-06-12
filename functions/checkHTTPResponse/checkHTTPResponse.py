import requests
from urllib.parse import urlparse


def lambda_handler(event, context):

    domain = event['domain'].lower()
    url = 'https://' + domain
    result = {}
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        result['status'] = response.status_code
        if ('location' in response.headers):
            redirectUrl = response.headers['location']
            redirectDomain = urlparse(redirectUrl).netloc.lower()
            result['redirectsToDomain'] = redirectDomain
    except:
        result['status'] = 'ERR_NO_RESPONSE'

    return result
