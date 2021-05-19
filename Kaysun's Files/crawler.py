from os import link
import requests
from bs4 import BeautifulSoup

def steamSpider():

        url = 'https://store.steampowered.com/search'
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        for link in soup.findAll('div', {'class': 'col search_price responsive_secondrow' }):
         titles = link.string
         print(titles)
        
steamSpider()
