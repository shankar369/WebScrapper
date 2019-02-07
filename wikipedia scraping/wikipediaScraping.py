from bs4 import BeautifulSoup
import requests
import csv

#Loading html page
html_page = requests.get('https://en.wikipedia.org/wiki/Bill_Gates').text

soup = BeautifulSoup(html_page,'lxml')

#creating csv file
csv_file = open('data.csv','w',newline='')
csv_writer = csv.writer(csv_file)

#extracting table from html
table = soup.find('table',class_='infobox')
tableBody = table.tbody


#traversing through each row in table to get the data
for trow in table.tbody:
    thead = trow.find('th')
    tdata = trow.find('td')

    try:
        print('head',thead.text)
        print('body',tdata.text)
        #Saving to csv file
        csv_writer.writerow([thead.text,tdata.text])

    except:
        pass

    print()

csv_file.close()
