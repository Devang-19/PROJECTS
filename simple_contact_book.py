contacts = {}
# full_name = fname + " " + lname

def add_contact():
    
    fname = input("Enter First Name : ").strip().title()
    lname = input("Enter Last Name : ").strip().title()
    full_name = fname + " " + lname

    if full_name in contacts:
        
        print("Contact Already Exists ! Please Use Update")
        return

    phone = int(input("Enter Mobile Number : "))
    email = input("Enter Email : ").strip().title()

    contacts[full_name] = {"Phone" : phone , "Email" : email}
    
    print("Contact Details Added Successfully !\n")


def update_contact():
    
    fname = input("Enter First Name for Update : ").strip().title()
    lname = input("Enter Last Name for Update : ").strip().title()
    full_name = fname + " " + lname

    if full_name in contacts:
        print("==== Updated Contact ====")
        print('Current Phone : ',contacts[full_name]['Phone'])


def delete_contact():
    pass


def search_contact():
    pass


def show_all():
    pass


text = " WELCOME TO CONTACT BOOK " 
print(text.center(130,'='))
print("\n1. ADD NEW CONTACT INFO \n2. UPDATE CONTACT INFO \n3. DELETE CONTATC \n4. SHOW ALL CONTACTS\n")
choice = int(input("Enter a Choice of Above : "))

match choice:

    case 1: add_contact()


    case 2: update_contact()


    case 3: delete_contact()


    case 4: search_contact()


    case 4: show_all()


    case _: print("Enter a Valid Choice !!!")