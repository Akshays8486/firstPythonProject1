# Recursion_ Factorial
def fact(n):
    if n == 0:
        res = 1
    else:
        res = n * fact(n - 1)
    return res


pqr = fact(4)
print(pqr)
