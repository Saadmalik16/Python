a = [1,2,3,4,5,6,7,8,9,0]
s = set (a) # in set best oppertunity to use the list data type
print(type(s))
s1 = set ([1,2,3,4,56])
s.add(10)
s.remove(1)
s.intersection(s1)
s.union(s1)
print(s.union(s1))
print(s.intersection(s1))
print(s)