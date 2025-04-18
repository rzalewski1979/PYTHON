def power_of_2(n):
    power=1
    for i in range(n):
        yield power
        power *=2
lista1=[x for x in power_of_2(10)]
print(lista1)

lista2=list(power_of_2(5))
print(lista2)
