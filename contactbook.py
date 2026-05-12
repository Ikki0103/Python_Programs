contacts = {
    "juan": {
        "phone": "09123456789",
        "email": "juan@email.com"
    },
    "jasmine": {
        "phone": "09283567212",
        "email": "jasmine@gmail.com"
    }
}


def main():
    while True:
        print("\n==== Contact Book ====")
        print(
            "\n[1] Show Contacts\n[2]Add Contacts\n[3]Search Contact\n[4]Delete Contact\n[5]Exit")
        choice = input("Enter Choice: ")
        try:
            if choice == "1":
                show_contacts()
            elif choice == "2":
                add_contact()
            elif choice == "3":
                search_contact()
            elif choice == "4":
                delete_contact()
            elif choice == "5":
                print("Goodbye")
                break
            else:
                print("Please input 1-5")
        except ValueError:
            print("Not within the Choices")


def show_contacts():
    for name, details in contacts.items():
        print(f'Name: {name}')
        print(f'Phone: {details["phone"]}')
        print(f'Email: {details["email"]}')
        print("----")


def add_contact():
    name = input("Enter name: ").lower()
    phone = input("Enter phone number: ")
    email = input("Enter email: ").lower()

    contacts[name] = {
        "phone": phone,
        "email": email
    }
    print("Contact added")
    show_contacts()


def search_contact():
    print("Search contacts")
    name = input("Enter name: ").lower()
    search_contacts = contacts.get(name)

    if search_contacts:
        print(f"Contact {name} Found")
        print(f"Name: {name}")
        print(f"phone: {search_contacts["phone"]}")
        print(f"email: {search_contacts["email"]}")
    else:
        print("Contact not found")


def delete_contact():
    print("DELETE contact")
    name = input("Enter name: ").lower()
    if name in contacts:
        del contacts[name]
        print("Contact Deleted")
    else:
        print("Contact not found")
    show_contacts()


# show_contacts()
# search_contact()
# delete_contact()
main()
