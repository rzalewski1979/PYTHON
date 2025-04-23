def fib(n):
    elem1=1; elem2=1
    if n<3:
        return 1
    return fib(n-1)+fib(n-2)
for i in range(1,11):
    print(i,"-->",fib(i))
    
