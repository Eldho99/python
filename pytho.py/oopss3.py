#create a class rectangle with private attributes length and width.overload '<' operator to compare the area of 2
class Rectangle:
	def __init__(self,length,width):
		self.length=length
		self.width=width
	def area(self):
		return self.length*self.width
	def __lt__(self,other): #operator overloading
		return self.area() < other.area()
l1=int(input("enter the length of rectangle1:"))
w1=int(input("enter the width of rectangle1:"))
l2=int(input("\nenter the length of rectangle2:"))
w2=int(input("enter the width of rectangle1:"))
		
		
		
rectangle1=Rectangle(l1,w1) #creating object
rectangle2=Rectangle(l2,w2)
if rectangle1<rectangle2: #function call
	print("area of rectangle 1 is smaller than area of rectangle 2")
elif rectangle1>rectangle2:
	print("area of recatangle1 is larger than area of rectangle 2")
else:
	print("both rectangles have same area")	

#output
#enter the length of rectangle1:10
#enter the width of rectangle1:20

#enter the length of rectangle2:12
#enter the width of rectangle1:15
#area of recatangle1 is larger than area of rectangle 2
	
#enter the length of rectangle1:5
#enter the width of rectangle1:4

#enter the length of rectangle2:3
#enter the width of rectangle1:6
#area of recatangle1 is larger than area of rectangle 2
		
#enter the length of rectangle1:10
#enter the width of rectangle1:10

#enter the length of rectangle2:10
#enter the width of rectangle1:10
#both rectangles have same area
		
