def abc(x,y):
    z= x+y
    n=x-y
    #print('Multiplication =',z)
    return z,n
def sqr(p):
    res =p*p
    # print('Square of p =',h)
    return res

try:
    var,var1=abc(10,15)
    print(var)
    sf=sqr(var)
    # print(var,var1,sep = "\n")
    print(sf)
    # print(z)
except:
    print('Hi')

