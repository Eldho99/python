s=input("enter a string:")
c=s[0]
str1=s[1:]
if c in str1: 
	new=str1.replace(c,"$")
print(c+new)
	
