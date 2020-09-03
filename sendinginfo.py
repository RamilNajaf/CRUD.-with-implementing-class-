from Class import *
##.... function to renew db.json's datas

def addNewUserToDb():
    UniqeId = id_validation()
    name = name_validation()
    surname = surname_validation()
    email = email_validation()
    User(UniqeId, name, surname, email)
    print("Students imformation is stored succesfully")




with open("db.json", "w") as conn:
    json.dump(data, conn)

