import re
"""
CSE-5382 Assignment 2
Kent Irvin
1001487672
"""
#with file = open('data.txt', 'r+'):
nameRegex = "^(O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?,?( (O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?)?( (O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?)?$"
phoneRegex = "[0-9]{5}.?([0-9]{5})?|(\+?[0-9]{1,3}[ \.\-]?)?\([0-9]{2,3}\)|[0-9]{3}[ \.\-][0-9]{4}|([0-9]{1,4}[ \.\-]){3,4}[0-9]{1,4}"
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

print("'"+action+"'")
print("'"+name+"'")
print("'"+phone+"'")   

if action.upper() == "ADD":
    match = re.match(nameRegex, name)
    if match:
        print("VALID NAME")
        match2 = re.match(phoneRegex, phone)
        if match2:
            #phonebook.append([name,phone])
            print("VALID PHONE NUMBER")
        else:
            print("INVALID PHONE NUMBER")
    else:
        print("INVALID NAME")

if action == "EXIT":
    exit()
#print(phonebook)