import os
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DOMAINS_TABLE'])


def lambda_handler(event, context):
    event.setdefault('ipAddress', '')
    event.setdefault('ipProvider', '')
    event.setdefault('httpResponse', {})
    event['httpResponse'].setdefault('status', '')
    event['httpResponse'].setdefault('redirectsToDomain', '')
    
    item = {}
    item['domainName'] = event['domain']
    item['dnsResult'] = 'OK' if event['ipAddress'] else 'ERR_NO_DNS_RECORD'
    if event['ipAddress']:
        item['ipAddress'] = event['ipAddress']
    if event['ipProvider']:
        item['ipProvider'] = event['ipProvider']
    if event['httpResponse']['status']:
        item['httpStatus'] = event['httpResponse']['status']
    if event['httpResponse']['redirectsToDomain']:
        item['redirectsTo'] = event['httpResponse']['redirectsToDomain']
    item['lastUpdated'] = str(datetime.datetime.now())
    table.put_item(Item=item)
