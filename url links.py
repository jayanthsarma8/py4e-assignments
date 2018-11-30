'''import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter url ')
url('http://py4e-data.dr-chuck.net/known_by_Fikret.html')

k=urllib.request.urlopen(url)
soup = BeautifulSoup(k, 'html.parser')
tags = soup('a')
def url(url):
    k=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(k, 'html.parser')
    tags = soup('a')
    return tags
    for tag in tags :
        if c == 3:
            print(tag.get('href', None))
            url=(tag.get('href'))
            c+=1
            url(url)'''
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input('Enter - ') 
i=0 
while i<8:
    html=urllib.request.urlopen(url).read()
    print ('Retrieving:',url)
    soup=BeautifulSoup(html)
    tags=soup('a')
    url=tags[17].get('href',None)
    i+=1 
