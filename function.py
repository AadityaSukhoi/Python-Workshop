def my_functionloc():
    x=10       #x is a local variable
    print(x)   #Accessing the local variable 

my_functionloc()



x=20 #x is a global variable
def my_functionglob():
    print(x) #Accessing the global variable

my_functionglob()