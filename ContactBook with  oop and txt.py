import os


class Contact:
    ## constructor of the class Contact
    def __init__(self, name, phone, address, notes):
        self.name= name
        self.phone = phone
        self.address = address
        self.notes = notes

## getter method to get value from class
    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def getAddress(self):
        return self.address

    def getNotes(self):
        return self.notes


## setter method to  set value to the class variables
    def setName(self,name):
        self.name = name

    def setPhone(self,phone):
        self.phone = phone

    def setAddress(self, address):
        self.address = address

    def setNotes(self, notes):
        self.notes = notes

## creating functions:
## function to add Contact to file

def addContact(contact):
    file = open('ContactBook.txt', 'a+')
    file.write(contact.getName() + '\t' + contact.getPhone() + '\t' + contact.getAddress() + '\t' + contact.getNotes())
    print('Records has been added succsessfully!')
    file.close

## function to search the requested record as per name    
def searchContact(search_contact):
    getLines = []
    results = []
    file = open('ContactBook.txt', 'r')
    for line in file:
        getLines.append(line)
    for line in getLines:
        if search_contact in line:
            results.append(line)
    if not results:
        print('Record is not found!')
    else:
        print(*results)
        print('Record found!')
    file.close()   


## view all records 
def displayContact():
    getLines=[]
    results=[]
    print('\nname  \tphone   \taddress\tnotes') 
    file = open('ContactBook.txt', 'r')
    for line in file:
        getLines.append(line)
    for line in getLines:
        results.append(line)
    print(*results)
    file.close()


## delete the requested record as per name
def delContact():
    results = []
    file= open('ContactBook.txt', 'r+')
    name_to_delete = input('Enter record Name to delete  ')
    for line in file:
        if not line.startswith(name_to_delete):
            results.append(line)
    file.close()
    file = open('ContactBook.txt', 'w')
    file.writelines(results)
    file.close()

    print('Record deleted succsessfully!')


## edit requested record as per cpy command of the desired information that need to be edited
def editContact():
    file = open('ContactBook.txt', 'r')
    read=file.read()
    file.close()
    print(read, '\n')

    name_to_replace = input('Copy the Contact name or information need to be edited  ')
    new_name_info = input('Enter new record/information   ')

    file=open('ContactBook.txt', 'w')
    replacement=read.replace((name_to_replace),(new_name_info))
    file.write(replacement)
    file.close()

    print('Requested record has been edited succsessfully!')


def resetFile():
    file_name=input('Please, be informed that the file reset will destruct all records and file as well. \nEnter your text file name to reset    ')
    os.remove(file_name)

## making loop with Menu and choice of functionality
while True:

    print( ''' *****Contact Book Menu**** 
         Enter 1 to Add Contact 
         Enter 2 to Search Contact  
         Enter 3 to Display Contact Book information
         Enter 4 to Delete Contact
         Enetr 5 to Edit Contact
         Enter 6 to Reset text file
         Enter 7 to Quit    ''')

    choice = eval(input('Enter your choice  '))
    if (choice == 1):
        name = input('Enter a Name  ')
        phone = input('Enter a Phone number ')
        address = input('Enter an Address  ')
        notes = input ('Enter Notes  ')
        contact = Contact(name, phone, address, notes)
        addContact(contact)
    
    elif (choice == 2):
        search_contact = input('Enter a Name to search  ')
        searchContact(search_contact)

    elif (choice ==3):
        displayContact()

    elif (choice == 4):
        delContact()

    elif (choice ==5):
        editContact()

    elif (choice == 6):
        resetFile()

    elif (choice==7):
        break  

    else:
        print('Enter a correct number of choice! Try again... ')
        continue

