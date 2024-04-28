#! /usr/bin/env python3
import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.library-archives.pref.fukui.lg.jp/tosyo/index.html')
res.encoding = res.apparent_encoding

soup = BeautifulSoup(res.text ,'html.parser')
o_or_c = soup.find("p").get_text()
print(soup)
