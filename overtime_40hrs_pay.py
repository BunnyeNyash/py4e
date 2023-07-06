# Prompt the user for working hours
hours = input("Number of working hours: ")

# Prompt the user for pay-rate
rate = input("What's your hourly Pay rate: ")

# Convert the string values to float values
hours = float(hours)
rate = float(rate)

# Calculate over-time pay
if hours > 40 :
    over_time = (hours - 40)
    new_rate = (rate * 1.5)
    gross_pay = ((hours - over_time) * rate) + (over_time * new_rate)
else :
    gross_pay = hours * rate

# Print the gross pay
print("Gross pay: ", gross_pay)
