def times_two(func):
    def init(*args,**kwargs):
        return func(*args, **kwargs)*2
    return init
def asa():
    return "asan"
new_asan = times_two(asan)
print(new_asan())

def get_meerim_func(func):
    def init():
        return func()*2
    return init

@get_meerim_func
def meerim():
    return "Super"
    