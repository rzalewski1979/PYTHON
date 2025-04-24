dictionary = {1:'jeden', 2:'dwa', 3:'trzy',4:'cztery',5:'piec'}
dictionary[1]+="kuna"
dictionary2={1:('zebra',),2:"jenot"}
for key in dictionary.keys():
    print (key,"---->",dictionary[key])
for value in dictionary.values():
    print (value)
print (dictionary2)
dictionary2[1]+=("kuna",)
print(dictionary2)
del dictionary[1]
print (dictionary)
dictionary.popitem()
print(dictionary)
for key,value in dictionary.items():
    print(key)
