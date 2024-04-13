# Write a lambda function two find sum of two nos
def sum(a,b):
    c= a+b
    return c
res = sum(10,11)
print(res)
# or with lambda 2 lines compact code
print("With Lambda Function")

x= lambda a,b:a+b
print("Sum = ",x(10,11))
