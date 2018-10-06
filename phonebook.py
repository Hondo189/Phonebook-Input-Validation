import re
"""
CSE-5382 Assignment 2
Kent Irvin
1001487672
"""
#with file = open('data.txt', 'r+'):
buffer = input("ADD <Person> <Telephone #> \nDEL <Person> \nDEL <Telephone #> \nLIST \n")
token = buffer.split()
name = ""

for i in range(0, len(token)):
    if i == 0:
        action = token[i]
    elif i == 1:
        name += token[i]
    elif i < len(token)-1:
        name += " " + token[i]
    else:
        phone = token[i]
print(action+".")
print(name+".")
print(phone+".")