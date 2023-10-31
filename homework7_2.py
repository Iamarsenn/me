uws = []
fhand = open("C:/Users/user/Downloads/romeo.txt",'r')
for line in fhand:
    ws = line.split()
    for w in ws:
        if w not in uws:
            uws.append(w)

uws.sort()

for w in uws:
    print(w)
