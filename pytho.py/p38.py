#from a list of integers create a list removing even numbers

#program
ol=[int(i)for i in input("enter the integers").split()]
nl=[i for i in ol if i%2!=0]
print("list after removing even numbers:",nl)

#output
#enter the integers 4 5 6 7 9 2 10
#list after removing even numbers: [5, 7, 9]

#enter the integers 22 45 12 34 68 
#list after removing even numbers: [45]



