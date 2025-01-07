#DATE 26-09-2024
#CO-1 
#11.program to find largest among three numbers

#PROGRAM
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
	print("first number is the greatest")
elif b>a and b>c:
	print("second number is the greatest")
else:
	print("third number is the greatest")
	
#OUTPUT
#ENTER THE FIRST NUMBER: 5
#ENTER THE SECOND NUMBER:4
#ENTER THE THIRD NUMBER:3
#FIRST NUMBER IS THE GREATEST

#ENTER THE FIRST NUMBER:2
#ENTER THE SECOND NUMBER:8
#ENTER THE THIRD NUMBER:3
#SECOND NUMBER IS THE GREATEST

#ENTER THE FIRST NUMBER:3
#ENTER THE SECOND NUMBER:4
#ENTER THE THIRD NUMBER:9
#THIRD NUMBER IS THE GREATEST	
