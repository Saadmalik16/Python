# #Lambda function or annonymous function This is only a one liner function
# def add(a,b):
#     return a+b
#
# add = lambda a,b: a+b

a = [[1,6],[3,56],[8,5],[3,5]]
a.sort(key=lambda x:x[1])
print(a)