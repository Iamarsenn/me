def salary_calc(hours, rate):
    if hours <0 or rate <0:
        return "error,enter value number"
    if hours > 40 :
        payment = (40 * rate)+((hours - 40) * (1.5 * rate))
    else:
        payment = hours * rate
    return payment
while True:
    try:
        hours = float(input("Enter hours: "))
        rate = float(input("Enter rate per hour: "))
        salary = salary_calc(hours, rate)
        print("Total salary:",salary)
    except ValueError:
        print("Error, please enter valid numeric values for hours and rate")
