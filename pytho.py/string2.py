#Get a string made of the first 2 and the last 2 chars from a given a string
s=input("enter the string:")
if len(s)>3:
	first=(s[0:2])
	last=(s[-2:])
	snew=first+last
	print("new string by taking first 2 and last 2 chararacters:",snew)
else:
	print("string is too short")		
		
