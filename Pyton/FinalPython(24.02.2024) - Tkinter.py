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
    with open(filename, 'w') as file:
        for name, phone in contacts.items():
            file.write(f"{name}: {phone}\n")

def find_contact(contacts):
    search_term = simpledialog.askstring("Find Contact", "Enter name or phone to search:")
    if search_term is not None:
        search_term = search_term.lower()  # Convert to lowercase for case-insensitive search
        found_contacts = []

        for name, phone in contacts.items():
            if search_term in name.lower() or search_term in phone.lower():
                found_contacts.append(f"{name}: {phone}")

        if found_contacts:
            result = "\n".join(found_contacts)
            messagebox.showinfo("Contact Found", f"Found contact:\n{result}")
        else:
            messagebox.showinfo("Contact Not Found", f"No contacts found for '{search_term}'.")

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

def create_menu_window():
    menu_window = tk.Tk()
    menu_window.title("Contact Manager")
    menu_window.geometry("150x180+500+200")
    
    # window_width = 300
    # window_height = 250

    # x_position = 1000
    # y_position = 1000

    button_width = 20  # Set the width for all buttons

    find_button = tk.Button(menu_window, text="Find Contact", width=button_width, command=lambda: find_contact(contacts))
    find_button.pack(pady=5)

    add_button = tk.Button(menu_window, text="Add Contact", width=button_width, command=lambda: add_contact(contacts))
    add_button.pack(pady=5)

    edit_button = tk.Button(menu_window, text="Edit Contact", width=button_width, command=lambda: edit_contact(contacts))
    edit_button.pack(pady=5)

    remove_button = tk.Button(menu_window, text="Remove Contact", width=button_width, command=lambda: remove_contact(contacts))
    remove_button.pack(pady=5)

    exit_button = tk.Button(menu_window, text="Exit", width=button_width, command=menu_window.destroy)
    exit_button.pack(pady=5)

    return menu_window

if __name__ == "__main__":
    contacts = load_contacts()
    menu_window = create_menu_window()
    menu_window.mainloop()