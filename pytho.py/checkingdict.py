#write a python program to check whether a given key already exists in the dictionary.
def checkkey(dictionary, key):
    if key in dictionary:
        print(f"Key '{key}' exists in the dictionary.")
    else:
        print(f"Key '{key}' does not exist in the dictionary.")

mydict = {
    "name": "ravi",
    "age": 22,
    "city": "ernakulam"
}


check = input("enter the key to check:")
checkkey(mydict,check)

