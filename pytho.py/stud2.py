#program to create a csv dictionary and read it
import csv
mydict=[{'jerseyno':'10','name':'messi','age':'37','position':'RWF'},
        {'jerseyno':'11','name':'neymar','age':'32','position':'LWF'},
        {'jerseyno':'9','name':'suarez','age':'36','position':'ST'},
        {'jerseyno':'7','name':'ronaldo','age':'39','position':'ST'}]
fields=['jerseyno','name','age','position']
filename="studentdict.csv"
with open(filename, 'w') as csvfile:
	writer = csv.DictWriter(csvfile, fieldnames=fields)        
	writer.writeheader()
	writer.writerows(mydict)
with open("studentdict.csv",'r') as f:
	csvr=csv.reader(f)
	for row in csvr:
		print(row)
		
#output
#['jerseyno', 'name', 'age', 'position']
#['10', 'messi', '37', 'RWF']
#['11', 'neymar', '32', 'LWF']
#['9', 'suarez', '36', 'ST']
#['7', 'ronaldo', '39', 'ST']
		
	
