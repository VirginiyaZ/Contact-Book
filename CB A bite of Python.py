import pickle  ## import modules 
import os


## create Class Person with general atributes of Contact
class Person(object):

    def __init__(self, name=None, phone=None, address=None, notes=None):
        self.name = name
        self.phone = phone
        self.address = address
        self.notes = notes
        
## Dunder method implement print() function
    def __str__(self): 
        return '{} {:>17} {:>17} {:>17}'.format(self.name, self.phone, self.address, self.notes)

## create Class Contac Book Application with file and functionality
class AppCB(object):

    def __init__(self, data):
        self.data = data
        self.persons = {}
        if not os.path.exists(self.data):
            file_reccord = open(self.data, 'wb')
            pickle.dump({}, file_reccord)
            file_reccord.close()
        else:
            with open(self.data, 'rb') as person_list:
                self.persons = pickle.load(person_list)

    def add(self):
        name, phone, address, notes = self.getdetails()
        if name not in self.persons:
            self.persons[name] = Person(name, phone, address, notes)
        else:
            print('Contact already present.')

    def viewall(self):
        if self.persons:
            print('{} {:>17} {:>17} {:>17}'.format('Name', 'Phone', 'Address', 'Notes'))
            for person in self.persons.values():
                print(person)
        else:
            print('There is No contacts in Contact Book.')

    def search(self):
        name = input('Enter Contact Name: ')
        if name in self.persons:
            print(self.persons[name])
        else:
            print('Contact not found.')

    def getdetails(self):
        name = input('Name: ')
        phone = input('Phone:')
        address = input('Address: ')
        notes=input('Notes:  ')
        return name, phone, address, notes

    def update(self):
        name = input('Enter Contact Name: ')
        if name in self.persons:
            print('Enter new details to update:  ')
            name, phone, address, notes = self.getdetails()
            self.persons[name].__init__(name, phone, address, notes)
            print('Successfully updated.')
        else:
            print('Contact is not found.')

    def delete(self):
        try:
            name = input('Enter Contact Name to Delete: ')
            if name in self.persons:
                del self.persons[name]
                print('Contact is Delete.')
            else:
                print('Contact is not found.')
        except TypeError or ValueError  as ex:
            print('An Error accured as {ex}\n Try to Enter a Name but blablabla )))')        
        

    def reset(self):
        self.persons = {}

    def __del__(self): ## Magic/Dunder method to delete 
        with open(self.data, 'wb') as db:
            pickle.dump(self.persons, db)

    def __str__(self): ## Magic/Dunder method (imitate print() function)
        return Menu
Menu = ''' 
        **** Contact Book Menu ****
        Enter 1 to Add new contact
        Enter 2 to View contacts
        Enter 3 to Search contact
        Enter 4 to Update contact
        Enter 5 to Delete contact
        Enter 6 to Reset all 
        Enter 7 to Exit from app Contact Book
                       '''

## initialize main menu of programm
def main():
    app = AppCB('contactbook.data')
    choice = ''
    while choice != '7':
        print(app)
        choice = input('Enter your choice: ')
        if choice == '1':
            app.add()
        elif choice == '2':
            app.viewall()
        elif choice == '3':
            app.search()
        elif choice == '4':
            app.update()
        elif choice == '5':
            app.delete()
        elif choice == '6':
            app.reset()
        elif choice == '7':
            print('See you next time.')
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()