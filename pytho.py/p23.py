l=input("enter the list of integers seperated by spaces")
l1=[int(num) for num in l.split()]
print(l1)
sqr=[i*i for i in l1 if i>0]
print(sqr)
