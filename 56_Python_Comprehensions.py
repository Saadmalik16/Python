# list = []
# for i in range(100):
#     if i%3==0:
#         list.append(i)
# list = [i for i in range(100) if i%5==0] #list comprehensions jo upr 4 line ma kaam huwa is ma 1 line ma ho gya hay
# print(list)
# dict = {i:f"Item{i}" for i in range(1,11)} #Comprhensive DIctionary
# dict2 = {value:key for key,value in dict.items()} #Traverse Dictionary
# print(dict, "\n", dict2 )
#
# set = {set for set in ["Dress1", "Dress2", "Dress3"]}
# print(set)

generator = (i for i in range(10) if i%2==0)
print(generator.__next__())
print(generator.__next__())
print(generator.__next__())
for item in generator: #only one time iterate we not produce value actually but we are capable to produce value
    print(item)