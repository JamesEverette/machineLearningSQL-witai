from wit import Wit
import os
import json
import sys


witAccessToken = os.environ.get('witAccessToken')
print(witAccessToken)

client = Wit(witAccessToken)

def getWitResponse(message_text):
	response = client.message(message_text)
	return response

print(sys.version)

while True:
	statement = input('Ask for something: ')
	response = getWitResponse(statement)
	print(json.dumps(response,indent=2))
	print('--------------------------------------------------------------------------------------')
