# Prompt the user to pick a letter
choice = input("Enter your choice from the English alphabets: ")

if choice == "a" :
    print("Bad guess")
elif choice == "o" :
    print("Good guess")
elif choice == "s" :
    print("Close but not correct")
else :
    print("Invalid Choice")
