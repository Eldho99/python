f = open("demofile.txt", "w")
f.write("appending\neldho\nmca")
f=open("demofile.txt","r")
print(f.read())
f.close()


