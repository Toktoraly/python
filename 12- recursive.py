
# def sumto:
#     print ("Hello")
#     return sumto()
def sumto(n):
    print (n)
    if n<1:
        return 1
    return n*sumto(n-1)

print(sumto(100))