#for loop la sth else tn=b lagta hay jb for loop hamara end ho jaay or forr
# loop hamara 2 surat ma end hota hay agr tw list khtm ho jaay
# ya string iterate ho jaay ya loop ma koi break statement mill jaay tb

College = ["PGC", "KIPS", "SIAC", "TIPS"]
for item in College:
    if item == "TIPS":
        break
    #print(item)
else:
    print("For loop End Successfully")