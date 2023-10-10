while True:
    inp=input("write here a sentence ")
    if inp == 'done':
        break
    punctuation_chars = ['?', '!', ',', '.', ':']
    for char in punctuation_chars:
        inp = inp.replace(char, '')
    inp=inp.upper()
    print(inp)
