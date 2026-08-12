import json

print("Welcome to the Command-line Contact Book:    ")

# Menu Item 1


def view_contacts():
    with open("data.json", "r") as file:
        return json.load(file)

# Menu Item 2


def add_contacts():
    with open("data.json", "r") as file:
        data = json.load(file)

    first_name = input("firstname: ")
    last_name = input("lastname: ")
    contact_age = int(input("Age: "))

    new_record = {
        "firstname": first_name,
        "lastname": last_name,
        "age": contact_age
    }

    data.append(new_record)

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

# Menu Item 3


def search_contacts():
    with open("data.json", "r") as file:
        data = json.load(file)

    search_name = input("Enter a firstname:    ")

    found = False

    for person in data:
        if person.get("firstname") == search_name:
            print(f"\n{person}\n")
            found = True

        if found == False:
            print(
                f"\n{search_name} did not return a result.\nOur database is case-sensitive. Please try again.\n")

# Menu Item 4


def delete_contacts():
    with open("data.json", "r") as file:
        data = json.load(file)

    print("You have chosen to delete an entry.\nWhich contact should be deleted?:    ")

    firstdel = input("firstname:    ")

    lastdel = input("lastname:    ")

    try:
        agedel = int(input("age:    "))
    except ValueError:
        print("Please enter a number.")

    confirm_delete = input(
        f"You have chosen to remove {firstdel} {lastdel}, age: {agedel}. Would you like to proceed?:    y/n")
    if confirm_delete == "y":

        remove_data = {
            "firstname": firstdel,
            "lastname": lastdel,
            "age": agedel
        }

        data.remove(remove_data)

        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"\nMaybe some other time then.\n")


while True:
    action = int(input(
        "To View contacts, press 1: \nTo add a new contact, press 2: \nTo search for a contact, press 3:  \nTo delete a contact, press 4:   \nTo Exit, press 5:    "))

    if action == 1:
        print(f"\n{view_contacts()}\n")

    elif action == 2:
        add_contacts()
        print("Contact saved!\n")

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
