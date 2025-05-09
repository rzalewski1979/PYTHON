class PizzaError(Exception):
    def __init__(self,pizza,message):
        Exception.__init__(self,message)
        self.pizza=pizza
class TooMuchCheese(PizzaError):
    def __init__(self,pizza,cheese,message):
        PizzaError.__init__(self,pizza,message)
        self.cheese=cheese
def make_pizza(pizza,cheese):
    if pizza not in ["margarita","capriciosa","pepperoni"]:
        raise PizzaError(pizza, "pizza is not available")
    if cheese > 100:
        raise TooMuchCheese(pizza,cheese,"Too much cheese")
    print "The order has been accepted" 
for (pz,ch) in [("margarita",50),("vesuvio",20),("capriciosa",230)]:
    try:
        make_pizza(pz,ch)
    except PizzaError as pe:
        print (pe)
    except TooMuchCheese as tmc:
        print(tmc)
    
