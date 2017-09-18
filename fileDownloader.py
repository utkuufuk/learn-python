import random
import urllib.request
from urllib import request

def dowonloadImage(url):
    name = str(random.randrange(1, 1000)) + '.jpg'
    urllib.request.urlretrieve(url, name)

def downloadStockData(url):
    response = request.urlopen(url)
    csv = response.read()
    csvStr = str(csv)               # convert the content to string
    lines = csvStr.split("\\n")     # split the data into lines
    destDir = r'goog.csv' 
    myFile = open(destDir, 'w')

    for line in lines:
        myFile.write(line + "\n")

dowonloadImage("https://avatars2.githubusercontent.com/u/15212283?v=4&u=91c9e7b4c2a718eda82c750a0cd38f04ba3b1069&s=400")
    
stockUrl = "http://www.google.com/finance/historical?q=NASDAQ:GOOG&output=csv"
downloadStockData(stockUrl)
