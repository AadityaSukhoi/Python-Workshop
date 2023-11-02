# Define dictionaries
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50,6:60}

# Use the update() method to add the key-value pairs from dic2 and dic3 to dic1
dict1.update(dict2)
dict1.update(dict3)

# Print the updated dic1
print(dict1)