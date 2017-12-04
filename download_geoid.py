import requests
from bs4 import BeautifulSoup
import csv

#Buat file csv untuk menyimpan nilai koordinat dan undulasi geoid
f= csv.writer(open('geoid_indo_srgi.csv', 'w', newline=''))
f.writerow(['lat', 'long', 'N'])

#Extent area yang akan didownload dan spasi antar titik samplingnya (dalam derajat)
xmin=118.943
ymin=-3.4
xmax=120.069
ymax=-2.688
interval = 0.008333

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step
for b in frange(xmin,xmax, interval):
	#print(b)
	for l in frange(ymin, ymax, interval):
		#print('http://srgi.big.go.id/srgi2/api/decimal-count?lat='+str(l)+('&lon=')+str(b))
		#page =requests.get('http://srgi.big.go.id/srgi2/api/decimal-count?lat='+str(l)+'&lon='+str(b))
		page = requests.get('http://srgi.big.go.id/peta/geoIdEvalServlet?lat='+str(l)+'&lon='+str(b))
		soup = BeautifulSoup(page.text, 'html.parser')
		latV = soup.find_all('th')[1].get_text()
		lonV = soup.find_all('th')[3].get_text()
		gdiV = soup.find_all('td')[18].get_text()
		print(latV,lonV,gdiV)
		f.writerow([latV, lonV, gdiV])

