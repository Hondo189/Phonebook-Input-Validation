import re
import sys
"""
CSE-5382 Assignment 2
Kent Irvin
1001487672
"""

name = ""
phonebook = []

#import phonebook entries from phonebook.txt
with open('phonebook.txt', 'r+') as file:
    for line in file:
        #print("Line: "+ line)
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

#print(phonebook)                
nameRegex = "^(O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?,?( (O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?)?( (O’)?([A-Za-z]{1,31})(-[A-Za-z]{1,31})?)?$"
phoneRegex = "[0-9]{5}.?([0-9]{5})?|(\+?[0-9]{1,3}[ \.\-]?)?\([0-9]{2,3}\)|[0-9]{3}[ \.\-][0-9]{4}|([0-9]{1,4}[ \.\-])[0-9]{1,4}"
buffer = input("ADD <Person> <Telephone #> \nDEL <Person> \nDEL <Telephone #> \nLIST \nEXIT")
token = buffer.split()
action = token[0]

if action.upper() == "ADD": #add new phonebook entry
    for i in range(1, len(token)):
        if i == 1:
            name += token[i]
        elif i < len(token)-1:
            name += " " + token[i]
        else:
            phone = token[i]    
    
    match = re.match(nameRegex, name)
    if match:
        #print("VALID NAME")
        match2 = re.match(phoneRegex, phone)
        if match2:
            #print("VALID PHONE NUMBER")
            phonebook.append([name,phone])
        else:
            #print("INVALID PHONE NUMBER")
            print("ERROR: Invalid Phone Number", file-sys.stderr)
            exit(1)
    else:
        #print("INVALID NAME")
        print("Error: Invalid Name", file-sys.stderr)
        exit(1)
elif action.upper() == "DEL": #delete phonebook entry based on name or phonenumber
    found = False
    for i in range(1, len(token)):
        if i == 1:
            temp = token[i]
        elif i < len(token):
            temp += " " + token[i]        
            
    matchN = re.match(nameRegex, temp)
    matchP = re.match(phoneRegex, temp)
    if matchP:
        phonebook = [v for v in phonebook if v[1] != temp]
        for i in range(0, len(phonebook)):
                if phonebook[i][0] == temp:
                    found = True
    elif matchN:
        phonebook = [v for v in phonebook if v[0].lower() != temp.lower()]
        for i in range(0, len(phonebook)):
                if phonebook[i][1] == temp:
                    found = True
    else:
        print("Error: Argument is not a valid name or phone number", file-sys.stderr)
        exit(1)
    if found == False: #if name/phone# unfound
        print("Name/Phone Number not found")
        exit(1)
elif action.upper() == "LIST": #print phonebook
    for row in phonebook:
        for elem in row:
            print(elem, end=' ')
        print()
elif action == "EXIT":
    exit()
#print(phonebook)

#store phonebook entries into phonebook.txt
with open('phonebook.txt', 'w+') as file:
    for row in phonebook:
        for elem in row:
            file.write(elem + ' ')
        file.write('\n')