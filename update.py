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
        x = False
        ID = int(input("student's ID: "))
        for dicts in data:
            if ID == dicts["id"]:
                x = True
        if x== False:
            print("Invalid ID,Try Again")
            return
        
        commandOne=input("Do you want to change this student's name?...'Type yes or not':" )

        if commandOne=="yes":
            newName=name_validation()
            for dicts in data:
                if ID == dicts["id"]:
                    dicts["name"] =newName
                    print("updated succesfully")
        commandTwo=input("Do you want to change this student's surname?...'Type yes or not':" )
        if commandTwo=="yes":
            NewSurname=surname_validation()
            for dicts in data:
                if ID == dicts["id"]:
                    dicts["surname"]=NewSurname
                    print("updated succesfully")
        commandTree = input("Do you want to change this student's email?...'Type yes or not':")
        if commandTree=="yes":
            NewEmail=email_validation()
            for dicts in data:
                if ID == dicts["id"]:
                    dicts["surname"]=NewEmail
                    print("updated succesfully")
        with open("db.json", "w") as connect:
            json.dump(data, connect)




ChangeStudentsData()

