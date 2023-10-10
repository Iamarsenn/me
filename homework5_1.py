while True:
    inp = input("Enter two words or 'done' to terminate: ")

    if inp == 'done' or inp == '':
        break
    try:
        x=inp.index(" ")
        word1 = str(inp[:x])
        word2 = str(inp[x + 1:])
    except ValueError:
        print("not enough words")
    if " " in inp:
        if word1 < word2:
            print("the word that comes before is:", word1)
        elif word2 < word1:
            print("the word that comes before is:", word2)
        else:
            print("words are the same:", word1)
