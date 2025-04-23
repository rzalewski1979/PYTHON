birthday=input("Podaj date urodzenia w formacie YYYYMMDD: ")
sum=0
count=0
tmp=birthday
while len(tmp)!=1:
    for ch in tmp:
        digit=int(ch)
        sum+=digit
    tmp=str(sum)
    sum=0
print(f"Twój wynik : {tmp}")
