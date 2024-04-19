s1 = float(input("enter the length of first side:- "))
s2 = float(input("enter the length of second side:- "))
s3 = float(input("enter the length of third side:- "))

if s1**2 == s2**2 + s3**2 or s2**2 == s1**2 + s3**2 or s3**2 == s2**2 + s1**2:
    print("it is a right angled triangle")

elif s1 == s2 or s1 == s3 or s2 == s3:
     print("it is a isoscalas triangle")

else:
    print("it is a scalen triangle")