from os import strerror
try:
    name=input("Input file name : ")
    s=""
    f1=open(name,"r")
    for line in f1:
        s+=line
    uniq_s=list(set(s))
    uniq_s.sort()
    try:
        uniq_s.remove('\n')
    except:
        pass
    for ch in uniq_s:
        print(ch,"-->",s.count(ch))
    f1.close()
except IOError as e:
    print("I/O Error : ",strerror(e.errno))

