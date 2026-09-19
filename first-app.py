from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db= client["myfirstapp"]
users = db["users"]
name=input("Enter Your Name that need to search :  ")
new_name = input("Enter a Name to Be Updated  :  ")

users.update_one(
    {"name": name},
    {"$set": {"name" : new_name}}   
)
print("Name Changed Successfully!!")