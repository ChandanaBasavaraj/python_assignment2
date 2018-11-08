#Implement a menu based  program for Arithemetic Calculator
num1= int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
choice=int(input("enter your choice...1/2/3/4"))
if choice==1:
	sum=num1 + num2
	print(sum)
elif choice == 2:
	sub = num1 - num2
	print(sub)
elif choice == 3:
	mul = num1 * num2
	print(mul)
elif choice == 4:
	div = num1/num2
	print(div)
else:
	print("invalid input")

