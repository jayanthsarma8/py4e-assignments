import re
n=input('enter file name')
o=open(n)
s=0
for i in o :
    i.rstrip()
    k=re.findall('[0-9]+',i)
    for j in k :
        s=s+int(j)
print(s)
    
