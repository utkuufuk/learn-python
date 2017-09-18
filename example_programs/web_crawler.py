import requests
from bs4 import BeautifulSoup

# builds a url from a link objects
def buildUrl(link):
    # some urls don't contain absolute urls
    rawUrl = link.get('href')
    if rawUrl.startswith("http"):
        return rawUrl
    else:
        return "https://thenewboston.com/" + rawUrl

# creates a soup objects from a url
def createSoup(url):
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    return BeautifulSoup(plainText)

# prints the tile and all the links inside an item page
def printItem(url):
    soup = createSoup(url)
    for name in soup.findAll('title'):
        print("Links in", name.string + ":")
    for link in soup.findAll('a'):
        url = buildUrl(link)
        print(url)

def crawl(maxPages):
    page = 1
    while page <= maxPages:
        url = 'https://thenewboston.com/search.php?type=1&sort=pop&page=' + str(page)
        soup = createSoup(url)
        for link in soup.findAll('a', {'class':'user-name'}):
            url = buildUrl(link)
            item = link.string
            print("Crawling:", item)
            printItem(url)
            print()
        page += 1

crawl(1)
