a = int(input("Ange en längd för sida ett: "))
b = int(input("Ange en längd för sida två: "))

print("Höjden | Volymen")
print("-----------------")

for i in range(1,11):
    print(i," | ", a*b*i)