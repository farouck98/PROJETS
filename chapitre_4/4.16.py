x = int(input("Entrez le premier nombre: "))
y = int(input("Entrez le second terme de la suite: "))

i = 0
while i < 20:
    z = int(input("Entrez la somme des deux termes précédents : "))
    if x+y != z:
        print(f"Fin du jeu. La valeur attendue est {x+y}")
        break
    else:
        x = y
        y = z
        i += 1
if i == 20:
    print(f"Vous avez gagné au bout de 20 tours")
else:
    print(f"Vous avez perdu au bout de {i+1} tours.")


