#write a program to read each row from the csv file and print the list of strings
import csv
with open("student.csv",mode="r") as f:
	csvr=csv.reader(f)
	for row in csvr:
		print(row)
	
