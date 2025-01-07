f=open("demofile.txt","r")
c=open("demofile2.txt","w")
ono=1
for line in f:
	if ono%2!=0:
	 c.write(line)
	ono=ono+1
c.close()
c=open("demofile2.txt","r")
print(c.read())
f.close()
c.close()

f=open("demofile.txt","r")
e=open("demofile3.txt","w")
eno=1
for eline in f:
	if eno%2==0:
	 e.write(eline)
	eno=eno+1
e.close()
e=open("demofile3.txt","r")
print(e.read())	
f.close()
e.close() 
	
	
