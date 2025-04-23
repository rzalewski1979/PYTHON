import time

class Weels:
    def change_direction(self,left,on):
        print("weels", left ,on)
class Tracks:
    def change_direction(self,left,on):
        print("tracks", left, on)
class Vehicle:
    def __init__(self,controller):
        self.controller = controller
    def turn(self,left):
        self.controller.change_direction(left,True)
        time.sleep(0.25)
        self.controller.change_direction(left,False)
obj1=Vehicle(Weels())
obj2=Vehicle(Tracks())

obj1.turn("left")
obj2.turn("left")
