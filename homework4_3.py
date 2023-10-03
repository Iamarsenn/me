def divide3(numb):
    count = 0
    for i in range(1, numb + 1):
        if i % 3 == 0:
            count += 1
    return count


while True:
    inp = input("Enter a positive integer or 'done': ")
    if inp == 'done':
        break

    try:
        numb = int(inp)
        if numb < 0:
            print("Please enter a positive integer")
        else:
            result = divide3(numb)
            print("Numbers divisible by 3 from 1 to", numb,":", result)
    except ValueError:
        print("Invalid input,please enter a positive integer or 'done'")
