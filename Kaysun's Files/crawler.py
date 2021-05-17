###test
import requests
from bs4 import BeautifulSoup

def steamSpider(maxAmount):
    Amount = 10
    while Amount <= maxAmount:
        url = 'https://store.steampowered.com/search'
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('a', {'class': 'title'}):
            href = link.get('href')
            print(href)
        Amount += 1


steamSpider(3)
