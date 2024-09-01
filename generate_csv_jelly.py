from bs4 import BeautifulSoup
import requests
import time

itemcount = 0
totalresults = 1
limit=75
maxprice = 100

while itemcount < totalresults:
    url = "https://items.jellyneo.net/search/?min_price=1&max_price="+str(maxprice)+"&limit="+str(limit)+"&start="+str(itemcount)+""
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    # pls do not ban
    time.sleep(1)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    if(totalresults == 1):
        # total number of items if we don't know it
        results = soup.select_one("body > div.row > div.large-9.small-12.columns.content-wrapper > p:nth-child(4) > b")
        totalresults = int(results.text.replace(",", ""))
        print("total number of results: "+str(totalresults))


    print("parsing "+str(itemcount))
    for name in soup.select('.no-link-icon'):
        if("https://items.jellyneo.net/item/" in name.get('href') and "img" not in str(name)):
         with open("itemsheet.csv", "a") as myfile:
            myfile.write("\n" + name.text)
    
    # move to the next page
    itemcount = itemcount+limit


