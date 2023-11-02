#WAP a Python program to check whether given key in a dictionary already exists in a dictionary
#d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
key_to_check = int(input("Enter a key"))

if key_to_check in d:
   print("Key exists")
else:
   print("Key doesn't exist")
