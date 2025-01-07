l=input("enter the list of integers seperated by spaces")
l1=[int(num) for num in l.split()]
pl=[num for num in l1 if num>0]
p2=[num for num in l1 if num<0]
print("the list of positive numbers are",pl)
print("the list of negative nubers are",p2)
