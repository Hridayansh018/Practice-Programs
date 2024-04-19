temp = float(input("enter temp:- "))
unit = input("enter unit in 'C' or 'F' :-  ")

if unit == 'C' or 'c':
    newtemp = 9/5*temp + 32
    print("temperature in Faranhite is =",newtemp)

elif unit == 'F' or 'f':
    newtemp = 5/9*temp - 32
    print("temperature in Celcius is =",newtemp)

else:
    print("Unknown Unit",unit)

