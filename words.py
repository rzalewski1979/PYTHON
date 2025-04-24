string1=input("Wprowadz ciag znakow : ")
string2=input("Wprowadz szukane slowo : ")
start=0
found=True
for ch in string2:
    result=string1.find(ch,start)
    if result<0:
        print("Slowo nie wystepuje")
        found=False
        break
    else:
        start=result
if found: print("Slowo wystepuje w ciagu znakow")

    
