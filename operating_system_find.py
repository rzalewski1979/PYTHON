import os
def find(path,dir):
    os.chdir(path)
    current_dir=os.getcwd()
    for entry in os.listdir():
        if entry==dir:
            print(os.getcwd()+"/"+entry)
        find(current_dir+"/"+entry,dir)
find(input("Enter path: "), input("Enter dir : "))

