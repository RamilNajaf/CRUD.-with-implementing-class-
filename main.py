from read import *
from update import ChangeStudentsData
from sendinginfo import *
from delete import DeleteStudentInfo
a=int(input(f'''press 1 for looking student's info 
press 2 for altering student's info
press 3 for sending new info to db
press 4 for deleting student's info
your command: '''
             ))
if a==1:
    ReadStudentsData()
if a==2:
    ChangeStudentsData()
if a==3:
    for i in range(5):
        addNewUserToDb()
if a==4:
    DeleteStudentInfo()

