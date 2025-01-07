thisdict={"name":"rishi", "age":23, "dep":"mca"}
print(thisdict)
print(thisdict["age"])
print(len(thisdict))
x=thisdict.keys()
print(x)
thisdict2=dict(name="jhon",age=23,dep="mba")
print(thisdict2)
thisdict.update({"dep":"btech"})
print(thisdict)
thisdict["addmission year"]=2022
print(thisdict)
thisdict.pop("addmission year")
print(thisdict)
for x in thisdict:
	print(thisdict[x])
