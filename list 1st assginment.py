fn=input()
fh=open(fn)
l=[]
word=[]
for i in fh :
    word+=i.split()
    
word.sort()
print(word)

##bellow code is good one


#orfn=input()
#fh=open(fn)
#l=[]
#for i in fh :
#    word=i.split()
#    for j in word:
#        if j in l:
#            continue
#        else :
#            l.append(j)
    
    
#l.sort()
#print(l)
