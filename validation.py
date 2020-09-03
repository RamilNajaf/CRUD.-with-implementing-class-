import random
import json
with open('db.json') as json_file:
    data = json.load(json_file)
## functions for validationg needed input
def email_validation():
    while True:
        email=input("Student's Email: ")
        if "@"  not in email:
            print("Invalid inout! Try again: ")
        else:
            break
    return email

def id_validation():
    UniqID=random.randint(1, 101)
    print("Student's ID "+str(UniqID))
    for  info in data:
            if info["id"]==UniqID:
                print("This ID is used! Try again")
                id_validation()
    return UniqID


def name_validation():
    while True:
        name = input("Student's Name: ")
        check = any(char.isdigit() for char in name)

        if check:
            print("Invalid input! Try again!")
        else:
            break
    return name.title()


def surname_validation():
    while True:
        surname = input("Student's Surname: ")
        check = any(char.isdigit() for char in surname)

        if check:
            print("Invalid input! Try again!")
        else:
            break
    return surname.title()
