#9.  Implement a program to create a dictionary of students with Registration number and names. Perform the two operations, insert and delete.
dict={'chandana':181040014,'jaijith':181040011,'deepa':181040002}
print(dict)

#to insert
dict.update(keerthi=1810140005)
print(dict)

#to delete
del dict["keerthi"]
print(dict)

del dict
print(dict)
