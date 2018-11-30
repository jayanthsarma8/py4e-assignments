import urllib.request, urllib.parse, urllib.error
import json
k=input('Enter url: ')
uh=urllib.request.urlopen(k)
data = uh.read().decode()
js=json.loads(data)
print( 'Retrived %d charecters' % len(data))
#print(js['comments'])
su=0
for i in js['comments']:
    su+=i['count']
print(su)
    
