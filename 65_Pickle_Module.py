import pickle

# # Pickling a python object means ap kisi bi cheez ko preserve kr ka rkh skty ho nut iska kuch contoversial hain
# like agr apna jb pickle kiya tw version or tha unpickle kiya tw version or tha error generate ho ga
# hos skta hay ksi prserved file ma hack ho or ap jb usay unpack karain twb apka system hack ho jaay
# cars = ["Audi", "BMW", "Maruti Suzuki", "Harryti Tuzuki"]
# file = "66_mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

file = "66_mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))




