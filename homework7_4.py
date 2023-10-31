a = []
while True:
    inp = input("Write here an integer, Typing 'done' will exit the program: ")
    if inp == "done":
        break
    try:
        inp = int(inp)
        a.append(inp)
        if len(a) > 0:
            average = sum(a) / len(a)
            print("average=", average)
    except ValueError:
        print("Invalid input, enter a correct integer or 'done'.")
