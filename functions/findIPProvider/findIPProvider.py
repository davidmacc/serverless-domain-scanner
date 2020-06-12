import os
import ipaddress
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['IP_RANGES_TABLE'])
# TODO: paginate scan. Currently 200kb (?), but will eventually hit 1MB Scan limit.
data = table.scan()
ipranges = []
for item in data['Items']:
    ipranges.append({
        'provider': item['provider'],
        'cidr': ipaddress.IPv4Network(item['cidr'])})


def lambda_handler(event, context):
    ip = ipaddress.ip_address(event['ipAddress'])
    for iprange in ipranges:
        if ip in iprange['cidr']:
            return iprange['provider']

    return "UNKNOWN"
