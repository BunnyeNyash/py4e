x = 10 # Global variable

def update_global() : #Modifying the global variable x
    global x # Declaring x as global variable
    x += 5

def print_global() : # Output: 15
    print(x)
