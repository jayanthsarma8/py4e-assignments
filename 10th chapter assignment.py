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
    w=wrd[5].split(':')
    d[w[0]]=d.get(w[0],0)+1

lis=list()
for k,v in d.items():
    new=(k,v)
    lis.append(new)
lis=sorted(lis) #no need to reverse=True here
#lis.sort()
for k,v in lis:
    print(k,v)
