
f1 = open("harry.txt")

try: #firstly program run start from try
    f = open("does2.txt")

except EOFError as e: #agr try wala code ni chlta tw except ka chalay ga or ap ak sa zyada except statement likh skty
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else: #agr try wala code chalay or except wala na chalay tw else bi try ka sth chalay ga
    print("This will run only if except is not running")

finally: #finally used for clean up code ya haar haal ma chalay ga hi chalay ga
    print("Run this anyway...")
    # f.close()
    f1.close()

print("Important stuff")
