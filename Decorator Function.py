# Decorator that increments the value of another function
def decor(fun):
    def inner():
        res = fun()
        res = res+2
        return res
    return inner
def fun():
    return 50

name = decor(fun)
n=name()
print(n)
