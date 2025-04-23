string = 'abcdefghijklmnoprstuwyz'
print(string[7])
print(tuple(string),list(string),string.index("k"),sep='\n')
print(string.count("k"))
string2= """chuj
dupa
i kamieni
kupa
"""
print(string2)
string_list=list(string)
print(string_list)
print("|".join(string_list))
string3="|".join(string_list)
print(string3.replace("|","---"))
a="77"
print(f'Szczesliwy numet to {a}')
print(string3.replace("|"," ").split())
print(string3.upper().lower())
list_unsorted=[1,4,8,2,6,3,9]
print(sorted(list_unsorted))
