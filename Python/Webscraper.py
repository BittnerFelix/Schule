from bs4 import BeautifulSoup
import requests


url = "https://www.fom.de/hochschulzentren/leipzig/lehrende.html"
html = requests.get(url).text
soup = BeautifulSoup(html, "html.parser")
for item in soup.find("div", {"class":"tx-nfpersonrepo"}).findAll("div", {"class":"fullname"}):
    title = item.find("div", {"class":"title_de"}).get_text()
    name = item.find("div", {"class":"name"}).get_Text()
    print(title+" "+name)


