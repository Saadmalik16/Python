f = open("17_saad.txt")
print(f.tell()) #tell the exact index of file
print(f.readline())
print(f.tell())
f.seek(9) # if we want to show from any index then use seek function file ko kahan sa read krna start karay
print(f.readline())
print(f.tell())
print(f.readline())
f.close()