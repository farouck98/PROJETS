num = int(input("Entrez un nombre : "))
if num == 0:
    print("Entrez un autre nombre")
for multiple in range(0, 101):
    if multiple % num == 0:
        print(f"{multiple} est un multiple de {num}")



