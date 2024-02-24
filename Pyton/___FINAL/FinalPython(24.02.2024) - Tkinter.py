import tkinter as tk
from tkinter import simpledialog, messagebox

def load_contacts(filename="contacts.txt"):
    contacts = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone = line.strip().split(':')
                contacts[name] = phone
    except FileNotFoundError:
        print("No existing contacts file. Starting with an empty list.")
    return contacts

def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name}:{phone}\n")

def find_contact(contacts):
    search_term = simpledialog.askstring("Find Contact", "Enter name or phone to search:")
    if search_term is not None and search_term != "":
        search_term = search_term.lower()
        found_contacts = []

        for name, phone in contacts.items():
            if search_term in name.lower() or search_term in phone.lower():
                found_contacts.append(f"{name}: {phone}")

        if found_contacts:
            result = "\n".join(found_contacts)
            messagebox.showinfo("Contact Found", f"Found contact:\n{result}")
        else:
            messagebox.showinfo("Contact Not Found", f"No contacts found for '{search_term}'.")

def add_contact(contacts):
    name = simpledialog.askstring("Add Contact", "Enter contact name:")
    if name is None or name == "":
        messagebox.showwarning("Error", "Contact name cannot be empty. \nReturning to the main menu.")
        return

    name_lower = name.lower()
    if name.lower() in contacts:
        messagebox.showinfo("Contact Exists", "Contact already exists.")
        return

    phone = simpledialog.askstring("Add Contact", "Enter phone number:")
    if phone is None or phone == "":
        messagebox.showwarning("Error", "Phone number cannot be empty. \nReturning to the main menu.")
        return

    contacts[name] = phone
    save_contacts(contacts)
    messagebox.showinfo("Contact Added", "Contact added successfully.")

def delete_contact(contacts):
    name = simpledialog.askstring("Delete Contact", "Enter contact name:")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        messagebox.showinfo("Contact Deleted", "Contact deleted successfully.")
    else:
        messagebox.showinfo("Contact Not Found", "Contact not found.")

def edit_contact(contacts):
    name = simpledialog.askstring("Edit Contact", "Enter contact name to edit:")
    if name in contacts:
        new_phone = simpledialog.askstring("Edit Contact", "Enter new phone number:")
        if new_phone is not None and new_phone != "":
            contacts[name] = new_phone
            save_contacts(contacts)
            messagebox.showinfo("Success", f"Contact '{name}' successfully edited.")
    else:
        messagebox.showwarning("Error", f"Contact '{name}' not found. Cannot edit a non-existent contact.")

contacts = load_contacts()
root = tk.Tk()
root.title("Phone Book")
root.geometry("150x230+300+300")
root.resizable(False, False)
root.configure(bg="white")

label = tk.Label(root, text="Phone Book", font=("Arial", 16), bg="white")
label.pack(pady=10)

find_button = tk.Button(root, text="Find Contact", command=lambda: find_contact(contacts), bg="green", fg="white", font=("Arial", 12), width=13)
find_button.pack(pady=5)

add_button = tk.Button(root, text="Add Contact", command=lambda: add_contact(contacts), bg="blue", fg="white", font=("Arial", 12), width=13)
add_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Contact", command=lambda: edit_contact(contacts), bg="orange", fg="white", font=("Arial", 12), width=13)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=lambda: delete_contact(contacts), bg="red", fg="white", font=("Arial", 12), width=13)
delete_button.pack(pady=5)

root.mainloop()