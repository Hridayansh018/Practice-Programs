import time
ltime = time.localtime()
print(time.strftime("%a %b %d %H:%M:%S %z %Y",ltime))


'''
In Time module every charecter is is represented with an > % < before it

a = day
b = month
d = date
H = hour
M = Minutes 
S = Seconds
Z = timezone
Y = year
'''