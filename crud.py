from pymongo import MongoClient
from bson import json_util
from bson.json_util import dumps
import json

client = MongoClient('localhost:27017')
db = client.EmployeeData

def main():
  while(1):
  # Choosing option to do CRUD operations
    selection = input('\nSelect 1 to insert, 2 to update, 3 to read, 4 to delete\n')
    
    if selection == '1':
      insert()
    elif selection == '2':
      update()
    elif selection == '3':
      read()
    elif selection == '4':
      delete()
    else:
      print('\n INVALID SELECTION \n')

def insert():
  try:
    employeeID = input('Enter employee ID: ')
    employeeName = input('Enter employee Name: ')
    employeeAge = input('Enter employee Age: ')
    employeeCountry = input('Enter employee Country: ')
    
    db.Employees.insert_one(
      {
        "id": employeeID,
        "name": employeeName,
        "age": employeeAge,
        "country": employeeCountry
      }
    )
    
    print('\Data Inserted Successfully\n')
    
  except Exception as e:
    print(str(e))
    
def read():
  try:
    employeeCollection = dumps(db.Employees.find())
    print('\nAll data from EmployeeData Database \n')
    print(employeeCollection)
      
  except Exception as e:
    print(str(e))
    
def update():
  try:
    criteria = input('\nEnter ID of Employee to be updated: \n')
    newEmployeeName = input('\nEnter new Employee Name: \n')
    newEmployeeAge = input('\nEnter new Employee Age: \n')
    newEmployeeCountry = input('\nEnter new Employee Country: \n')
    
    db.Employees.update_one(
      {
        "id": criteria
      },
        {
          "$set": {
            "name": newEmployeeName,
            "age": newEmployeeAge,
            "country": newEmployeeCountry
          }
        }
    )
    print('\nRecords Updated Successfully')
    
  except Exception as e:
    print(str(e))
    
def delete():
  try:
    criteria = input('\nEnter ID of Employee to be deleted: \n')    
    db.Employees.delete_one({"id": criteria})
    print('\nRecord Deleted Successfully\n')
    
  except Exception as e:
    print(str(e))
    
main()