# serverless-domain-scanner

## Deploy SAM stack

```bash
sam build

sam deploy --guided
```

Review deployment outputs:
* IPRangesTableName
* DomainTableName
* DomainInputBucketName

## Import vendor IPs

Edit import-ip-ranges.py. Update table name to [IPRangesTableName]. 

```bash
python import-ip-ranges.py
```

## Run domain scan

```bash
aws s3 cp ./data/domain-lists/alexa100.txt s3://[DomainInputBucketName]
```

See results in DynamoDB [DomainTableName]


## --notes--

* 80k domain sample, Standard WF, DDB Parallelization x3 = 6:40 min, 200 p/sec
* 80k domain sample, Standard WF, DDB Parallelization x5 = FAIL, SF throttle
* 80k domain sample, EXPRESS WF, DDB Parallelization x6 = 2:20 min, 570 p/sec
* 80k domain sample, EXPRESS WF, DDB Parallelization x10 = 1:20 min, 1000 p/sec

