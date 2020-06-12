import requests
from urllib.parse import urlparse


def lambda_handler(event, context):

    domain = event['domain']
    url = 'https://' + domain
    result = {}
    try:
        response = requests.get(url, allow_redirects=False, timeout=5)
        result['status'] = response.status_code
        if ('location' in response.headers):
            redirectUrl = response.headers['location']
            redirectHost = urlparse(redirectUrl).netloc
            result['redirectsTo'] = redirectHost
    except:
        result['status'] = 'ERR_NORESPONSE'

    return result
