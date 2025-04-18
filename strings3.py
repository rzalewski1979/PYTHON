string1=input("Enter string :")
string2=string1.replace(" ","").lower()
for i in range(1,len(string2)+1):
    if (string2[i-1]==string2[-i]):
        check=True
    else:
        check=False
if check:
    print("OK")
else:
    print("Fucking far from ok")

print(string2[::-1])
