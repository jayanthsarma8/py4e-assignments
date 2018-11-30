fname = input("Enter file name: ")

fh = open(fname)
count = 0
for i in fh:
    i=i.rstrip()
    if  not i.startswith('From'):
        continue
    word =i.split()
    if len(word)<4:
        continue
    else:
        print(word[1])
        count=count+1
print("There were", count, "lines in the file with From as the first word")
