from os import strerror
try:
    counter=0
    s=open("test_file.txt","rt")
    char=s.read(1)
    while char!='':
        print(char, end='_')
        char=s.read(1)
    s.close()
except IOError as e:
    print("I/O error occured", strerror(e.errno))
