# Function computepay taking parameters (hours and rate).

def computepay(hours, rate):
    gross_pay = hours * rate
    return gross_pay

def overtime_computepay(hours, rate):
    new_gross_pay = regular_pay + overtime_pay
    return new_gross_pay

# Prompt user for working hours
hours = input("Total number of working hours: ")

# Prompt user for pay rate on a hour basis
rate = input("Your pay rate: ")


# Calculate gross pay
try:
    hours = float(hours)
    rate = float(rate)

    regular_pay = 40 * rate

    if hours > 40:
        overtime_hours = hours - 40
        overtime_rate = rate + (rate / 2)
        overtime_pay = overtime_hours * overtime_rate
    
        # Print the gross pay
        print("Pay", overtime_computepay(hours, rate))
    
    else:
       print("Pay", computepay(hours, rate))

except ValueError:
    print("Please enter a numerical value")
