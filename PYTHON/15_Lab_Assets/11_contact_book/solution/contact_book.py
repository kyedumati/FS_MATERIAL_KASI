"""SOLUTION — contact dict menu (no def/json/pathlib — those weeks later)."""

contacts = {}

while True:
    print("1 add  2 lookup  3 delete  4 list  5 quit")
    c = input("> ").strip()
    if c == "1":
        name = input("name: ").strip().title()
        phone = input("phone: ").strip()
        contacts[name] = phone
    elif c == "2":
        name = input("name: ").strip().title()
        phone = contacts.get(name)
        if phone is None:
            print("Not found")
        else:
            print(phone)
    elif c == "3":
        name = input("name: ").strip().title()
        if name in contacts:
            del contacts[name]
            print("Deleted")
        else:
            print("Not found")
    elif c == "4":
        print(contacts)
    elif c == "5":
        break
    else:
        print("Invalid choice")
