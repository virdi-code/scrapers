from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.coingecko.com/en/crypto-gainers-losers")

#print(page.status_code)
#print(page.content)

soup = BeautifulSoup(page.content,'html.parser')
#print(soup)

table = soup.find_all('table')
rows = table[0].find_all('tr')
print("GAINERS")
for r in rows:
    rp = ""
    a = r.find('span',{"class":"tw-hidden"})
    if(a):
        rp = rp + a.text.strip() + ','

    a = r.find('span',{"class":"font-bold"})
    if(a):
        rp = rp + a.text.strip() + ','
    
    a = r.find('span', {"data-coin-symbol":True})
    if(a):
        rp = rp + a.text.strip() + ','
    a = r.find('span', {"data-24h":True})
    if(a):
        rp = rp + a.text.strip()
    print(rp)


#LOSERS
table = soup.find_all('table')
rows = table[1].find_all('tr')

print("\n\nLOSERS")
for r in rows:
    rp = ""
    a = r.find('span',{"class":"tw-hidden"})
    if(a):
        rp = rp + a.text.strip() + ','

    a = r.find('span',{"class":"font-bold"})
    if(a):
        rp = rp + a.text.strip() + ','
    
    a = r.find('span', {"data-coin-symbol":True})
    if(a):
        rp = rp + a.text.strip() + ','
    a = r.find('span', {"data-24h":True})
    if(a):
        rp = rp + a.text.strip()
    print(rp)
