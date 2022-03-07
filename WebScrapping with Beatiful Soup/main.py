from bs4 import BeautifulSoup
import requests

url = 'https://www.casasbahia.com.br/c/?filtro=L34743'

headers = {'User Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

print(soup.prettify())