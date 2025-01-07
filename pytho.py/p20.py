thislist=["apple","bannana","cherry","kiwi","melon"]
tropical=["mango","pineapple"]
if "kiwi" in thislist:
	print("yes,kiwi in this list")
thislist[2]="blackberry"
thislist.append("orange")
thislist.insert(3,"guvava")
thislist.extend(tropical)
thislist.remove("mango")
print(thislist)
list2=[1,2,3,4]
print(list2)
print(list2[0])
print(thislist[2:4])
print(len(thislist))
print(thislist[:4])
