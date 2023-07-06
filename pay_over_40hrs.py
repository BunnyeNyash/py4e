# Prompt the user for total number of working hrs
hours = input("Enter your working hours: ")

# Prompt user for pay rate on a hourly basis
rate = input("Enter your pay rate: ")

# Convert the input strings to float values
hours = float(hours)
rate = float(rate)

# Formula to calculate gross pay
if hours > 40 :
    new_rate = (1.5 * rate)
    gross_pay = hours * new_rate
else :
    gross_pay = hours * rate

print("Gross pay:", gross_pay)
