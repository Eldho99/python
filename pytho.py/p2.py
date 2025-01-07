#DATE 26-09-2024
#CO-1
#2.DISPLAY FUTURE LEAP YEAR'S FROM CURRENT YEAR TO FINAL YEAR ENTERED BY THE USER

#PROGRAM
startyear=2016
endyear=int(input("enter a future year:"))
print(f"leap years from{startyear} to {endyear} are:")
for year in range(startyear,endyear+1):
	if year%4==0 and (year%100!=0 or year%400==0):
		print(year)
	
#OUTPUT
#ENTER A FUTURE YEAR: 2040
#leap year from 2016 to 2024 are:
#2016
#2020
#2024
#2028
#2032
#2036
#2040	

#enter a future year:2028
#leap year from 2016 to 2028 are:
#2016
#2020
#2024
#2028
	
	
	  
