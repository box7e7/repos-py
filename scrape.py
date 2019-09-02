from bs4 import BeautifulSoup
import requests
import csv

URL = "https://developers.google.com/public-data/docs/canonical/countries_csv"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'lxml') 
section=soup.find('article', attrs = {'class':'devsite-article-inner'})
section=section.find('div', attrs = {'class':'devsite-article-body clearfix'})
f = csv.writer(open('file.csv', 'w'))
for i in section.table.findAll('tr'):
	li1=[]
	for j in i.findAll('th'):
		li1.append(j.text)
	if len(li1)>0:
		f.writerow(li1)
	li1=[]
	for j in i.findAll('td'):
		li1.append(j.text)
	if len(li1)>0:
		f.writerow(li1)

