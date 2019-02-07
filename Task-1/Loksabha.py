from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import csv






file_name = "LoksabhaMpList.csv"


#creating csv file
csv_file = open(file_name,'w',newline='')
csv_writer = csv.writer(csv_file)




headers = set()

for i in range(30,50):
    page = "https://archive.india.gov.in/govt/loksabhampbiodata.php?mpcode="+str(i)


    #Loading html page
    html_page = requests.get(page,verify = False).text

    soup = BeautifulSoup(html_page,'lxml')

    #extracting table from html

    table = soup.find('table',class_='table1')

    htmlHeaders = table.find_all("strong")

    for hdr in htmlHeaders:
        #print(hdr.text)
        headers.add(hdr.text.strip())



Dict = dict()

print(headers)

for header in headers:
     Dict[header] = []

Dict['otherData'] = []

print(headers)










count = 0

for i in range(30,50):
    print(i)
    page = "https://archive.india.gov.in/govt/loksabhampbiodata.php?mpcode="+str(i)


    #Loading html page
    html_page = requests.get(page,verify = False).text

    soup = BeautifulSoup(html_page,'lxml')

    #extracting table from html

    table = soup.find('table',class_='table1')
    

    trs = table.find_all('tr')
    otherData = ' '
    for trow in trs:
        emptyTable = False
        flag = 1
        

        if(trow.find('strong')!= None):
            for td in trow:
                if(flag == 1):
                    strongText = td.text.strip()
                    #print("head  ",strongText)
                else:
                    tdata = td.text.strip()
                    #print("body  ",tdata)
                    
                    Dict[strongText].append(tdata)

                flag+=1
        else:
            for td in trow:
                otherData+=td.text
                otherData+='|'

        
        print()
        if(emptyTable):
            break
    otherData = otherData.strip()
    Dict['otherData'].append(otherData)

    count+=1
    for header in headers:
        if(len(Dict[header])!=count):
            Dict[header].append(' ')
    
    for header in headers:
        print(len(Dict[header]))


for i in Dict:
    print(len(Dict[i]))



csv_writer.writerow(list(Dict.keys()))


l = list()

for header in Dict:
    l.append(Dict[header])

print(len(l))

l = zip(*l)

for i in list(l):
    csv_writer.writerow(list(i))
    

# for header in Dict:
#     csv_writer.writerow(Dict[header])
