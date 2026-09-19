from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["student_registration"]
students = db["students_details"]


def Main():
    lop = 1
    while lop==1:
        print("Welcome to Student Management System \n 1.Add Student \n 2.Search Details \n 3.Quit")
        lis = int(input("Enter your Option  :   "))

        if lis == 1:
            AddStudent()
        elif lis == 2:
            SearchStudent()
        else:
            break
def AddStudent():
    new_id = int(input("Enter the Student Roll Number  :  "))
    new_name = input("Enter the Student Name  :  ")
    dob = int(input("Enter the Date of Birth (yyyymmdd)  :  "))
    newadd={
        "id" : new_id ,
        "name" : new_name ,
        "dob" : dob
    }
    students.insert_one(newadd)

    print("Student Added Successfully!!!!")
    print("Student ID : " , new_id)

    lop = int(input("Do you want to Continue (0/1)  : "))
def SearchStudent():
        search = 1
        while search == 1:
            print("Search Details \n 1.Search by Name \n 2.Search by Roll Number \n 3.Search by Date of Birth")
            search_box = int(input("Enter your Option  :  "))
            if search_box==1:
                 SearchStudent_Name()
            elif search_box==2:
                 SearchStudent_ID()
            elif search_box==3:
                 SearchStudent_DOB()
            else:
                 continue
def SearchStudent_Name():
            search_name = input("Enter the Student Name  :  ")
            results = students.find({
                "name" : {
                    "$regex" : search_name ,
                    "$options" : "i"
                }
            })
    
            if results:
                print("|ID  \t Name |")
                for i in results:
                    print(i["id"] , "\t" , i["name"])
                print("--------------------------")
def SearchStudent_ID():
     search_name = int(input("Enter the ID of the Student  :  "))
     results = students.find({
          "id" : search_name
     })

     if results:
          print("|ID  \t Name |")
          for i in results:
              print(i["id"] , "\t" , i["name"])
          print("--------------------------")
def SearchStudent_DOB():
     search_name = int(input("Enter the DOB of the Student (yyyymmdd)  :  "))
     results = students.find({
               "dob" : search_name
          })
     if results:
         print("|ID  \t Name |")
         for i in results:
              print(i["id"] , "\t" , i["name"])
         print("--------------------------")

Main()