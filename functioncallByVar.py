# def sqr(x):
#     return x*x
# x = sqr(5)
# print(x)

def func1(hi):
    res = hi()
    return 'Akshay '+res
def func2():
    return 'Singre'

op=func1(func2)
print(op)