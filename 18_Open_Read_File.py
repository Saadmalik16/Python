f = open("17_saad.txt")
#content = f.read()
#print(content) #for whole content read
#content = f.read(10) #on choice how many content read
#print(content)
#print(f.readline()) # for one line read
#print(f.readlines()) #for read in form of list
for line in f:
    print(line) #print every line with backspaces
f.close()