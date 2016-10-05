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
#kinesis = kinesis.connect_to_region("us-east-1")

# if stream is not created, uncomment this line
# kinesis.create_stream(name = "twitter", number_shards = 1)

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
tweets = []
for item in r:
	record = {'Data':json.dumps(item), 'PartitionKey':"filler"}
	tweets.append(record)
	kinesis.put_record(StreamName="twitter", Data=json.dumps(item), PartitionKey="filler")

#kinesis.put_records(Records=tweets,StreamName="twitter")

