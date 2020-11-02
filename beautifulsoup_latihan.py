import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.kompas.com")

print(result.status_code)
#200 means accessable

print(result.headers)

source = result.content
print(source)

soup = BeautifulSoup(source, 'lxml')

links = soup.findall("a")
print(links)
print("\n")