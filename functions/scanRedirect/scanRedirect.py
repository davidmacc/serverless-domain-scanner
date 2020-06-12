import os
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DOMAINS_TABLE'])


def lambda_handler(event, context):
    print(event)
    if ('redirectsToDomain' in event['httpResponse']):
        domain = event['domain'].lower()
        redirectDomain = event['httpResponse']['redirectsToDomain'].lower()
        # if we're being redirected to a subdomain then
        # add it to the scan table
        print(domain)
        print(redirectDomain)
        if (redirectDomain != domain and redirectDomain.endswith(domain)):
            print(f"Adding subdomain for scanning: '{redirectDomain}'")
            item = {'domainName': redirectDomain}
            table.put_item(Item=item)
