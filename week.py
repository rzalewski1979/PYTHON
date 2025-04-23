class WeekDayError(Exception):
    pass
class Weeker:
    week=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    
    def __init__(self,day):
        self.__day=day
    def __str__(self):
        return self.__day
    def add_days(self,n):
        numer=(Weeker.week.index(self.__day)+n)%7
        self.__day=Weeker.week[numer]
    def subtract_days(self,n):
        numer=(Weeker.week.index(self.__day)-n)%7
        self.__day=Weeker.week[numer]
try:
    weekday=Weeker("Mon")
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday=Weeker("Monday")
except WeekDayError:
    print("Error")
