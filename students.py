class StudentsDataException(Exception):
    pass
class WrongLine(StudentsDataException):
    def __init__(self,line_number,line_string):
        super().__init__(self)
        self.line_number=line_number
        self.line_string=line_string
class EmptyFile(StudentsDataException):
    def __init(self):
        super().__init__(self)
from os import strerror
data={}
counter=0
file_name=input("Enter file name: ")
try:
    f1=open(file_name,"rt")
    lines=f1.readlines()
    f1.close()
    if len(lines)==0:
        raise EmptyFile()
    for line in lines:
        counter+=1
        columns=line.split()
        if len(columns)!=3:
            raise WrongLine(counter,line)
        try:
            data[columns[0]+' '+columns[1]]+=float(columns[2])
        except:
            data[columns[0]+' '+columns[1]]=float(columns[2])
    for key,value in data.items():
        print(key," : ",value)
except IOError as e:
    print("I/O Error occured: ",strerror(e.errno))
except WrongLine as e:
    print("Wrong line : ",e.line_number, " line : ",e.line_string)
except EmptyFile as e:
    print("The file is empty")
