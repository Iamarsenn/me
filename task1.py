decision=input("print c if you want to make farenheits \nprint f if you want to make celciums ")
if decision=="c":
    celciums=float(input("write here your celciums "))
    print((celciums * 9/5) + 32,"farenheits")
if decision=="f":
    farenheits=float(input("write here your farenheits "))
    print((farenheits-32) * 5/9,"celciums")
