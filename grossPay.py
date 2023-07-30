# Prompt user for working hours
hours = input("Enter working hours: ")

# Prompt user for pay rate on a hourly basis
rate = input("Enter pay rate: ")

hours = float(hours)
rate = float(rate)
if hours <= 40:
    grossPay = hours * rate
else:
    grossPay = 40 * rate
    if hours > 40:
        newHours = hours - 40
        newRate = rate * 1.5
        newGrossPay = grossPay + (newHours * newRate)
        print(newGrossPay)
    else:
        print(grossPay)
