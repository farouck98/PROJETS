#nbre_utilisateur = float(input("Entrez un nombre : "))
#rep = input("Voulez-vous continuer Y/N ? : ")
#while rep == "y" or rep == "yes":
    #nbre_utilisateur = nbre_utilisateur + float(input("entrez un nombre : "))
    #rep = input("Voulez-vous continuer Y/N ? : ").lower()
#print(f"la somme de tous les nombres est {nbre_utilisateur}")

nbr = float(input("Enter a number : "))
end = False
while not end:
    rep = input("Do you want to continue Y/N ? :").lower()
    if rep == "y" or rep == "yes":
        nbr = nbr + float(input("Enter a number : "))
    elif rep == "n" or rep == "no":
        print(f"la somme de tous les nomres entrés est : {nbr}")
        end = True
    else:
        print(" enter y/yes or n/no ")

