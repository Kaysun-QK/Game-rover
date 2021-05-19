# This crawler is a test(for now) for getting all the datas from games on https://store.steampowered.com

import re
from os import link
from typing import Pattern
import requests
from bs4 import BeautifulSoup

def steamSpider():

        url = 'https://store.steampowered.com/search'
        sourceCode = requests.get(url)
        plainText = sourceCode.text
        soup = BeautifulSoup(plainText)
        Pattern = r'^https://store.steampowered.com/app/'
        games = soup.findAll('a', href=re.compile(Pattern))
         #titles = link
        print(games)
        
steamSpider()


def main():
    url = 'https://store.steampowered.com/search/results/?query&start=0&count=100'



# all the games on steam with page search "https://store.steampowered.com/search/?page=2"
# a very important url: "https://store.steampowered.com/search/results/?query&start=0&count=100" 
# add "&infinite=1" in the end of the url above to make it infinite
