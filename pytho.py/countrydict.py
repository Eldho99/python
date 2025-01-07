# Dictionary of 5 countries and their capitals
mydict = [{
    "India":"New Delhi",
    "France": "Paris",
    "Japan":"Tokyo",
    "country":"Brazil","capital": "Brasília",
    "country":"Australia","capital":"Canberra"
}]

countryi=input("enter any country:")
capital(mydict,countryi)

def capital(mydict,countryi):
	if countryi in mydict:
		print("capital is",mydict[countryi])
	else:
		print("note in dictionary")
