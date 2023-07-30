# Prompt for a score between 0.0 and 1.0
score = input("Enter your score: ")

# Catch ValueError
try:
    score = float(score)
    # print score within range
    if 0.0 <=  score <= 1.0:
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
        print("Score out of Range 0.0 - 1.0")

except:
    print("Enter a numeric input")
