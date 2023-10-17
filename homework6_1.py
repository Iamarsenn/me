inp=input("write here the name of file: ")
try:
    with open(inp, 'r') as file:
        c=0
        for line in file:
            print(line.upper(),end='')
            c+=1
except FileNotFoundError:
    print("file does not exist")
