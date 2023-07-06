# Prompts user for a score
score = input("Score between 0.0 and 1.0: ")

try :
    score = float(score)

    if int(score * 10) in range(0, 11):
        if score >= 0.9 :
            print("A")
        elif score >= 0.8 :
            print("B")
        elif score >= 0.7 :
            print("C")
        elif score >= 0.6 :
            print("D")
        elif score < 0.6 :
            print("F")
    else :
        print("Bad Score")

except ValueError : 
    print("Bad Score")
