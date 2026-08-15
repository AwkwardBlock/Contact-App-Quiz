import json


def delete_contacts():
    with open("data.json", "r") as file:
        data = json.load(file)

    print("You have chosen to delete an entry.\nWhich contact should be deleted?:    ")

    firstdel = input("firstname:    ")

    lastdel = input("lastname:    ")

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

    if confirm_delete == "y":
        data.remove(del_record)
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        print(f"\nMaybe some other time then.\n")


delete_contacts()
