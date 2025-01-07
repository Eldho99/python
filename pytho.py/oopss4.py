
class time:
	def __init__(self,hour,minute,second):
		self.hour=hour
		self.minute=minute
		self.second=second
	def display_time(self):
		print(f"{self.hour}h:{self.minute}m:{self.second}s")
		
	def __add__(self,other):
		total_second=self.second+other.second
		total_minute=self.minute+other.minute+(total_second//60)
		total_hour=self.hour+other.hour+(total_minute//60)
		
		total_second=total_second%60
		total_minute=total_minute%60
		return time(total_hour,total_minute,total_second)
	
h1=int(input("enter the hour 1:"))
m1=int(input("enter the minute 1:"))
s1=int(input("enter the second 1:"))
h2=int(input("\nenter the hour 2:"))
m2=int(input("enter the minute 2:"))
s2=int(input("enter the second 2:"))

t1=time(h1,m1,s1)
t2=time(h2,m2,s2)
t3=t1+t2

print("\n time1:")
t1.display_time()

print("\n time2:")
t2.display_time()

print("\n time3:")
t3.display_time()

#output

#enter the hour 1:2
#enter the minute 1:34
#enter the second 1:15

#enter the hour 2:1
#enter the minute 2:27
#enter the second 2:36

 #time1:
#2h:34m:15s

 #time2:
#1h:27m:36s

 #time3:
#4h:1m:51s

#enter the hour 1:3   
#enter the minute 1:34
#enter the second 1:15

#enter the hour 2:2
#enter the minute 2:23
#enter the second 2:22

#time1:
#3h:34m:15s

#time2:
#2h:23m:22s

#time3:
#5h:57m:37s

		
		
