from bs4 import BeautifulSoup
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import csv





#finding headers

headers = set()

for i in range(10):
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
# for header in headers:
#     Dict[header] = []


# print(Dict)



# for i in range(9,10):
#     print(i)
#     page = "https://archive.india.gov.in/govt/loksabhampbiodata.php?mpcode="+str(i)


#     #Loading html page
#     html_page = requests.get(page,verify = False).text

#     soup = BeautifulSoup(html_page,'lxml')

#     #extracting table from html

#     table = soup.find('table',class_='table1')
#     otherData = ''
#     print("check")
#     for trow in table:
#         # try:
#         #     if(trow.find('strong') != None):
#         #         th = trow.td.strong.text
#         #         td = trow[1].text.strip()
#         #         print(trow)
#         #     else:
#         #         otherData+=trow[0].text
#         #         otherData+=' | '
#         #         otherData+=trow[1].text

#         # except:
#         #     pass
#         flag = 1    
#         if(trow.find('strong')!= None):
#             for td in trow:
#                 print(td.text)
#                 print()
#             # for td in trow:
#             #     if(flag == 1):
#             #         print("head  ",td.text)
#             #     else:
#             #         print("body  ",td.text)
                

#         #Dict[th].append(td)
#     #print(th,'      ',td)
#     print(otherData)
#     print()
#     # for header in headers:
#     #     print(len(Dict[header]),) 
#     # print()
       
       










'''



'''
#traversing through each row in table to get the data
'''for trow in table.tbody:
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
'''

# csv_file.close()
