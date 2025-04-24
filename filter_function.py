from random import seed,randint
list1= [randint(-100,100) for x in range(10)]
print(list1)
list2=list(filter(lambda x: x>0, list1))
print(list2)
