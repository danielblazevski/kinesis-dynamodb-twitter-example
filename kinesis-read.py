import boto3
import time
import json

## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis")
#kinesis = kinesis.connect_to_region("us-east-1")
shard_id = "shardId-000000000000" #we only have one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")

shard_it = pre_shard_it["ShardIterator"]
while 1==1:
     out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
     shard_it = out["NextShardIterator"]
     print out;
     time.sleep(1.0)
