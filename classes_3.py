class Example:
    counter=0
    def __init__(self,val=1):
        self.dupa1=1
        self.__dupa2=2
        Example.counter+=1
object1=Example()
object2=Example(2)
object3=Example(3)

print(object1.counter)
print(Example.counter)
print(object1.dupa1)
print(object1._Example__dupa2)

