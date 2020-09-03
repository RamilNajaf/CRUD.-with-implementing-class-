import json
def getDataFromJsonFile(_fileName):
    with open(_fileName,"r") as needed_db:
        return json.load(needed_db)
## deleting student's info through their id number
data=getDataFromJsonFile("db.json")


def DeleteStudentInfo():
    while True:
        id = int(input("type stunden's ID number for deleting his or her information: "))
        check = False
        for dicts in data:
            if id == dicts["id"]:
                check = True
        if check == True:

            for dicts in data:
                 if dicts["id"] == id:
                     data.pop(data.index(dicts))
                     print("Deleted Succesfully")
                     with open("db.json", "w") as connect:
                         json.dump(data, connect)
                     break
            break
        if check==False:
            print("Invalid Input!Try Again")
            
        
DeleteStudentInfo()