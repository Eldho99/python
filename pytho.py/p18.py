#DATE 08-10-2024
#CO-2 
#WRITE A PROGRAM TO DISPLAY THE FIRST N NUMBERS OF THE FIBONACCI SERIES

#PROGRAM
limit=int(input("enter the limit"))
f=0
s=1
print(f,s)
for i in range (2,limit):
	ans=f+s
	f=s
	s=ans
	print(ans)
	
#output	
#enter the limit:7
#ans 0 1 1 2 3 5 8

#enter the limit:8
#0 1 1 2 3 5 8 13

