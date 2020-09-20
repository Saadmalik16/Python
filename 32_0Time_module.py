import  time
#
# initial = time.time()
# print(initial)
# a=1
# while(a<50):
#     print("I am Saad")
#     time.sleep(5)
#     a+=1
# print("Total time: ", time.time() - initial , "Seconds")
#
# initial2 = time.time()
# for i in range(5):
#     print("I am Saad")
# print("Total time: ", time.time() - initial2, "Seconds")
localtime = time.asctime(time.localtime(time.time()))
print(localtime)