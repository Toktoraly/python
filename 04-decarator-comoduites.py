def check_cart(func):
    def init(*args,**kwarsg):
        if args[0] ==True:
            return func(*args,**kwarsg)
        return "You don not have cart"
    return init

@check_cart
def get_product(cart):
        return "mandarim"
print(get_product(False))

