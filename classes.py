class Stack:
    def __init__(self):
        self.stack_list=[]
    def put(self,val):
        self.stack_list.append(val)
    def pop(self):
        val=self.stack_list[-1]
        del self.stack_list[-1]
        return val
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum=0
    def put(self,val):
        self.__sum+=val
        Stack.put(self,val)
    def pop(self):
        val=Stack.pop(self)
        self.__sum-=val
        return val
    def sum(self):
        return self.__sum
    
stack_object=AddingStack()

for i in range(1,11):
    stack_object.put(i)
    print(stack_object.sum())
for i in range(1,11):
    stack_object.pop()
    print(stack_object.sum())
