import requests
from bs4 import BeautifulSoup

def steamSpider():

        url = 'https://store.steampowered.com/search'
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('span', {'class': 'title'}):
            href = link.get('href')
            print(href)
        
steamSpider()
