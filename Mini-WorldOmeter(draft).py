from bs4 import BeautifulSoup as soup
import urllib.request, urllib.parse, urllib.error
import re

print("Welcome to Covid-19 Live update(Country and Continent Based Status)")
print("*******************************************************************")
print("### WORLD Update ###")
print("Loading.....")

main_url = 'https://www.worldometers.info/coronavirus/#country'


#this fuction make soup of the html code for navigaiting at ease
def url_address(url):
	#next 6 lines helps this code to pretend myself as a fake browser.....
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

	#url = "https://www.worldometers.info/coronavirus/country/bangladesh/"
	headers = {
	    'User-Agent': user_agent,
	}

	request = urllib.request.Request(url, None,
	                                 headers)  #The assembled request
	response = urllib.request.urlopen(request)
	data = response.read()  # The data u need
	#6 lines ends here

	bsoup = soup(data, "html.parser")

	return bsoup


container4 = url_address(main_url).findAll("div", {"class": "content-inner"})

#Shows total cases ....
level = 0
for item in container4[0].findAll("span"):
	level += 1
	if level == 1:
		total_cases = item.text
	elif level == 2:
		total_deaths = item.text
	elif level == 3:
		total_recovered = item.text
	else:
		break

print("Total cases:", total_cases)
print("Total Deaths:", total_deaths)
print("Total Recovered:", total_recovered)

print("\n")

while True:

	print("1. Continent wise update")
	print("2. Country wise update")
	print("3. Exit")
	inp = int(input("Enter your choice >>> "))
	print("\n")

	if inp == 1:

		print("Loading......")
		#shows continent based cases......

		main_url = 'https://www.worldometers.info/coronavirus/#country'

		#this fuction make soup of the html code for navigaiting at ease
		def url_address(url):
			#next 6 lines helps this code to pretend myself as a fake browser.....
			user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

			#url = "https://www.worldometers.info/coronavirus/country/bangladesh/"
			headers = {
			    'User-Agent': user_agent,
			}

			request = urllib.request.Request(url, None,
			                                 headers)  #The assembled request
			response = urllib.request.urlopen(request)
			data = response.read()  # The data u need
			#6 lines ends here

			bsoup = soup(data, "html.parser")

			return bsoup

		#it targets the tag/section which contains the continent's names
		container1 = url_address(main_url).findAll("nav", {"class": "ctabs"})

		continent_name = list()
		i = 0

		# this loop iterates through the names of continent
		for item in container1[0].findAll("a"):
			i += 1
			x = item.text
			if i == 1:
				continue
			else:
				continent_name.append(x)

		# **this list enlist names of continents**

		print(continent_name)

		container2 = url_address(main_url).findAll("tbody")

		continent_total_cases = list()
		continent_total_death = list()

		for item in container2[0].findAll(
		    "tr", {"class": "total_row_world row_continent"}):
			x = item.text
			total_case = re.findall(r'\S+\d', x)
			continent_total_cases.append(total_case[0])
			continent_total_death.append(total_case[2])
			#print(total_case)

		# **this enlist the total cases of continents status***
		#print(continent_total_cases)

		# this takes user input to find certain frequency of toal cases.
		user_inp = input('Enter continent name as follows: ')
		print("\n")

		if user_inp in continent_name:
			index = continent_name.index(user_inp)
			print("Total cases in", user_inp, "is",
			      continent_total_cases[index])
			print("Total death cases in", user_inp, "is",
			      continent_total_death[index])
			print("\n")
		else:
			print("NO")

	elif inp == 2:
		#shows country bases status
		print("Loading.....")

		main_url = 'https://www.worldometers.info/coronavirus/country/'
		main_url2 = 'https://www.worldometers.info/coronavirus/#countries'

		#this fuction make soup of the html code for navigaiting at ease
		def url_address(url):
			#next 6 lines helps this code to pretend myself as a fake browser.....
			user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

			#url = "https://www.worldometers.info/coronavirus/country/bangladesh/"
			headers = {
			    'User-Agent': user_agent,
			}

			request = urllib.request.Request(url, None,
			                                 headers)  #The assembled request
			response = urllib.request.urlopen(request)
			data = response.read()  # The data u need
			#6 lines ends here

			bsoup = soup(data, "html.parser")

			return bsoup

		#this prints out total cases+deaths+recovered cases
		def total_cases(name):

			main_url = 'https://www.worldometers.info/coronavirus/country/'
			main_url5 = main_url + name

			container4 = url_address(main_url5).findAll(
			    "div", {"class": "content-inner"})

			level = 0
			for item in container4[0].findAll("span"):
				level += 1

				if level == 1:
					total_cases = item.text
				elif level == 2:
					total_deaths = item.text
				elif level == 3:
					total_recovered = item.text
					break

			print("Total cases:", total_cases)
			print("Total Deaths:", total_deaths)
			print("Total Recovered:", total_recovered)

		container9 = url_address(main_url2).findAll("tbody")
		country_link = list()
		level = 0

		for link in container9[0].findAll("a"):
			level += 1
			data = format(link.get("href"))
			data3 = format(link.text)

			if level % 2 != 0:
				country_link.append(data)

		country_link.sort()

		try:

			name = input("Enter country name in lowercase: ")
			print("\n")
			main_url2 = main_url + name

			container3 = url_address(main_url2).findAll(
			    "div", {"id": "news_block"})

			total_cases(name)
			print("\n")

			print("Updates data of last 7 days", end='\n')
			for item in container3[0].findAll("li", {"class": "news_li"}):
				data = item.text
				for i in range(0, len(data), 1):
					if data[i] != '[':
						print(data[i], end='')
					else:
						break

				print(end='\n')
			print("\n")

		except:

			for item in country_link:
				print(item)

			print(end='\n')
			print("Wrong input....please try agian")
			print(
			    "Find your desired name from the list above(skip\"country and backslash mark\")"
			)
			print(end='\n')
			name = input("Enter country name in lowercase: ")
			print(end='\n')
			main_url2 = main_url + name

			container3 = url_address(main_url2).findAll(
			    "div", {"id": "news_block"})

			total_cases(name)
			print("\n")

			print("Updates data of last 7 days", end='\n')
			for item in container3[0].findAll("li", {"class": "news_li"}):
				data = item.text
				for i in range(0, len(data), 1):
					if data[i] != '[':
						print(data[i], end='')
					else:
						break

				print(end='\n')

			print("\n")
	else:
		print(
		    "-----------------------Coded by FAHAD-----------------------"
		)
		print("Thanks for being with us... :)")
		break

