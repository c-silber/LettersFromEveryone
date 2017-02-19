from twython import Twython
from watson_developer_cloud import ToneAnalyzerV3

import json
import time

CONSUMER_KEY = 'vngBDv6ciW1rbwuP5PpIVnTV8'
CONSUMER_SECRET = 'iT1VOjZoEemZb6jQp62iWRD0OJSdW0uu4e6APoEravXtZgTyjF'
ACCESS_KEY = '833228196489347072-0thhaychaSkP2bx3gLoxmxFlAP9tbHe'
ACCESS_SECRET = 'xrAZI6ikzaFYXJADNJjs5ASlxvSkSuoh6znXkAqzyBlXX'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

tone_analyzer = ToneAnalyzerV3(
	username = "c6f68481-98bb-41cf-9175-f77d6ce6820c",
	password="dAt8yit27znG",
	version='2016-02-11'
)

lis = [833050081641234435] ## this is the latest starting tweet id
for i in range (0, 16):
	user_timeline = twitter.get_user_timeline(screen_name="@realDonaldTrump", count=10, include_retweets=False, max_id=lis[-1])
	
	for tweet in user_timeline:
		tone = json.dumps(tone_analyzer.tone(text=tweet['text']), indent=2)
		parsed_json = json.loads(tone)
		print(parsed_json["document_tone"]["tone_categories"][0]["tones"])
		print(tweet['text'])
		lis.append(tweet['id'])