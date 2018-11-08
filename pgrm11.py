 #Implement a program with functions, for finding the area of circle, triangle, square.

import sys
pi=3.142
def circle():
	r=float(input("enter the value of radius:"))
	return pi*(r*r)
def triangle():
	h=float(input("enter the value of lenght:"))
	b=float(input("enter the value of breadth:"))
	return 0.5*(b*h)
def square():
	s=float(input("enter the value of lenght:"))
	return s*s
while (True):
	print("1:Circle")
	print("2:Triangle")
	print("3:Square")
	print("q:Exit")
	choice=input("enter your choice")
	if choice=='1':
		print(circle())
	elif choice == '2':
		print(triangle())
	elif choice=='3':
		print(square())
	elif choise=='q':
		sys.exit()
	

