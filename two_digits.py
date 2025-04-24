def two_digits(val):
    s=str(val)
    if len(val)==1:
        s="0"+s
    return s

while True:
    value=str((input("Podaj liczbe: ")))
    if value=="0": break
    print(two_digits(value))
   
