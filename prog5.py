mylist = [] # Empty list
print(mylist)
mylist = [1,2,3,4,5,6,7,8,9,10] # Integer list
print(mylist)
mylist = [1,"Yoo",4.32] # Mixed data type
print(mylist)
mylist = ["mouse",[1,2,3,4],["a"]]
print(mylist)

# Appending and Extending list

odd = [1,3,5]
odd.append(7)
print(odd)

odd.extend([9,11,13])
print(odd)

# Deleting list items

mylist = ['P','R','O','B','L','E','M']

del mylist[2] # Single item
print(mylist)

del mylist[1:3] # Multiple item
print(mylist)

del mylist # Entire list

print(mylist) # Error
