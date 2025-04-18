tuple1 = (1,2,3)
for elem in tuple1:
    print(elem)
print(3 in tuple1, 5 in tuple1)
print(type(tuple1))
list=list(tuple1)
try:
    a=input("Podaj a: ")
    print(1/a)
except:
    print("Lolaboga")
print(type(list))

