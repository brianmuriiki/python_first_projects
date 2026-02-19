import json
import random
import string

FILE_NAME = "passwords.json"


# -------------------------
# Load Data
# -------------------------
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {}


# -------------------------
# Save Data
# -------------------------
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# -------------------------
# Generate Password
# -------------------------
def generate_password():
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()"

    password = (
        random.choice(letters) +
        random.choice(numbers) +
        random.choice(symbols)
    )

    password += ''.join(random.choice(letters + numbers + symbols) for _ in range(8))

    print("Generated Password:", password)
    return password


# -------------------------
# Add Password
# -------------------------
def add_password(data):
    website = input("Enter website: ")
    username = input("Enter username: ")

    choice = input("Generate password? (y/n): ")

    if choice.lower() == "y":
        password = generate_password()
    else:
        password = input("Enter password: ")

    data[website] = {
        "username": username,
        "password": password
    }

    save_data(data)
    print("Saved successfully.")


# -------------------------
# Search Password
# -------------------------
def search_password(data):
    website = input("Enter website to search: ")

    if website in data:
        print("Username:", data[website]["username"])
        print("Password:", data[website]["password"])
    else:
        print("No data found.")


# -------------------------
# Menu
# -------------------------
def main():
    data = load_data()

    while True:
        print("\n==== PASSWORD MANAGER ====")
        print("1. Add Password")
        print("2. Search Password")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_password(data)
        elif choice == "2":
            search_password(data)
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid option")


main()
