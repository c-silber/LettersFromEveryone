from twython import Twython
from watson_developer_cloud import ToneAnalyzerV3

import sys, os
import lob
import json
import time

CONSUMER_KEY = 'vngBDv6ciW1rbwuP5PpIVnTV8'
CONSUMER_SECRET = 'iT1VOjZoEemZb6jQp62iWRD0OJSdW0uu4e6APoEravXtZgTyjF'
ACCESS_KEY = '833228196489347072-0thhaychaSkP2bx3gLoxmxFlAP9tbHe'
ACCESS_SECRET = 'xrAZI6ikzaFYXJADNJjs5ASlxvSkSuoh6znXkAqzyBlXX'



sys.path.insert(0, os.path.abspath(__file__+'../../..'))
lob.api_key = "test_f80325b79c77e12660e66d2840b1987de6e" ## Find out the actual API key.

test_address = lob.Address.create(
    name = 'Chris Collins',
    description = 'Chris Collins Address',
    metadata = {
        'group': 'Members'
    },
    address_line1 = 'Wehrle Drive',
    address_city = 'Williamsville',
    address_state = 'NY',
    address_country = 'US',
    address_zip = '14221'
)



twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

tone_analyzer = ToneAnalyzerV3(
	username = "c6f68481-98bb-41cf-9175-f77d6ce6820c",
	password="dAt8yit27znG",
	version='2016-02-11'
)

list = [833050081641234435] ## this is the latest starting tweet id
for i in range (0, 16):
	user_timeline = twitter.get_user_timeline(screen_name="@realDonaldTrump", count=10, include_retweets=False, max_id=list[-1])
	
	for tweet in user_timeline:
		tone = json.dumps(tone_analyzer.tone(text=tweet['text']), indent=2)
		parsed_json = json.loads(tone)
		print(parsed_json["document_tone"]["tone_categories"][0]["tones"])
		print(tweet['text'])
		list.append(tweet['id'])
		print_postcard = True
		if (print_postcard):
			## Trigger Lob API to send a postcard.
			print 'Sending a postcard.'

			test_postcard = lob.Postcard.create(
			    description = 'Postcard to Representative',
			    metadata = {
			        'campaign': 'Member welcome'
			    },
			    to_address = test_address,
			    from_address = test_address,
			    front = """
			      <html>
			        <head>
			          <style>
			            @font-face {
			              font-family: 'Roboto';
			              src: url('https://s3-us-west-2.amazonaws.com/lob-assets/LovedbytheKing.ttf');
			            }
			          </style>
			        </head>
			        <body><h1>Hi {{name}}</h1></body>
			      </html>""",
			    data = {
			        'name': test_address.name
			    },
			    message = "To Whom it May Concern, Women are people too.",
			)

			print "Postcard Response"
			print "\n"
			print "======================================================="
			print "\n"
			print test_address
			print "\n"
			print "======================================================="
			print "\n"


