# Prompt the user for a score
score = input("Your score between 0.0 and 0.9: ")

# Define computepay function taking argument score

def computepay(score):
    try:
        score = float(score)

        if 0.0 <= score <= 1.0:
            # Grade Calculation Logic
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
        else:
             print("Bad Score")

    except ValueError:
        print("Bad Score")

# Call the computepay function
computepay(score)
