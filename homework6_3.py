filename = input("Enter the name of the file: ")

try:
    filename2=open(filename,'r')
    count = 0
    total = 0
    for line in filename2:
        if line.startswith('X-DSPAM-Confidence:'):
            number = float(line.split(': ')[1])
            count += 1
            total += number
    if count > 0:
        average = total / count
        print("Average DSPAM:", average)
    else:
        print("No 'DSPAM' lines found")
except FileNotFoundError:
    print("File not found:", filename)
