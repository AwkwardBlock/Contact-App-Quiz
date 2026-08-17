import json
import re

print("=================================================")
print("-------------------------------------------------")
print("    WELCOME TO THE COMMAND-LINE CONTACT BOOK:    ")
print("-------------------------------------------------")
print("=================================================")

# REGEX validation


def quick_check_email(email_address):
    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(EMAIL_REGEX, email_address.strip()))


def quick_check_phone(phone_num):
    PHONE_REGEX = re.compile(
        r"(\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    return bool(re.fullmatch(PHONE_REGEX, phone_num))


# json mgmt

def read_file():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def write_file(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
        return

# Menu Item 5


def filter_contacts():
    data = read_file()

    print("\nWhich category would you like to see?")
    category = input("\n").strip().lower()

    cat_sort = []

    found = False

    for person in data:
        if person.get("category", "").strip().lower() == category:
            found = True
            cat_sort.append(person)

    if not found:
        cat_sort = "We didn't find that Category"
        print(cat_sort)
        return

    print(cat_sort)

# Menu Item 1


def view_contacts():
    contacts = read_file()

    if not contacts:
        print("\nYour contact book is empty.\n")
        return

    print("\n===================================")
    print("          MY CONTACT BOOK          ")
    print("===================================")

    for val in contacts:

        print("--------------------------------")
        print(
            f"   Name:  {val['firstname'].title()} {val['lastname'].title()}")
        print(f"   Age:   {val['age']}")
        print(f"   Email: {val['email']}")
        print(f"   Phone: {val['phone']}")
        print(f"   category: {val['category']}")
        print("--------------------------------")

# Menu Item 2


def add_contacts():
    data = read_file()

    first_name = input("firstname: ").lower()

    if first_name.lower() == "cancel":
        print("Adding contact cancelled.")
        return

    last_name = input("lastname: ").lower()

    if last_name.lower() == "cancel":
        print("Adding contact cancelled")
        return

    try:
        contact_age = int(input("Age: "))
    except ValueError:
        print("\nAge, please, in digits.\n")
        return

    email_address = input("email: ").lower()

    if not quick_check_email(email_address):
        print("\nInvalid email address.\n")
        return

    phone_num = input("phone:  ")

    if not quick_check_phone(phone_num):
        print("\nInvalid Phone Number.\n")
        return

    con_cat = input("How do you know this person?:  ").lower()

    new_record = {
        "firstname": first_name,
        "lastname": last_name,
        "age": contact_age,
        "email": email_address,
        "phone": phone_num,
        "category": con_cat
    }

    data.append(new_record)

    write_file(data)
    print("Contact saved!\n")

# Menu Item 3


def search_contacts():
    data = read_file()

    search_name = input("Enter a name:    ").lower()

    if search_name == "cancel":
        print("Search contact cancelled.")
        return

    found = False

    for person in data:
        firstname = person.get("firstname", "").strip().lower()
        lastname = person.get("lastname", "").strip().lower()

        if search_name in firstname or search_name in lastname:
            print("===========================")
            print("---------------------------")
            print("       CONTACT FOUND       ")
            print("---------------------------")
            print("===========================")
            print(
                f"\nName:  {person['firstname'].title()} {person['lastname'].title()}")
            print(f"\nAge:   {person['age']}")
            print(f"\nemail: {person['email']}")
            print(f"\nphone: {person['phone']}")
            print(f"\ncategory: {person['category']}")
            print("---------------------------")
            found = True

    if not found:
        print(
            f"\n{search_name} did not return a result.\n")

# Menu Item 4


def delete_contacts():
    data = read_file()

    print("You have chosen to delete an entry.\nWhich contact should be deleted?:    ")

    firstdel = input("firstname:    ").strip().lower()
    if firstdel == "cancel":
        print("Delete contact cancelled")
        return

    lastdel = input("lastname:    ").lower()
    if lastdel == "cancel":
        print("Delete contact cancelled")
        return

    del_record = {
        "firstname": firstdel,
        "lastname": lastdel
    }

    target_person = None
    for person in data:
        if (
            person.get("firstname", "").lower() == firstdel
            and person.get("lastname", "").lower() == lastdel
        ):
            target_person = person
            break

    if not target_person:
        print(
            f"{del_record['firstname']} {del_record['lastname']} doesn't seem to be in our system.")
        return

    confirm_delete = input("\nWould you like to proceed?:y/n    ").strip()

    if confirm_delete == "cancel":
        print("Delete contact cancelled")
        return

    if confirm_delete == "y" or confirm_delete == "Y" or confirm_delete == "yes" or confirm_delete == "YES":
        data.remove(target_person)
        write_file(data)
        print("Contact deleted!")
    else:
        print(f"\nMaybe some other time then.\n")


while True:
    print("\n1: View contacts")
    print("2: Add a new contact")
    print("3: Search for a contact")
    print("4: Delete a contact")
    print("5: Filter contacts (temp)")
    print("6: Exit")
    print("\nReturn to this menu at any time by typing 'cancel'")

    action = input("Choose an option: ")

    if action.lower() == "cancel":
        print("\nThat won't do anything here, silly goose\n")
        continue

    try:
        action = int(action)
    except ValueError:
        print("\nPlease choose 1 through 5\n")
        continue

    if action == 1:
        view_contacts()

    elif action == 2:
        add_contacts()

    elif action == 3:
        search_contacts()

    elif action == 4:
        delete_contacts()

    elif action == 5:
        filter_contacts()

    elif action == 6:
        print("Goodbye")
        break

    else:
        print("\nPlease choose 1 through 5\n")
        continue
