#DATE 15-10-2024
# co q.5 prompt the user for a list of integers.for all values greater than 100 store 'over' instead
uinput=input("enter the list of integers seperated by spaces")
numbers=uinput.split()
result=[]
for x in numbers:
	num=int(x)
	if num>100:
	 result.append('over')
	else:
	 result.append(num)
print("updated list of numbers is ")
print(result)
