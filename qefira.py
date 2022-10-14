

from bs4 import BeautifulSoup 
# pip install lxml
#install request library
#pip install requests
import requests
import time

filename = "vehicle.csv"
f= open(filename, "w")

headers = "Adtitle, Price, Build_year, Date, Condition, Make, Transmission, Drive_type, Mileage, Link\n"
f.write(headers)

def vehicle_scrap(weburl):


	html_text = requests.get(weburl).text
	soup = BeautifulSoup(html_text, 'lxml')

	cars = soup.find_all('div', class_ = 'listings-cards__list-item')

	for car in cars:


		Link = car.find('a', class_ = 'listing-card__inner')['href'].replace(' ', '')


		html_text2 = requests.get(Link).text
		soup2 = BeautifulSoup(html_text2, 'lxml')
		autos = soup2.find('div', class_ = 'listing-item__info') 


		try:
			ad_title = autos.find('h1', class_ = 'listing-item__header').text.replace(' ', '')
		except: ad_title = 'N/A'

		try:

			Price = autos.find('span', class_ = 'listing-card__price__value').text.replace(' ', '')
		except: Price = 'N/A' 

		try:

			Date = autos.find('div', class_ = 'listing-item__details__date').text.replace(' ', '')
		except: Date = 'N/A' 
								
		try:

			Conditions = autos.find('dl', class_ = 'listing-item__properties')
			Condition = Conditions.find_all('dd', class_ = 'listing-item__properties__description')[0].text.replace(' ', '')
		except: Condition = 'N/A' 

		try:

			Make = Conditions.find_all('dd', class_ = 'listing-item__properties__description')[1].text.replace(' ', '')
		except: Make = 'N/A' 

		try:

			Transmission = Conditions.find_all('dd', class_ = 'listing-item__properties__description')[3].text.replace(' ', '')
		except: Transmission = 'N/A' 

		try:

			Drive_type = Conditions.find_all('dd', class_ = 'listing-item__properties__description')[4].text.replace(' ', '')
		except: Drive_type = 'N/A' 

		try:

			Mileage = Conditions.find_all('dd', class_ = 'listing-item__properties__description')[5].text.replace(' ', '')
		except: Mileage = 'N/A' 

		try:

			Build_year = Conditions.find_all('dd', class_ = 'listing-item__properties__description')[6].text.replace(' ', '')
		except: Build_year = 'N/A' 


		print(ad_title)
		print(Build_year)
		print("     ")
		print("   ")

		with open('vehicle.csv','a') as f:
			f.write(ad_title.replace(",", "-").strip() + "," + Price.replace(",", "-").strip() + "," +  Build_year.replace(",", "-").strip() + "," + Date.replace(",", "-").strip() + "," + Condition.replace(",", "-").strip() + "," + Make.replace(",", "-").strip() + "," + Transmission.replace(",", "-").strip() + "," + Drive_type.replace(",", "-").strip() + "," + Mileage.replace(",", "-").strip() + "," + Link.replace(",", "-").strip() + "\n")
	
	f.close()	

vehicle_scrap('https://www.qefira.com/cars?page=14')



## Some changes needed are shown here 

# 1. First change Oct 14, 2022

 # 2. Second change Oct 14, 2022

