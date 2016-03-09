import urllib2
from bs4 import BeautifulSoup
import csv
import os

assets = "http://www.opensecrets.org/pfds/assets.php?year=2014&cid="
liabilities = "http://www.opensecrets.org/pfds/liabilities.php?year=2014&cid="
transactions="http://www.opensecrets.org/pfds/transactions.php?year=2014&cid="
assets_class = "datadisplay"
liabilities_class = "datadisplay"
transactions_class = "pretty dataTable no-footer"

def getTable(url, cid, selector, cssClass):
	http = url+cid
	#jsb2092 - jeremys github
	request = urllib2.Request(http, headers={'User-Agent' : "Magic Browser"})
	page = urllib2.urlopen(request)
	soup = BeautifulSoup(page)
	table = soup.find("table", {selector : cssClass})
	return table

def parseTable(table, fileName):
	if not os.path.exists(os.path.dirname(fileName)):
		try:
			os.makedirs(os.path.dirname(fileName))
		except OSError as exc:
			if exc.errno != errno.EEXIST:
				raise
	with open(fileName,'wb') as csvFile:
		for row in table.findAll("tr"):
			cells = row.findAll("td")
			if len(cells) == 2:
				org_name = cells[0].text.encode('utf-8')
				values = cells[1].text.encode('utf-8').split()
				if(len(values) == 1):
					low_value =0
					high_value = 0
				else:
					low_value = int(values[0][1:].replace(',',''))
					high_value = int(values[2][1:].replace(',',''))
				csvWriter = csv.writer(csvFile)
				csvWriter.writerow([org_name, low_value, high_value])
			elif len(cells) == 6:
				org_name = cells[0].text.encode('utf-8')
				date = cells[1].text.encode('utf-8')
				liability_term = cells[2].text.encode('utf-8')
				interest_rate = cells[3].text.encode('utf-8')
				ir_type = cells[4].text.encode('utf-8')
				values = cells[5].text.encode('utf-8').split()
				if(len(values) == 1):
					low_value = 0
					high_value = 0
				else:
					low_value = int(values[0][1:].replace(',',''))
					high_value = int(values[2][1:].replace(',',''))
				csvWriter = csv.writer(csvFile)
				csvWriter.writerow([org_name, date, liability_term, interest_rate, ir_type, low_value, high_value])
			elif len(cells) ==4:
				org_name = cells[0].text.encode('utf-8')
				action = cells[1].text.encode('utf-8')
				date = cells[2].text.encode('utf-8')
				value = cells[3].text.encode('utf-8')
				values = value.split(" ")
				if(len(values) == 1):
					low_value =0
					high_value = 0
				else:
					low_value = int(values[0][1:].replace(',',''))
					high_value = int(values[2][1:].replace(',',''))
				csvWriter = csv.writer(csvFile)
				csvWriter.writerow([org_name, action, date, low_value, high_value])

with open('cid.csv', 'r') as csvFile:
	csvReader = csv.reader(csvFile)
	for row in csvReader:
		cid = row[1]
		print row[0]
		fileName = cid + '/' + cid
		assetsTable = getTable(assets, cid, "class", assets_class)
		if assetsTable is not None:
			print 'assets'
			parseTable(assetsTable, fileName + "_assets.csv")
		liabTable = getTable(liabilities, cid, "class", liabilities_class)
		if liabTable is not None:
			print 'liabilities'
			parseTable(liabTable, fileName + "_liabilities.csv")
		tranTable = (getTable(transactions, cid, "id", "transactions"))
		if tranTable is not None:
			print 'transactions'
			parseTable(tranTable, fileName + "_transactions.csv")

"""assetsTable = getTable(assets, 'N00012508', "class", assets_class)
parseTable(assetsTable, "N00012508\N00012508_assets.csv")"""
