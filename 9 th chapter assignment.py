na=input("")
ha=open(na)
d=dict()
for i in ha :
    i=i.rstrip()
    if  not i.startswith("From "):
        continue
    wrd=i.split()
    if len(wrd) < 3 :
        continue
    w=str(wrd[1])
    d[w]=d.get(w,0)+1

ma=0
key=None
for l,m in d.items() :
    if m > ma:
        ma = m
        key=w
print(key, ma)
    
