# Types of Dictionaries

mydict = {} # empty
print(mydict)

mydict = {1:"Hello",2:"Yoo"} # With int keys
print(mydict)

mydict = {"Hello":"yoo",1:[2,3,4]} # With Mixed keys
print(mydict)

mydict = {"name":"Jack","age":24}
print(mydict)
print(mydict['name'])
print(mydict.get("age"))
print(mydict.get("address"))