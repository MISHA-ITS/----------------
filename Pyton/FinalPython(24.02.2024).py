def load_contacts(filename="contacts.txt"):
    contacts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone = line.strip().split(': ')
                contacts[name] = phone
    except FileNotFoundError:
        print("No existing contacts file. Starting with an empty list.")
    return contacts

def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name}: {phone}\n")

def show_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("Contacts:")
        for name, phone in contacts.items():
            print(f"{name}:\t {phone}")

def add_contact(contacts, filename="contacts.txt"):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    save_contacts(contacts, filename)
    print(f"Contact '{name}' successfully added.")
    
def edit_contact(contacts, filename="contacts.txt"):
    name = input("Enter contact name to edit: ")
    if name in contacts:
        new_phone = input("Enter new phone number: ")
        contacts[name] = new_phone
        save_contacts(contacts, filename)
        print(f"Contact '{name}' successfully edited.")
    else:
        print(f"Contact '{name}' not found. Cannot edit a non-existent contact.")


def remove_contact(contacts, filename="contacts.txt"):
    name = input("Enter contact name to remove: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts, filename)
        print(f"Contact '{name}' successfully removed.")
    else:
        print(f"Contact '{name}' not found. Cannot remove a non-existent contact.")

def menu():
    filename = "contacts.txt"
    contacts = load_contacts(filename)

    while True:
        print("\n\tOptions:")
        print("1. Show contacts")
        print("2. Add contact")
        print("3. Edit contact")
        print("4. Remove contact")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            add_contact(contacts, filename)
        elif choice == '3':
            edit_contact(contacts, filename)
        elif choice == '4':
            remove_contact(contacts, filename)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    menu()