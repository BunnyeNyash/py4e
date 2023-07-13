numbers = []
while True:
    try:
        number = input("Enter a number: ")

        if number.lower() == "done":
            break

        number = int(number)
        numbers.append(number)

    except ValueError:
        print("Invalid input")
        continue

if numbers: 
    total = sum(numbers)
    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    print(total, count, minimum, maximum)
