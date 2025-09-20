contact_book={
    "John Doe":{
        "phone":"8967542310",
        "email":"johndoe@gmail.com"
    },
    "Jane Smith":{
        "phone":"8976543210",
        "email":"jane@gmail.com"
    },
    "Alice Johnson":{
        "phone":"8987654321",
        "email":"alice@gmail.com"
    }
}
def get_contact(name):
    for contact_name in contact_book:
        if contact_name==name:
            return contact_book[contact_name]
    return "Contact not found"
def get_all_contacts():
    return contact_book
def add_contact(name,phone,email):
    if name not in contact_book:
        contact_book[name]={"phone":phone,"email":email}
        return "contact  added successfully"
    else:
        return "Contact already exists"
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        return "Contact Deleted successfully"
    else:
        return "Contact not found"
# 
def update_contact(name,phone=None,email=None):
    if name in contact_book:
        if phone:
            contact_book[name]['phone']=phone
        if email:
            contact_book[name]['email']=email
        return "Contact updated successfully"
    else:
        return "Contact not found"
def main(): 
    while True:
        print("1. Get Contact")
        print("2. Get All Contacts")
        print("3. Add Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            name=input("Enter contact name:")
            print(get_contact(name))
        elif choice==2:
            print(get_all_contacts())
        elif choice==3:
            name=input("Enter contact name:")
            phone=input("Enter phone number:")
            email=input("Enter email address:")
            print(add_contact(name,phone,email))
        elif choice==4:
            name=input("Enter contact name:")
            print(delete_contact(name))
        elif choice==5:
            name=input("Enter contact name:")
            phone=input("Enter new phone number (leave blank to skip):")
            email=input("Enter new email address (leave blank to skip):")
            phone=phone if phone else None
            email=email if email else None
            print(update_contact(name,phone,email))
        elif choice==6:
            break
        else:
            print("Invalid choice. Please try again.")
if __name__=="__main__":
    main()

