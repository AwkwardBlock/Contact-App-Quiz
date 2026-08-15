import json
import re

print("Welcome to the Command-line Contact Book:    ")
# json mgmt


def read_file():
    with open("data.json", "r") as file:
        return json.load(file)


def write_file(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        return

# Menu Item 1


def view_contacts():
    contacts = read_file()

    for val in contacts:
        print(
            f"\nName:{val['firstname']} {val['lastname']} \nAge:{val['age']} \nEmail:{val['email']}")

# Menu Item 2


def add_contacts():
    data = read_file()

    first_name = input("firstname: ").lower()
    last_name = input("lastname: ").lower()

    try:
        contact_age = int(input("Age: "))
    except ValueError:
        print("\nPlease enter a number.\n")
        return

    email_address = input("email: ").lower()

    def quick_check_email(email_address):
        EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.fullmatch(EMAIL_REGEX, email_address.strip()))

    if not quick_check_email(email_address):
        print("\nInvalid email address.\n")
        return

    new_record = {
        "firstname": first_name,
        "lastname": last_name,
        "age": contact_age,
        "email": email_address
    }

    data.append(new_record)

    write_file(data)
    print("Contact saved!\n")

# Menu Item 3


def search_contacts():
    data = read_file()

    search_name = input("Enter a name:    ").lower()

    found = False

    for person in data:
        if person.get("firstname") == search_name or person.get("lastname") == search_name:
            print(f"\n{person}\n")
            found = True

    if found == False:
        print(
            f"\n{search_name} did not return a result.\n")

# Menu Item 4


def delete_contacts():
    data = read_file()

    print("You have chosen to delete an entry.\nWhich contact should be deleted?:    ")

    firstdel = input("firstname:    ").lower()

    lastdel = input("lastname:    ").lower()

    try:
        agedel = int(input("age:    "))
    except ValueError:
        print("\nPlease enter a number.\n")
        return

    del_record = {
        "firstname": firstdel,
        "lastname": lastdel,
        "age": agedel
    }

    found = False

    for person in data:
        if person == del_record:
            print(f"You have chosen to delete {del_record}")
            found = True

    if found == False:
        print(f"{del_record} doesn't seem to be in our system.")
        return

    confirm_delete = input("\nWould you like to proceed?:y/n    ")

    if confirm_delete == "y" or confirm_delete == "Y" or confirm_delete == "yes" or confirm_delete == "YES":
        data.remove(del_record)
        write_file(data)
    else:
        print(f"\nMaybe some other time then.\n")


while True:
    try:
        action = int(input(
            "\nTo View contacts, press 1: \nTo add a new contact, press 2: \nTo search for a contact, press 3:  \nTo delete a contact, press 4:   \nTo Exit, press 5:    "))
    except ValueError:
        print("\nHmm. That's not quite right.\n")
        continue

    if action == 1:
        view_contacts()

    elif action == 2:
        add_contacts()

    elif action == 3:
        search_contacts()

    elif action == 4:
        delete_contacts()
        continue

    elif action == 5:
        print("Goodbye")
        break

    else:
        print("\nYou weren't paying attention\n")
        continue
