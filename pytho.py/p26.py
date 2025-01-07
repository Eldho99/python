#DATE 15-10-2024
# co q.5 prompt the user for a list of integers.for all values greater than 100 store 'over' instead use list comprehension
uinput=[i for i in input("enter the list of integers seperated by spaces").split()]
result=[int(i) for i in uinput if i>100 ]
result=int(i)
result.append('over') 
print(result)
