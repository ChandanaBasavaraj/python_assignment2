#14. Implement function to find the string length without using standard library.
string=raw_input("enter the string")
length = 0
for i in string:
	length = length + 1
print("length of the string is:",length)
