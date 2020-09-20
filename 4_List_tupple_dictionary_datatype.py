# List Data type and its function basically it is mutable can change
grocery = ["Soap","Shampo","Rice","Wheat","Almond", 3232] #square bracket list
grocery.insert(2,"salt") #add at specific place
grocery.append("sugar") #add in the end
grocery.remove(3232) #remove function
print(grocery)
print(grocery[0])
print(grocery[4])
num = [32,654,123,456,23234]
print(type(num))
print(max(num))
print(min(num))

# If we talk about tupple it is immutable and cannot be change
numbers = (21,22,23,34,345,435) #parranthsis tupple
print(type(numbers))
print(numbers)

#If we talk about dictionary it is also a data type in python which means some key value pairs
d1 = {}
print(type(d1))
d2= {"Saad":"Malik", "Mani": "Sheikh", "Muaz": "Ansari", "Faizan": "Mughal",
     "SMMF":{"Saad":"Malik", "Mani": "Sheikh", "Muaz": "Ansari", "Faizan": "Mughal"}}
d2["Saim"] = "Ansari"
d2["Anas"] = "jutt"
d2[163] = "AlwaysWait"
print(d2["Saad"])
print(d2["SMMF"])
del d2["SMMF"]

d3 = d2.copy() #Copy of d2 in d3 if not copy simple d2 = d3 then change in d3 also occur in d2
print(d2.keys())
print(d2.items())
print(d2)