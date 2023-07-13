total = 0
count = 0

while True:
    try:
        number = input("Enter a number: ")

        if number.lower() == "done":
            break

        number = int(number)
        total += number
        count += 1

    except ValueError:
        print("Invalid input")
        continue

if count > 0:
    average = total / count
    print(total, count, average)
