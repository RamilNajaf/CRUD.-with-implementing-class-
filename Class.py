import json
from validation import*
data = []
## classes to form db's structure
class StudentDictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

class User:
    def __init__(self,_id,_name, _surname,_email,):
        self.id=_id
        self.name = _name
        self.surname = _surname
        self.email=_email
        self.addDataToDict()   
    def addDataToDict(self):
        st_Dict = StudentDictionary()
        st_Dict.add('id',self.id)
        st_Dict.add('name', self.name)
        st_Dict.add('surname', self.surname)
        st_Dict.add('email',self.email)
        data.append(st_Dict)



