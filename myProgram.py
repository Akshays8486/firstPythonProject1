lst =[i for i in input ('Enter Strings:').split(',')]
print(lst)
lst1=[]
for i in lst:
  lst1.append(i.strip())
lst1.sort()
print(lst1)