#implement a program to create a list containing two tuples of fruit and vegetables.access them separately
fruits=('banana','apple')
vegetables=('potato','carrot')
mylist=list(zip(fruits,vegetables))
print(mylist)

for fruits in mylist:
       print(fruits[0])

for vegetables in mylist:
       print(vegetables[1])

