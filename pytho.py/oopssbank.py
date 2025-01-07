#create a bank account with
class account:
	def __init__(self,accname,accnumber,acctype,balance):
		self.accname=accname
		self.accnumber=accnumber
		self.acctype=acctype
		self.balance=balance
	
	def deposit(self,amt):
		if amt>0:
			self.balance+=amt
			print("successfully deposited amount:Rs.",amt)
		else:
			print("invalid amount")
	def withdraw(self,amt):
		if amt>self.balance:
			print("insufficient balance")
		else:
			self.balance-=amt
			print("sucessfully withdrawn:Rs.",amt)
	def viewdetails(self):
		print("account number:",self.accnumber)
		print("account name:",self.accname)
		print("account type:",self.acctype)
		print("account balance:Rs.",self.balance)		
				
		
accnumber=int(input("enter account number:"))		
accname=input("enter the name of the user:")		
acctype=input("enter the account type:")
balance=int(input("enter account balance:"))

c1=account(accname,accnumber,acctype,balance)
while True:
	print("****MENU*****\n 1.deposit \n 2.withdraw\n 3.current balance\n 4.view details\n 5.Exit")
	ch=int(input("enter your choice:"))
	if ch==1:
		amt=int(input("enter the amount to be deposited:Rs."))
		c1.deposit(amt)
	elif ch==2:
		amt=int(input("enter the amount to be withdrawn:Rs."))
		c1.withdraw(amt)
	elif ch==3:
		print("current balance: Rs.",c1.balance)
	elif ch==4:
		c1.viewdetails()
	elif ch==5:
		break
		
#output

#enter account number:445200678
#enter the name of the user:eldho mathew
#enter the account type: savings
#enter account balance:20150         
#****MENU*****
 #1.deposit 
 #2.withdraw
 #3.current balance
 #4.view details
 #5.Exit
#enter your choice:1
#enter the amount to be deposited:Rs.200
#successfully deposited amount:Rs. 200
#****MENU*****
 #1.deposit 
 #2.withdraw
 #3.current balance
 #4.view details
 #5.Exit
#enter your choice:3
#current balance: Rs. 20350
#****MENU*****
 #1.deposit 
 #2.withdraw
 #3.current balance
 #4.view details
 #5.Exit
#enter your choice:2
#enter the amount to be withdrawn:Rs.500
#sucessfully withdrawn:Rs. 500
#****MENU*****
 #1.deposit 
 #2.withdraw
 #3.current balance
 #4.view details
 #5.Exit
#enter your choice:3
#current balance: Rs. 19850
#****MENU*****
 #1.deposit 
 #2.withdraw
 #3.current balance
 #4.view details
 #5.Exit
#enter your choice:4
#account number: 445200678
#account name: eldho mathew
#account type:  savings
#account balance:Rs. 19850
#****MENU*****
 #1.deposit 
 #2.withdraw
 #3.current balance
 #4.view details
 #5.Exit
#enter your choice:5
		
		
		


