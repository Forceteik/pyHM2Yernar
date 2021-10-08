import requests
import datetime
from bs4 import BeautifulSoup

now = datetime.datetime.now()

print ("Latest information in market for " + now.strftime("%d-%m-%Y %H:%M") + ": \n")

class Scrapper:
    def get(self, currency_name):
        page = requests.get(
            "https://google.com/search?q=site%3Acoinmarketcap.com+" + currency_name + "&ie=utf-8&oe=utf-8")
        soup = BeautifulSoup(page.content, 'html.parser')
        post = soup.find_all("h3")
        return post

scrapper = Scrapper()
res = scrapper.get("bitcoin")

for i in res:
    print(i.find("div").get_text())