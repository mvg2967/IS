import urllib2
from bs4 import BeautifulSoup
import csv
#house votes go to h001-h564
#sentave votes go to s001-ss366

# for i in range(1,367):
# 	s.append(i)
def getCSV(http, vote_number):
	request = urllib2.Request(http,  headers={'User-Agent' : "Magic Browser"})
	response = urllib2.urlopen(request)
	csv = response.read()
	open('C://Users/mark/Desktop/' + vote_number + '.csv','wb').write(csv)

def main(n)
	for i in range(1,n):
		before_url = 'https://www.govtrack.us/congress/votes/113-2014/h'
		after_url = '/export/csv'
		vote_number = 'h' + '%03d'%i
		http = before_url + '%03d'%i + after_url
		getCSV(http, vote_number)

main(367)
main(565) 