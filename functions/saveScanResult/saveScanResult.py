import os
import boto3
import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DOMAINS_TABLE'])


def lambda_handler(event, context):
    event.setdefault('ipaddress', '')
    event.setdefault('provider', '')
    item = {}
    item['domainName'] = event['domain']
    item['dnsResult'] = 'OK' if event['ipaddress'] else 'ERR_NO_DNS_RECORD'
    if event['ipaddress']:
        item['ipaddress'] = event['ipaddress']
    if event['provider']:
        item['provider'] = event['provider']
    item['lastUpdated'] = str(datetime.datetime.now())
    table.put_item(Item=item)
