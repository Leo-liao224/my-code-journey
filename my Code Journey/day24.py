#解包
t1 = (11,14,15,18,16)
t = 11,15,17,18

first,second,*other,last= t1
print(first)
print(second)


a = 10
b = 20
a,b = b,a
print(a)
print(b)



a = 100
b = 200
c = 300
a,b,c = b,c,a

print(a)
print(b)
print(c)
