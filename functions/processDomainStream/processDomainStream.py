import os
import json
import boto3

client = boto3.client('stepfunctions')
stateMachineARN = os.environ['STATE_MACHINE_ARN']


def lambda_handler(event, context):
    for record in event['Records']:
        if (record['eventName'] == 'INSERT' or record['eventName'] == 'MODIFY'):
            item = record['dynamodb']['NewImage']
            # Only kick-off domain scan if this is new record (i.e. doesn't have a lastUpdated attribute)
            if (not ('lastUpdated' in item)):
                eventid = record['eventID']
                domain = item['domainName']['S']
                print(f"Processing domain '{domain}'")
                response = client.start_execution(
                    stateMachineArn=stateMachineARN,
                    name=eventid,
                    input=json.dumps({'domain': domain})
                )
                print(f"Step Function response: {response}")
