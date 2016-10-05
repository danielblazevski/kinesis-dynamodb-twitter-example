## script to create a stream to ingest Twitter data
## This does not actually ingest the data, which 
## is done in twitter-kinesis.py

import boto3

kinesis = boto3.client('kinesis')
kinesis.create_stream(StreamName="twitter", ShardCount=1)
