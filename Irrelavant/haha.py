import string
a=12321
b=str(a)
b=eval(b[len(b)::-1])
print(a==b)