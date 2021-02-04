sida1 = []
sida2 = []
area = []
counter = 0

while True: 
    x = str(input("Vill du göra en beräkning till? (J/N): "))
    if x == "J":

        a = int(input("Ange en längd för sida ett: "))
        b = int(input("Ange en längd för sida två: "))
        ae = a*b

        sida1.append(a)
        sida2.append(b)
        area.append(ae)

        print("Höjden | Volymen")
        print("-----------------")

        for i in range(1,11):
            print(i," | ", a*b*i)
        counter += 1
    else:
        for h in range(counter):
            if sida1[h] == sida2[h]:
                print(f"Rektangeln har sidorna {sida1[h]} och {sida2[h]} vilket gör att arean är {area[h]}, det är en kvadrat.")
            else:
                print(f"Rektangeln har sidorna {sida1[h]} och {sida2[h]} vilket gör att arean är {area[h]}")