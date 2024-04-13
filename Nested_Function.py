def display():
    def inner():
        return 'Singre'
    return 'Akshay '+inner()
str = display()
print(str)