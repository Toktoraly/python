class Product():
    def __init__(self,name,price):
        self.name = name
        self.price = price
class Category():
    products = []
    def  __init__(self,name):
        self.name = name
    def set_product(self,a):
        self.products.append(a)

    def get_product(self):
        result = []
        for i in self.products:
            result.apend(i.name)
        return result
    
    def get_count(self):
        return len (self.products)
    
    def get_price_product(self):
        summa = 0
        for i in self.products:
            summa+=i.price
        return summa

product1 = Product("shirt", 200)
product2 = Product("T-shit", 100)
product3 = Product("kepka", 150)

category1 = Category("summer")

category1.set_product(product1)
category1.set_product(product2)
category1.set_product(product3)
for i in category1.products:
    print(i.name)
    
print(category1.get_price_product())

[
    product1,
    product2,
    product3
]
