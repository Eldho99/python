#write a program to read each row from the csv file and print the list of strings
import csv
with open("student.csv",mod="r") as file:
	csvr=csv.reader(file)
	for row in csvr:
		print(row)
