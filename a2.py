#WAP a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#Sample dictionary (n=5):
#Expected Output: {1: 1, 2: 4, 3: 9,4: 16, 5: 25 }

n = int(input("Please enter the Maximum Number: "))
myDict = {}
for x in range(1, n + 1):
   myDict[x] = x * x
print("Dictionary = ", myDict)
