from wit import Wit
from msSqlQuery import query
import os
import json
import sys
import re

def jsonPrint(text):
	print(json.dumps(text, indent=2))

def getWitResponse(message_text):
	response = client.message(message_text)
	select = formSelect(response)
	where = formWhere(response)
	table = ""
	result = query(select, where, table)
	print(result)

def formQuery(select, where, table):
	finalQueryString = select + table + where
	return finalQueryString


def formSelect(response):
	select = response['entities']['select']
	selects = ""
	for index1, item1 in enumerate(select):
		for index2, item2 in enumerate(select[index1]['entities']['field']):
			selects = selects + ", " + select[index1]['entities']['field'][index2]['value']
	selects = selects[2:]
	if selects == "":
		selects = "*"
	finalSelectString = "SELECT " + selects
	print(finalSelectString)
	return finalSelectString

def formWhere(response):
	evaluate = response['entities']['evaluate']
	wheres = []

	andOrs = []
	for index, item in enumerate(response['entities']['andOr']):
		andOrString = response['entities']['andOr'][index]['value']
		andOrs.append(andOrString)

	for index1, item in enumerate(evaluate):
		evaluateText = evaluate[index1]['value']

		fieldString = ""
		comparisonString = ""
		valueString = ""
		for element in evaluate[index1]['entities']:
			if element == "number":
				valueString = str(evaluate[index1]['entities'][element][0]['value'])
			if element == "field":
				fieldString = evaluate[index1]['entities'][element][0]['value']
			if element == "comparison":
				comparisonString = evaluate[index1]['entities'][element][0]['value']
		if comparisonString == "" or comparisonString == "equal":
			comparisonString = "="
		elif comparisonString == "greaterThan":
			comparisonString = ">"
		elif comparisonString == "lessThan":
			comparison = "<"
		whereString = fieldString + " " + comparisonString + " " + valueString
		wheres.append(whereString)

	finalWhereString = ""
	for index, item in enumerate(andOrs):
		finalWhereString = finalWhereString + " " + wheres[index] + " " + andOrs[index]
	finalWhereString = "WHERE" + finalWhereString + " " + wheres[index+1]
	print(finalWhereString)
	return finalWhereString

witAccessToken = os.environ.get('witAccessToken')
print(witAccessToken)

client = Wit(witAccessToken)

print(sys.version)

anInput = 'what are the terms, description, and premium of policy number 2341 and account number is greater than 4241 and premium is 80'
response = getWitResponse(anInput)
# while True:
# 	#statement = input('Ask for something: ')
# 	#response = getWitResponse(statement)

# 	#print(json.dumps(response,indent=2))
# 	print('--------------------------------------------------------------------------------------')
# # what are the terms, description, and premium of policy number 2341 and account number is greater than 4241



