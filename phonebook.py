import re
"""
CSE-5382 Assignment 2
Kent Irvin
1001487672
"""
#with file = open('data.txt', 'r+'):
nameRegex = "^(O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?,?( (O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?)?$"
buffer = input("ADD <Person> <Telephone #> \nDEL <Person> \nDEL <Telephone #> \nLIST \n")
token = buffer.split()
name = ""
phonebook = []

for i in range(0, len(token)):
    if i == 0:
        action = token[i]
    elif i == 1:
        name += token[i]
    elif i < len(token)-1:
        name += " " + token[i]
    else:
        phone = token[i]

if action.upper() == "ADD":
    match = re.match(nameRegex, name)
    if match:
        #phonebook.append([name,phone])
        print("VALID NAME")
    else:
        print("INVALID NAME")
if action == "EXIT":
    exit()
print(phonebook)