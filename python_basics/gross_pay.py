# Prompts the user for working hours
hours = float(input("What is the total number of your working hours? "))

# Prompts the user for pay rate per hour
rate = float(input("What is your pay rate on a hourly basis? "))

gross_pay = hours * rate

print("Your gross pay is: ", gross_pay)
