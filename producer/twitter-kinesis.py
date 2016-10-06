## Example to use twitter api and feed data into kinesis

from TwitterAPI import TwitterAPI
import boto3
import json
import twitterCreds

## twitter credentials

consumer_key = twitterCreds.consumer_key
consumer_secret = twitterCreds.consumer_secret
access_token_key = twitterCreds.access_token_key
access_token_secret = twitterCreds.access_token_secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})

for item in r:
	kinesis.put_record(StreamName="twitter", Data=json.dumps(item), PartitionKey="filler")

