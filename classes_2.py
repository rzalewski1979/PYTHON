class Attributes():
    def __init__(self,value=1):
        self.__val = value

object = Attributes()
print(object.__dict__)

object = Attributes(4)
print(object.__dict__)
