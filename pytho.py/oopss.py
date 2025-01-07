#create a class student with attributes number name and age ,create an object student1 of the student class. print the roll no ,name and age
class student:
	def __init__(self,rollno,name,age):
		self.rollno=rollno
		self.name=name
		self.age=age
rollno=int(input("Enter the rollno:"))
name=input("Enter the name:")
age=int(input("Enter the age:"))					
student1=student(rollno,name,age)
print("Roll no:",student1.rollno)	
print("Name:",student1.name)
print("Age:",student1.age)

#output
#Enter the rollno:10
#Enter the name:leo
#Enter the age:22

#Roll no: 10
#Name: leo
#Age: 22

	

