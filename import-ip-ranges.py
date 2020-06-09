####
IPRANGES_DYNAMO_TABLE = 'domainscan01-IPRangesTable-1LITHZQBFRJLF'
####

import boto3

def importfile(filename, providerName):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(IPRANGES_DYNAMO_TABLE)
    print(f"Importing IP Ranges for '{providerName}'...")
    with open(filename, "r") as file:
        with table.batch_writer() as batch:
            for line in file:
                batch.put_item(Item={'cidr': line.strip(),
                                     'provider': providerName})


importfile('./data/vendor-ip-ranges/akamai-ipv4-ranges.csv', 'Akamai')
importfile('./data/vendor-ip-ranges/aws2-ipv4-ranges.csv', 'AWS')
importfile('./data/vendor-ip-ranges/azure-ipv4-ranges.csv', 'Azure')
importfile('./data/vendor-ip-ranges/cloudflare-ipv4-ranges.csv', 'Cloudflare')
importfile('./data/vendor-ip-ranges/cloudfront-ipv4-ranges.csv', 'AWS.CloudFront')
importfile('./data/vendor-ip-ranges/fastly-ipv4-ranges.csv', 'Fastly')
importfile('./data/vendor-ip-ranges/gcp-ipv4-ranges.csv', 'GCP')
importfile('./data/vendor-ip-ranges/incapsula-ipv4-ranges.csv', 'Incapsula')
