file=open("demofile.txt","r")
l=[i.split() for i in open ("demofile.txt")]
print(l)
f.close()
