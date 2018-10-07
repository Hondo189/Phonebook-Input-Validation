import re
"""
CSE-5382 Assignment 2
Kent Irvin
1001487672
"""

name = ""
phonebook = []

with open('phonebook.txt', 'r+') as file:
    for line in file:
        print("Line: "+ line)
        token2 = line.split()
        #print(token2)
        for i in range(0, len(token2)):
            if i == 0:
                name = token2[i]
                #print("0: "+name)
            elif i < len(token2)-1:
                name += " " + token2[i]
                #print(str(i)+": "+name)
            else:
                phone = token2[i]
                #print(phone)
        phonebook.append([name,phone])
        name = ""
print(phonebook)                
"""
nameRegex = "^(O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?,?( (O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?)?( (O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?)?$"
phoneRegex = "[0-9]{5}.?([0-9]{5})?|(\+?[0-9]{1,3}[ \.\-]?)?\([0-9]{2,3}\)|[0-9]{3}[ \.\-][0-9]{4}|([0-9]{1,4}[ \.\-]){3,4}[0-9]{1,4}"
buffer = input("ADD <Person> <Telephone #> \nDEL <Person> \nDEL <Telephone #> \nLIST \nEXIT")
token = buffer.split()

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
            phonebook.append([name,phone])
        else:
            print("INVALID PHONE NUMBER")
    else:
        print("INVALID NAME")

if action.upper() == "LIST":
    for row in phonebook:
        for elem in row:
            print(elem, end=' ')
        print()
if action == "EXIT":
    exit()
print(phonebook)
"""