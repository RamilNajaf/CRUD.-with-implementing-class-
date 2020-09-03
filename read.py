## looking students' information through their ID number
import json
def getDataFromJsonFile(_fileName):
    with open(_fileName,"r") as needed_db:
        return json.load(needed_db)

data=getDataFromJsonFile("db.json")

def ReadStudentsData():
    ID = int(input("Student's ID:"))
    check=False
    for dicts in data:
        if ID==dicts["id"]:
            check=True
            print("your name: " + dicts["name"],"your surname: " +dicts["surname"]+" your email: "+dicts["email"])
    if check==False:
        print("Invalid ID!Try Again")
        ReadStudentsData()
    


