s=input("enter a string:")
freq={}
for c in s:
	if c in freq:
		freq[c]=freq[c]+1
	else:
		freq[c]=1
print(freq)	
	
