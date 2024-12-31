from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'http://olympus.realpython.org'
page = urlopen(url + '/profiles')
html = page.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

for link in soup.find_all('a'):
    print(url + link['href'])