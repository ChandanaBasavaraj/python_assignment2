import sys
f=open("example.txt\n","a+")
a=sys.argv[1]
b=sys.argv[2]
f.write(a)
f.write(b)
print(a,b)