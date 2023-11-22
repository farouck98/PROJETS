nbr = float(input("Entrez un nombre : "))
for i in range(10):
    nbr = nbr * 1.025
    message = f"Year +{i + 1} : {round(nbr, 3)}"
    print(message)




