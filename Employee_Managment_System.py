d1 = {}

def add_emp():
    id = int(input("Enter Employee ID : "))
    
    if id in d1:
        print("Employee ID Already Exists! Please use Update Option.")
        return

    name = input("Enter Employee Name : ").strip().title()
    salary = int(input("Enter Employee's Salary : "))
    d1[id] = [name,salary]
    print("Employee Added Successfully...")

def update_emp():
    id = int(input("Enter Employee ID : "))
    if id in d1:
        name = input("Enter Employee Name : ").strip().title()
        salary = int(input("Enter Employee's Salary : "))
        d1[id] = [name,salary]
        print("Employee's Details Updated Successfully...")
    else:
        print("Employee Not Found !!!")
    
def delete_emp():
    id = int(input("Enter Employee ID for Delete : "))
    if id in d1: 
        del d1[id]
        print("Employee Deleted Successfully...")
    else:
        print("Employee Not Found !!!")

def search_emp():

    s_id = int(input("Enter Employee's ID For Search : "))

    if s_id in d1:
        name,salary = d1[s_id]
        print("ID : ", s_id,"Name : ",name," | Salary : ",salary)
    else:
        print("Employee Not Found !!!")

def display_all():

    if d1:
        text = "<===============    ALL EMPLOYEES    ===============>"
        centered_text = text.center(120)
        print(centered_text)

        for id,details in d1.items():
            name,salary = details
            print("ID : ",id,"NAME : ",name," | SALARY : ",salary)
    
    else:
        print("No Employee Found !!!")

while True :
    print("1 - Add Employee")
    print("2 - Update Employee")
    print("3 - Delete Employee")
    print("4 - Search Employee")
    print("5 - Display Employee")
    print("6 - Exit")
    
    choice = int(input("Enter Your Choice : "))
    if choice == 1 :
        add_emp()
    elif choice == 2 :
        update_emp()
    elif choice == 3 :
        delete_emp()
    elif choice == 4 :
        search_emp()
    elif choice == 5 :
        display_all()
    else :
        break