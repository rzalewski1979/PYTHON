def Fib(n):
    first=second=1
    for i in range(n+1):
        if i in [1,2]:
            yield 1
        if i>2:
            sum=first+second
            first,second=second,sum
            yield sum
list = [x for x in Fib(10)]
print (list)
