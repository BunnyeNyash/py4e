# Create variables to hold smallest and largest values
smallest = None
largest = None

while True:
    # prompt user for an integer number
    num = input("Enter a number: ")

    try:
        num = int(num)

        if smallest is None or num < smallest:
            smallest = num

        if largest is None or num > largest:
            largest = num

    except ValueError:
        print("Invalid input")

    if num == "done":
        break

if smallest != None and largest != None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
