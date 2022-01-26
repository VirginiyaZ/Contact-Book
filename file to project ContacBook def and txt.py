file_name = "Phonebook.txt"
filerec = open(file_name, "a+")
filerec.close


def show_main_menu():
    ## General menu 
    print("\n   Phone Book Menu \n"+
          "author: Zubar Virginiya \n"+
          "=================================\n"+
          "Enter 1,2,3,4,5 or 6:\n"+
          "Enter 1 To Display Contacts Records\n" +
          "Enter 2 To Add a New Contact Record\n"+
          "Enter 3 To Search Contacts\n"+
          "Enter 4 To Delete Contacts\n"+
          "Enter 5 To Edit Contacts information\n"+
          "Enter 6 To Quit\n=========================")
    choice = input("Enter your choice: ")
    if choice == "1":
        filerec = open(file_name, "r+")
        file_contents = filerec.read()
        if len(file_contents) == 0:
            print("Phone Book is Empty")
        else:
            print (file_contents)
        filerec.close
        entry = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "2":
        enter_contact_record()
        entry = input("Press Enter to continue ...")
        show_main_menu()
    elif choice == "3":
        search_contact_record()
        entry = input("Press Enter to continue ...")
        show_main_menu()
    elif choice=='4':
        del_contact_name()
        entry=input("Press Enter to continue ...")
        show_main_menu()
    elif choice== '5':
        edit_contact()
        entry=input("Press Enter to continue ...")
        show_main_menu()
    elif choice== "6":
        print("Thanks for using Phone Book Programm ")
    else:
        print("Wrong choice, Please Enter [1 to 6]\n")
        entry = input("Press Enter to continue ...")
        show_main_menu()
        
def search_contact_record():
    ##' This function is used to searches a specific contact record 
    search_name = input("Enter First name for Searching contact record: ")

    search_name = search_name.title()
    filerec = open(file_name, "r+")
    file_contents = filerec.readlines()
     
    found = False   
    for line in file_contents:
        if search_name in line:
            print("Your Searched Contact Record is:", end=" ")
            print (line)
            found=True
            break
    if  found == False:
        print("There's no contact Record in Phone Book with name = " + search_name )

def enter_contact_record():
    ##  It  collects contact info firstname, last name, notes and phone
   
    first = input('Enter First Name: ')
    first = first.title()
    last = input('Enter Last Name: ')
    last = last.title()
    phone = input('Enter Phone number: ')
    notes = input('Enter notes: ')
    contact = ( first + " " + last + ", " + phone + ", " + notes +  "\n")
    filerec = open(file_name, "a")
    filerec.write(contact)
    print( "This contact\n " + contact + "has been added successfully!")


def del_contact_name():
    ## It should delete the required line as per name in txt file
    filerec = open(file_name)
    result=[]
    name_to_delete=input('Enter record to delete:   ')
    name_to_delete=name_to_delete.title()
    for line in filerec:
        if not line.startswith(name_to_delete):
            result.append(line)
    filerec.close()
    filerec=open(file_name, 'w')
    filerec.writelines(result)
    filerec.close()

    print("Your Required Contact Record is deleted:", end=" ")


def edit_contact():
        filerec = open(file_name, "r")
        read = filerec.read()
        filerec.close
        print (read, "\n")

        name_to_del = input("Copy the Contact name or information you wish to edit\n:")
        new_info=input('Enter new information \n:  ')
        
        filerec = open(file_name, "w")
        var = read.replace((name_to_del), (new_info))
        filerec.write(var)
        filerec.close

        print("Your Required Contact Record is edited:", end=" ")
         
 
show_main_menu()