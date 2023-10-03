def calc_grade(score):
    if score < 0 or score > 100:
        return "Error,score is out of range"
    elif score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F,work harder"

while True:
    try:
        score = int(input("Enter a score between 0 and 100: "))
        grade = calc_grade(score)
        print("Grade:",grade)
    except ValueError:
        print("Error, please enter a valid numeric score")
