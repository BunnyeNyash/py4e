# Prompt user for score
score = input("Your Score between 0.0 and 1.0: ")

# Define the computepay function
def computepay(score):

    score = float(score)

    if 0.0 <= score <= 1.0:
        try:
            if score >= 0.9:
                print("A")
            elif score >= 0.8:
                print("B")
            elif score >= 0.7:
                print("C")
            elif score >= 0.6:
                print("D")
            elif score < 0.6:
                print("F")

        except ValueError:
            print("Bad Score")

    else:
        print("Bad Score")

# Call the function computepay
computepay(score)
