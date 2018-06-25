# you must install beautifulsoup to use this code. 

# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import time
import datetime
from datetime import timedelta

# importing time, datetime, and timedelta are not neccesary unless you plan on scraping dynamic date ranges.ou 

Domain = "https://www.domaintoscrape.com"

# spoof browser request headers
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
  'Upgrade-Insecure-Requests': '1',
  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Encoding' : 'gzip, deflate, sdch',
  'Accept-Language' : 'en-US,en;q=0.8,fr;q=0.6,he;q=0.4',
}

page = requests.get(Domain, headers = headers)

soup = BeautifulSoup(page.text, 'html.parser')

divitem = soup.find(class_='div-class-name')


# grab all text from p tags within the div inserted above

pitem = divitem.find_all('p')

