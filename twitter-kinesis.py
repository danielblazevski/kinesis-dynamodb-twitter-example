## Example to use twitter api and kinesis

from TwitterAPI import TwitterAPI
from boto import kinesis
import json
import twitterCreds

## twitter credentials

consumer_key = twitterCreds.consumer_key
consumer_secret = twitterCreds.consumer_secret
access_token_key = twitterCreds.access_token_key
access_token_secret = twitterCreds.access_token_secret

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = kinesis.connect_to_region("us-east-1")

# if stream is not created, uncomment this line
# kinesis.create_stream(name = "twitter", number_shards = 1)

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
#should clean and use put_records for bulk loads to Kinesis
for item in r:
	kinesis.put_record("twitter", json.dumps(item), "partitionkey") #item["zip_code"]
