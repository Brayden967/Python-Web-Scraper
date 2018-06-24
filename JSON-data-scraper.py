import random
import requests
import simplejson as json
import time
import datetime
from datetime import timedelta
import json

Domain = "https://www.domaintoscrape.com"

# spoof browser request headers
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36',
  'Upgrade-Insecure-Requests': '1',
  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Encoding' : 'gzip, deflate, sdch',
  'Accept-Language' : 'en-US,en;q=0.8,fr;q=0.6,he;q=0.4',
}
date = time.strftime("%Y-%m-%d")

print (date)

# construct base url
URL =\
str(Domain) +\
       "/api/posts.json?end_date="+date+""

print (URL)

# send GET request
rsp = requests.get(URL, headers=headers)

  # check response status code
if (rsp.status_code == 200):
    print ('Connection Made....')
    time.sleep(5) 
else:
    raise Exception("Failed to connect")

  # get JSON data
jsonData = rsp.json()


 # save JSON data
jsonFileName = 'Data ' + (date)
with open(jsonFileName, 'w') as outfile:
    json.dump(jsonData, outfile)


