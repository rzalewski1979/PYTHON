data=input("Enter numbers: ")
strings=data.split()
print(strings)
total=0.0
try:
    for ch in strings:
        total+=float(ch)
    print(f"The total is {total}")
except:
    print(f"{ch} is not a number")
print(data[4:]+data[0:4])
for ch in data:
    print(chr(ord(ch)+1))
    
