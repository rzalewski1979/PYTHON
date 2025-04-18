count=0
f1=open("test_file.txt","r")
lines=f1.readlines()
f1=open("test_file.txt","w")
for line in lines:
    count=+1
    s=("line"+str(count)+": "+line)
    f1.write(s)
