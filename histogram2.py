from random import randint
counters = {chr(ch):randint(0,100) for ch in range(ord('a'),ord('z')+1)}
print(counters)
sorted_counters=sorted(counters.items(), key=lambda x:x[1])
print(sorted_counters)

