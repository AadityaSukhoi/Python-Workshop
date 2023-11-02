#Creating a dictionary
student = {
    "name" : "Alice",
    "age" : 25,
    "grade" : "A"
 }
print(student)

#Accessing Dictionary Values by key
name = student["name"]
age = student["age"]

#Modifying a value
student["age"] = 26

#Adding a new key value pair
student["city"] = "New York"

#Iterating through a dictionary
for key, value in student.items():
    print(f"{key}: {value}")

#Checking if a key exists
if "age" in student:
    print("Age exists in the dictionary")