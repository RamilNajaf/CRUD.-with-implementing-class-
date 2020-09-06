#updating students' info through their ID number

import json
from validation import name_validation
from validation import email_validation
from validation import surname_validation
def getDataFromJsonFile(_fileName):
    with open(_fileName,"r") as needed_db:
        return json.load(needed_db)

data=getDataFromJsonFile("db.json")
def ChangeStudentsData():
        for dicts in data:
            while True:
                ID=int(input("student's ID:"))
                if ID==dicts["id"]:
                    print("entered succesfuly")
                    break
                else:
                    print("invalid ID,Try again")

            break

        while True:
            commandOne = input("Do you want to change this student's name?...'Type yes or not':")
            x = "yes"
            y = "no"
            if commandOne == x or commandOne == y:
                break
            else:
                print("type right command")

        if commandOne=="yes":
            newName=name_validation()
            for dicts in data:
                if ID== dicts["id"]:
                    dicts["name"] =newName
                    print("updated succesfully")
        while True:
            commandTwo = input("Do you want to change this student's surname?...'Type yes or not':")
            if commandTwo == x or commandTwo == y:
                break
            else:
                print("type right command")
        if commandTwo=="yes":
            NewSurname=surname_validation()
            for dicts in data:
                if ID== dicts["id"]:
                    dicts["surname"]=NewSurname
                    print("updated succesfully")
        while True:
            commandTree = input("Do you want to change this student's email?...'Type yes or not':")
            if commandTree == x or commandTree == y:
                break
            else:
                print("type right command")
        if commandTree=="yes":
            NewEmail=email_validation()
            for dicts in data:
                if ID == dicts["id"]:
                    dicts["surname"]=NewEmail
                    print("updated succesfully")
        with open("db.json", "w") as connect:
            json.dump(data, connect)




ChangeStudentsData()

