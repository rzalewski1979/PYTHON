from datetime import date,datetime
import time
print (date.today())
date_of_birth=date(1979,4,25)
week={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday"\
      ,6:"Saturday",7:"Sunday"}
print(date_of_birth, week[date_of_birth.isoweekday()])
print(datetime.today())
dt=datetime.today()
print("\n"*2)
print("Ide spac")
print("Aktualny czas: ",dt.strftime('%Y.%m.%d, godzina: %H:%M:%S'))
for i in range(1,11):
    print(i)
    time.sleep(1)
dt=datetime.today()
print("Aktualny czas: ",dt.strftime('%Y.%m.%d, godzina: %H:%M:%S'))
date_of_birth=input("podaj date urodzenia [YYYY-MM-DD]: ")
birth_date=datetime.strptime(date_of_birth,'%Y-%m-%d').date()
present_date=date.today()
print("Uplynelo dni : ",present_date-birth_date)
