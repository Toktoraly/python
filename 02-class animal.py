class Animal():
    place = None
    food = None
    def __init__(self,place,food)
    self.place = place
    self.food = place
class Predator(Animal):
    kanattu = None
    food = "meat"

    def __init__(self,place,kanattu):
        self.kanattu = kanattu
        self.place = place
class Trav(Animal):
    muzu = None
    food = "grass"
    def __init__(self,place,muzu):
        self.muzu = muzu
        self.place = place

proud1 = Predator("Africa", True)
print(proud.place)
print(proud1.food)
print(proud1.kanattu)

trav1 = Trav ("Asia", False)
print(trav1.place)
print(trav1.food)
print(trav1.muzu)

