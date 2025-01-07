#co2.11 write lamda functions to find area of a square, rectangle and traiangle

#PROGRAM
 area1=lambda a:a*a
 area2=lambda l,b: l*b
 area3=lambda b1,h1: 0.5*b*h
 S=int(input("enter the side of the square"))
 print("area of the square is:",area1(S))
 l=int(input("enter the lenght of the rectangle"))
 b=int(input("enter the breadth of the rectangle"))
 print("area of the rectangle",area2(l,b))
 b1=int(input("enter the base of the traingle"))
 h1=int(input("enyter the height of the traingle"))
 print("area of the traingle is",area3(b1,h1))
 
#OUTPUT
 
