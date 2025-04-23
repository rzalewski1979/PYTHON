from os import strerror
count_l=count_ch=0
try:
    for line in open("test_file.txt","rt"):
        count_l+=1
        for ch in line:
            count_ch+=1
            print(ch,end="")
    print("Lines : ",count_l)
    print("Characters : ",count_ch)
except IOError as e:
    print("I/O Error occured: ",strerror(e.errno))
