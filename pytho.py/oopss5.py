#create a class publisher,derive a class from publisher with attributes author and title,derive class python from book with attributes price and no_of_pages,write a program that displays about  
class publisher:
	def __init__(self,namep):
		self.namep=namep
	def display():
		pass
		
class book(publisher):
	def __init__(self,namep,title,author):
		super().__init__(namep)    #invoking the base class publisher
		self.title=title
		self.author=author
	def display():
		pass
		
		
class python(book):
	def __init__(self,namep,title,author,price,pageno):
		super().__init__(namep,title,author)
		self.price=price
		self.pageno=pageno
	def display(self):
		print("\n****book details****")
		print("\ntitle:      ",self.title)
		print("\nname of publication:",self.namep)
		print("\nauthor:     ",self.author)
		print("\nprice:      ",self.price)
		print("\nno of pages:",self.pageno)
		
namep=input("enter the name of publication:")
title=input("enter the title:")
author=input("enter the name of author:")
price=int(input("enter the price of books:"))
pageno=int(input("enter the no of pages:"))

b=python(namep,title,author,price,pageno)
b.display()

#output

#enter the name of publication:dc
#enter the title:batman vs superman
#enter the name of author:chris
#enter the price of books:2000
#enter the no of pages:200

#****book details****

#title:       batman vs superman

#name of publication: dc

#author:      chris

#price:       2000

#no of pages: 200


#enter the name of publication:marvel
#enter the title:Avangers        
#enter the name of author:stan lee
#enter the price of books:2500
#enter the no of pages:150

#****book details****

#title:       Avangers

#name of publication: marvel

#author:      stan lee

#price:       2500

#no of pages: 150




		
