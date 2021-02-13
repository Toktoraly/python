# def sort_numbers(l_num=[]):
#     sort_l=[]
#     for  i in range(len(l_num)):
#         min_num = l_num[0]
#         for num in l_num:
#             if min_num>num:
#                 min_num = num
#         sort_l.append(min_num)
#         l_num.remove(min_num)
#     return sort_l

# class Telefon():
#     def __init__(self, marka, model, screen):
#         self.marka = marka
#         self.model = model
#         self.screen = screen
# telefon1 = Telefon ("samsung","A5","Amoled")

# print(telefon1.marka)
# print(telefon1.model)
# print(telefon1.screen)
class Auto():
    def __init__(self, marka, model,motor_valum,year):
        self.marka = marka
        self.model = model
        self.motor_valum = motor_valum
        self.year = year
auto1 = Auto ("BMW","I3","3","2003")

print(auto1.marka)
print(auto1.model)
print(auto1.motor_valum)
print(auto1.year)