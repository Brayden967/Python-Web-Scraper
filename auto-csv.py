import random
import requests
import simplejson as json
import time
import datetime
from datetime import timedelta
import json
import csv
 
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

#Allows you to confirm data format is correct, this is only needed if you plan on using the date variable in JSON URL.
print (date)

# construct base url
URL =\
str(Domain) +\
       "/api/posts.json?end_date="+date+""

print (URL)

#This should print https://www.domaintoscrape.com/api/posts.json?end_date="THEDATE"

# send GET request
rsp = requests.get(URL, headers=headers)

  # check response status code
if (rsp.status_code == 200):
    print ('Connection Made....')
    time.sleep(5) 
else:
    raise Exception("Failed to connect")
 
  # get JSON data
csvFileName = 'MyData ' + (date)+".csv"
csvfile = open(csvFileName, "a+")
csvfile.write("Data_Column_1,Data_Column_2,Data_Column_3")
csvfile.close()
jsonData = rsp.json()
for i in range (len(jsonData["JSON"][0]["DATASET-NAME"])):
    try:
        csvfile = open(csvFileName, "a+")
        print(str(jsonData["Data"][0]["Column"][i]["1"]))
        csvfile.write(str(jsonData["Data"][0]["Column"][i]["1"])+",")
        csvfile.close()
    except:
        csvfile = open(csvFileName, "a+")
        print("not found")
        csvfile.write("not found" + ",")
        csvfile.close()
    try:
		csvfile = open(csvFileName, "a+")
        print(str(jsonData["Data"][0]["Column"][i]["2"]))
        csvfile.write(str(jsonData["Data"][0]["Column"][i]["2"])+",")
        csvfile.close()
    except:
        csvfile = open(csvFileName, "a+")
        print("not found")
        csvfile.write("not found" + ",")
        csvfile.close()
    try:
        csvfile = open(csvFileName, "a+")
        print(str(jsonData["Data"][0]["Column"][i]["2"]))
        csvfile.write(str(jsonData["Data"][0]["Column"][i]["2"])+",")
        csvfile.close()
    except:
        csvfile = open(csvFileName, "a+")
        print("not found")
        csvfile.write("not found" + ",")
        csvfile.close()
    
 # save JSON data
jsonFileName = 'MyData ' + (date)+".json"
with open(jsonFileName, 'w') as outfile:
    json.dump(jsonData, outfile)