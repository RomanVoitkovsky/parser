import requests
from bs4 import BeautifulSoup
import csv


def write_csv(result):
    with open('select.homes.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, dialect='excel', fieldnames=['name', 'phone', 'region', 'ad_url'])
        writer.writeheader()
        for item in result:
            writer.writerow(item)


url_list = 'https://select.homes/realty'

# response = requests.get(url_list)
# soup = BeautifulSoup(response.text, 'lxml')

result = []
for i in range(1, 50 + 1):
    print('Parsing page # ' + str(i) + ' of ' + str(50))
    adpageurl = url_list + '?page=' + str(i)
    adpage = requests.get(adpageurl)
    adpagesoup = BeautifulSoup(adpage.text, 'lxml')
    alist = adpagesoup.find_all('a', class_='css-1rmv58g')
    for a_element in alist:
        ad_url = 'https://select.homes' + a_element.get('href')

        adresponse = requests.get(ad_url, allow_redirects=True)
        adpage = BeautifulSoup(adresponse.text, 'lxml')

        phone = adpage.find('a', class_='css-1b6gwwz')
        item = {'phone': phone.text, 'ad_url': ad_url, }
        result.append(item)

write_csv(result)

# write_csv(result)
#
# urls = soup.find_all('a', class_='catalog-card-media')
#
# for url in urls:
#     links = 'https://rieltor.ua' + url.get('href')
#
#     print(links)
#
#     adresponse = requests.get(links, allow_redirects=True)
#     adpage = BeautifulSoup(adresponse.text, 'lxml')
#
#
#
