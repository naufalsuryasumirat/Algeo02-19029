import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.vice.com/id")
#print(result.status_code)
source = result.content
soup = BeautifulSoup(source, 'lxml')

list_url = []
for h3_tag in soup.find_all('h3'):
    a_tag = h3_tag.find('a')
    list_url.append(a_tag.attrs['href'])

for link in range (len(list_url)):
    print(list_url[link])

  

print(requests.codes.ok)