data=[]
for r in range(1,4):
    check=False
    while not check:
        number=input("Enter number: ")
        check=(len(number)==9 and number.isdigit())
        if not check:
            print("Enter correct number")
    data.append(number)
print(data)
col=[]
for i in range(9):
    for j in range (3):
        col.append((data[j][i]))
print(col)

        
