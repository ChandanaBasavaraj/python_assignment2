#. Implement a program using CLA for simple arithmetic calculator exmaple: operand operator operand ie. 10 + 10 / 30 * 20
import sys
a=int(sys.argv[1])
b=(sys.argv[2])
c=int(sys.argv[3])

if b =='+':
	sum = a+c
	print(sum)
elif b =='-':
	sub = a-c
	print(sub)
 
elif b =='*':
	mul = a*c
	print(mul)
elif b =='/':
	div = a/c
	print(div)
else:
	print("invalid input")
