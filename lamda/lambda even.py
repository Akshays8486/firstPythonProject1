# Write a lambda to test if a given no is even or not

n = int(input('Enter no. : '))
def even_odd(n):
    if n%2==0:
        return'Even'
    else:
        return'Odd'
str =even_odd(n)
print("This is normal function",str)

f = lambda n:'Even' if n%2==0 else'Odd'
print('This is lambda function',f(n))

#f = lambda n: 'Even' if n%2 ==0 else 'odd'
