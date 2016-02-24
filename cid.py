import json
import glob
import errno
import sys
import csv

path = 'E:\Courses\independent_study\getLegislators\*.json'

files = glob.glob(path)
with open('cid.csv', 'wb') as csvFile:
	csvWriter = csv.writer(csvFile)
	csvWriter.writerow(['name', 'cid','party','office'])
	for fileName in files:
		try:
			with open(fileName) as f:
				data = json.load(f)
				
				if(len(data['response']['legislator'])) > 1:
					for i in data['response']['legislator']:
						csvWriter.writerow([i['@attributes']['firstlast'],i['@attributes']['cid'], i['@attributes']['party'], i['@attributes']['office']])
				elif (len(data['response']['legislator'])) == 1:
					csvWriter.writerow([data['response']['legislator']['@attributes']['firstlast'],data['response']['legislator']['@attributes']['cid'],
									data['response']['legislator']['@attributes']['party'], data['response']['legislator']['@attributes']['office']])
		except IOError as exc:
			if exc.errno != errno.EISDIR:
				raise