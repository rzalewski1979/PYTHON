import time
class Student():
    def nap(self,seconds):
        print("Ide spac na",seconds,"sekund")
        for i in range(1,seconds+1):
            print(i)
            time.sleep(1)
        print("Juz")
rafal=Student()
rafal.nap(5)
