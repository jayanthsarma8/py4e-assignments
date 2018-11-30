import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
url = input('Enter : ')
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
lis=tree.findall('.//count')
k=0
for i in lis:
    k=k+int(i.text)
    
print(k)
#print(sum(lis))
