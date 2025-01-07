#date:24-10-2024
#Get a string from an input string where all occurrences of first character replaced with ‘$’, except first character.

#PROGRAM
s=input("enter a string:")
c=s[0]
str1=s[1:]
if c in str1: 
	new=str1.replace(c,"$")
print(c+new)
 
#OUTPUT
#enter a string:hellhoh
#hell$o$

#enter a string:eurecaaa
#eur$caaa

