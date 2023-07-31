# Define the computepay() function
def computepay(hours, rate):
    grossPay = hours * rate
    return grossPay

# Prompt user for working hours
hours = input("Enter working hours: ")

# Prompt the user for pay rate on a hourly basis
rate = input("Enter your pay rate: ")

# Type conversion
hours = float(hours)
rate = float(rate)

if hours > 40:
    overtimeHours = hours - 40
    overtimeRate = rate * 1.5
    overtimePay = overtimeHours * overtimeRate
    gross_pay = (40 * rate) + overtimePay
    print("Pay",gross_pay)

else:
    print("Pay",computepay(hours, rate))
