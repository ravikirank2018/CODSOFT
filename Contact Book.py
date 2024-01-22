import tkinter as tk
from tkinter import messagebox

class ContactBookGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")

        self.contacts = []

        self.name_label = tk.Label(root, text="Name:")
        self.name_entry = tk.Entry(root)

        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_entry = tk.Entry(root)

        self.email_label = tk.Label(root, text="Email:")
        self.email_entry = tk.Entry(root)

        self.address_label = tk.Label(root, text="Address:")
        self.address_entry = tk.Entry(root)

        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)
        self.search_button.grid(row=6, column=0, columnspan=2, pady=5)
        self.update_button.grid(row=7, column=0, columnspan=2, pady=5)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", f"Contact '{name}' added successfully.")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone are required fields.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "Contact list is empty.")
        else:
            contact_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        search_name = self.name_entry.get()
        if search_name:
            results = [contact for contact in self.contacts if search_name.lower() in contact['name'].lower()]
            if results:
                contact_list = "\n".join([f"{contact['name']}: {contact['phone']}" for contact in results])
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Search Results", "No matching contacts found.")
        else:
            messagebox.showerror("Error", "Enter a name to search.")

    def update_contact(self):
        name = self.name_entry.get()
        field = self.phone_entry.get()  # Assuming phone entry is used for field input
        new_value = self.email_entry.get()

        if name and field and new_value:
            for contact in self.contacts:
                if contact['name'] == name:
                    contact[field] = new_value
                    messagebox.showinfo("Success", f"Contact '{name}' updated successfully.")
                    self.clear_entries()
                    return
            messagebox.showinfo("Info", f"No matching contact found with name '{name}'.")
        else:
            messagebox.showerror("Error", "Name, field, and new value are required fields.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name:
            for contact in self.contacts:
                if contact['name'] == name:
                    self.contacts.remove(contact)
                    messagebox.showinfo("Success", f"Contact '{name}' deleted successfully.")
                    self.clear_entries()
                    return
            messagebox.showinfo("Info", f"No matching contact found with name '{name}'.")
        else:
            messagebox.showerror("Error", "Enter a name to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookGUI(root)
    root.mainloop()
