list1=[x for x in range(6)]
list2=list(map(lambda x:x**2, list1))
print (list2)

for x in map(lambda x:x**2, list1):
    print (x, end= " ")
print()
