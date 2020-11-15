import json
from tinydb import TinyDB, Query

db = TinyDB("db.json")  # Initialise the databse in json format
print("\n Setup DB")

db.truncate()  # Purge the databse of any previous entries

# Test inserting value into db
db.insert({"name": "James"})  # Insert data into the database
db.insert({"dob": "10 11 91"})
db.insert({"city": "London"})
db.insert({"job": "Network Engineer"})

for i in db:  # Iters over the db to print out line by line
    print(i)


print("\n" + "*" * 50)
