from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
x=re.findall('[0-9]+',str(tags))
c=0
for i in x:
    c=c+int(i)
    
print(c)
