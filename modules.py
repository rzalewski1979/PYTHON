import math
print(math.sin(math.pi/2))
from math import e
print(e)
from math import pi as dupa
print(dupa)
print(dir(math))
import random
print(dir(random))
number=[]
for i in range(10):
    number.append(int(random.random()*10))
    print(number)
number.clear()
for i in range(10):
    number.append(random.randrange(0,100))
    print(number)
number.clear()
for i in range(50):
    number.append(i)
print(number)
for i in range(10):
    print(random.choice(number), end=",")
print("")
from platform import platform
from platform import machine
from platform import processor
from platform import system
print(platform())
print(machine())
print(processor())
print(system())
import os
print(dir(os))
