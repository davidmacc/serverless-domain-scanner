import os
import boto3
import botocore

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DOMAINS_TABLE'])


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    file = s3.get_object(Bucket=bucket, Key=key)
    rows = file['Body'].read().decode('utf-8').strip().split('\n')

    with table.batch_writer() as batch:
        for domain in rows:
            batch.put_item(
                Item={'domainName': domain.strip()}
            )
