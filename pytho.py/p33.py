#date 24-10-2024
#Q.declare a string "welcome to python programming"

s="welcome to python programming"
print(s)
#lenght of string
print("length of the string is:",len(s))
s1="hello"
print(s1)
#concatinate
print(s+"\t"+s1)
print(s[11:18])
#replacing letter
print(s.replace("w","$"))
print(s1[-4:])
# string to uppercase
s="welcome to python programming"
print(s.upper())
#displaying reverse of the string
print(s1[::-1])
#displaying python programming
print(s[11:])
#to check whether string is lower
print(s.islower())
#to split string
print(s.split())

#OUTPUT
#welcome to python programming
#length of the string is: 29
#hello
#welcome to python programming	hello
#python 
#$elcome to python programming
#ello
#WELCOME TO PYTHON PROGRAMMING
#olleh
#python programming
#True
#['welcome', 'to', 'python', 'programming']

