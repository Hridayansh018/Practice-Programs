# Different types of tuples

mytup = () # Empty
print(mytup)

mytup = (1,2,3,4,5,6,7,8,9) # Integer 
print(mytup)

mytup = (1,2,"Hello",32.3) # Mixed Data type
print(mytup)

mytup = (1,2,[9,8,7],["yoo","yooi"]) # Nested 
print(mytup)

# Unpacking Tuple
mytup = (1,"hello",54.3)
print(mytup)
a, b, c = mytup
print(a)
print(b)
print(c)

# Having a parantheses is not enogh, we need to have a tailing comma to indicate it as a tuple

mytup = ("Hello")
print(type(mytup))

mytup = ("hello",)
print(type(mytup))

mytup = "hello",
print(type(mytup))

