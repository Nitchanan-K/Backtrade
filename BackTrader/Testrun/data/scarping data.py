import pandas as pd
import requests
import time

from  bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/GC%3DF/history?period1=1626652800&period2=1658188800&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
#print(r.status_code)

league_table = soup.find_all('table',class_ = "W(100%) M(0)")
x =soup.find_all("div",attrs={'class':'W(100%) M(0)'})

#<table class="W(100%) M(0)" data-test="historical-prices">

print(league_table)



#<table class="W(100%) M(0)" data-test="historical-prices">














