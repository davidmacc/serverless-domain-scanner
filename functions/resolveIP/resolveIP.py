import socket


def lambda_handler(event, context):
    try:
        domain = event['domain']
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        raise Exception('DNSError')
