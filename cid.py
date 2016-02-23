import json
import glob
import errno
import sys
import csv

path = 'E:\Courses\independent_study\getLegislators\*.json'

files = glob.glob(path)
with open('cid.csv', 'wb') as csvFile:
	csvWriter = csv.writer(csvFile)
	for fileName in files:
		try:
			with open(fileName) as f:
				data = json.load(f)
				
				if(len(data['response']['legislator'])) > 1:
					for i in data['response']['legislator']:
						csvWriter.writerow(['name', i['@attributes']['firstlast'],'cid',i['@attributes']['cid'],'party', i['@attributes']['party'], 'office', i['@attributes']['office']])
				elif (len(data['response']['legislator'])) == 1:
					csvWriter.writerow(['name', data['response']['legislator']['@attributes']['firstlast'],'cid',data['response']['legislator']['@attributes']['cid'],
										'party', data['response']['legislator']['@attributes']['party'], 'office', data['response']['legislator']['@attributes']['office']])
		except IOError as exc:
			if exc.errno != errno.EISDIR:
				raise