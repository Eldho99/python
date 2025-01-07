#create a rectangle class with atrribute length and breadth and methods to find area and perimeter
class rectangle:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
	def perimeter(self):
		return 2*(self.length+self.breadth)
			
length1=int(input("enter the lenght of first rectangle:"))
breadth1=int(input("enter the breadth of first rectangle:"))
length2=int(input("\nenter the length of second rectangle:"))
breadth2=int(input("enter the breadth of second rectangle:"))
	
rectangle1=rectangle(length1,breadth1)
rectangle2=rectangle(length2,breadth2)

print("\narea of rectangle 1:",rectangle1.area())
print("perimeter of rectangle 1:",rectangle1.perimeter())
print("\narea of rectangle 2:",rectangle2.area())
print("perimeter of rectangle 2:",rectangle2.perimeter())

if rectangle1.area()<rectangle2.area():
	print("\narea of rectangle 2 is greatest")
elif rectangle1.area()>rectangle2.area():
	print("\narea of rectangle 1 is the greatest")
else:
	print("\narea of two rectangles are equal")	\

#output
#enter the length of rectangle1:25
#enter the width of rectangle1:20

#enter the length of rectangle2:30
#enter the width of rectangle1:20
#area of rectangle 1 is smaller than area of rectangle 2
 
 
#enter the length of rectangle1:24  
#enter the width of rectangle1:22

#enter the length of rectangle2:12
#enter the width of rectangle1:25
#area of recatangle1 is larger than area of rectangle 2

#enter the length of rectangle1:10
#enter the width of rectangle1:5

#enter the length of rectangle2:10
#enter the width of rectangle1:5
#both rectangles have same area


	
	
