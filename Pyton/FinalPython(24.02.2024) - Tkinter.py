import tkinter as tk
from tkinter import simpledialog, messagebox

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
    sorted_contacts = dict(sorted(contacts.items(), key=lambda x: x[0]))
    with open(filename, 'w') as file:
        for name, phone in sorted_contacts.items():
            file.write(f"{name}: {phone}\n")

def show_contacts(contacts):
    if not contacts:
        messagebox.showinfo("Contacts", "No contacts available.")
    else:
        contact_list = "\n".join([f"{name}: \t{phone}" for name, phone in contacts.items()])
        messagebox.showinfo("Contacts", f"Contacts:\n{contact_list}")

def add_contact(contacts, filename="contacts.txt"):
    name = simpledialog.askstring("Add Contact", "Enter contact name:")
    
    # Check if the contact already exists
    if name in contacts:
        messagebox.showwarning("Error", f"Contact '{name}' already exists. Cannot add duplicate contact.")
        return
    phone = simpledialog.askstring("Add Contact", "Enter contact phone number:")
    
    # Check if the user clicked Cancel
    if name is None or phone is None:
        return

    contacts[name] = phone
    save_contacts(contacts, filename)
    messagebox.showinfo("Success", f"Contact '{name}' successfully added.")

def edit_contact(contacts, filename="contacts.txt"):
    name = simpledialog.askstring("Edit Contact", "Enter contact name to edit:")
    
    # Check if the user clicked Cancel
    if name is None:
        return
    
    if name in contacts:
        new_phone = simpledialog.askstring("Edit Contact", "Enter new phone number:")
        
        # Check if the user clicked Cancel
        if new_phone is None:
            return

        contacts[name] = new_phone
        save_contacts(contacts, filename)
        messagebox.showinfo("Success", f"Contact '{name}' successfully edited.")
    else:
        messagebox.showwarning("Error", f"Contact '{name}' not found. Cannot edit a non-existent contact.")

def remove_contact(contacts, filename="contacts.txt"):
    name = simpledialog.askstring("Remove Contact", "Enter contact name to remove:")
    
    # Check if the user clicked Cancel
    if name is None:
        return
    
    if name in contacts:
        del contacts[name]
        save_contacts(contacts, filename)
        messagebox.showinfo("Success", f"Contact '{name}' successfully removed.")
    else:
        messagebox.showwarning("Error", f"Contact '{name}' not found. Cannot remove a non-existent contact.")

def menu():
    filename = "contacts.txt"
    contacts = load_contacts(filename)

    while True:
        choice = simpledialog.askstring("Menu", "Options:\n1. Show contacts\n2. Add contact\n3. Edit contact\n4. Remove contact")

        if choice == '1':
            show_contacts(contacts)
        elif choice == '2':
            add_contact(contacts, filename)
        elif choice == '3':
            edit_contact(contacts, filename)
        elif choice == '4':
            remove_contact(contacts, filename)
        elif choice is None: # Check if the user clicked Cancel
            messagebox.showinfo("Exit", "Exiting the program. Goodbye!")
            break
        else:
            messagebox.showwarning("Error", "Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    menu()