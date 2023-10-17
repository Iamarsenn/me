hoc = {}
hostcount=0
with open('mbox.txt', 'r') as file:
    for line in file:
        if line.startswith('From:'):
            email = line.split(':')[1]
            host = email.split('@')[1].strip()
            hoc[host] = hoc.get(host, 0) + 1
            hostcount+=1

for host, count in hoc.items():
    print("Host:", host, " Count:", count)

print("Total different hosts:", len(hoc))
print("Total hosts:",hostcount)
