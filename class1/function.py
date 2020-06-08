
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        fact = 1
#        for i in range (1,int(n)+1):
#            fact = fact * i
#    return fact
#
#def main():
#    for i in range(1, 11):
#        n = factorial(i)
#        print(n)
#
#main()

def multi(x,y):
    if x == 0 or y == 0
        return 0
    product = 0  
    multi1 = x
    if x < 0:
        multi1 = -multi1
    multi2 = y
    if y < 0:
        multi2 = -multi2
    product = 0
    for loop in range(0, x):
        multi += y
    return multi

def exp(base, power):
    if power == 0:
        return 1
    elif power == 1:
        return base
    otherp = power
    if power < 0: otherp = -otherp
    product = 1
    for loop in range(0, otherp):
        product = multi(product, base)
    if power < 0:
        return 1 / product
    else:
        return product

print(multi(3, 3))
print(exp(3,3))