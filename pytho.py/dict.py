#write a program to read specific coloumns from a csv file
import csv
with open("student.csv",mode="r")as f:
	csvr=csv.reader(f)
	print("CSV FILE")
	for row in csvr:
		print("\n",row)
f.close()
f=open("student.csv","r")
col=csv.reader(f)
print("\nprint the colomns only\n")
for i in col:
	print(i[1]+" "+i[3])
f.close()	
	
     

