#Implement a program to read alternative characters in the file
f=open("text.txt","r")
f1=f.read()
print(f1)
for i in f1:
	for j in i:
		print(j)
