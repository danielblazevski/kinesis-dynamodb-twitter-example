import boto3
import time
import json
import decimal

## aws creds are stored in ~/.boto

## Connent to the kinesis stream
kinesis = boto3.client("kinesis")
shard_id = 'shardId-000000000000' #we only have one shard!
shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")["ShardIterator"]

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hashtags')

while 1==1:
	out = kinesis.get_records(ShardIterator=shard_it, Limit=100)
	for record in out['Records']:
		if 'entities' in json.loads(record['Data']):
			print(json.loads(record['Data'])['entities']['hashtags'])
			htags = json.loads(record['Data'])['entities']['hashtags']
			if htags:
 				for ht in htags:
					htag = ht['text']	
					try:
						response = table.update_item(
							Key={
								'hashtag': htag 
							},
							UpdateExpression="set htCount  = htCount + :val",
							ConditionExpression="htCount > 0",
							ExpressionAttributeValues={
								':val': decimal.Decimal(1) 	
							},
							ReturnValues="UPDATED_NEW"
						)
					except: 
                                		response = table.update_item(
                                        		Key={
                                                		'hashtag': htag
                                        		},
                                        		UpdateExpression="set htCount = :val",
                                        		ExpressionAttributeValues={
                                                		':val': decimal.Decimal(1)
                                        		},
                                        		ReturnValues="UPDATED_NEW"
                                		)    
	shard_it = out["NextShardIterator"]
#	print out;
	time.sleep(1.0)


