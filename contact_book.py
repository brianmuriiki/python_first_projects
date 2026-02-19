import json
   
FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []
    
# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact(contacts):
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")

# View contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    print("\nContact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")

        #search contact
def search_contact(contacts):
    name = input("Enter contact name to search: ")

    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Found: {contact['name']} - {contact['phone']} - {contact['email']}")
            found = True
    if not found:
        print("Contact not found.")

        #delete contact
def delete_contact(contacts):
    view_contacts(contacts)

    try:
        contact_num = int(input("Enter contact number to delete: "))
        if 1 <= contact_num <= len(contacts):
            removed = contacts.pop(contact_num - 1)
            save_contacts(contacts)
            print(f"Deleted contact: {removed['name']}")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Please enter a valid number.")

# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n==== CONTACT BOOK MENU ====")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()