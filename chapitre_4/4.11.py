nb_lines = int(input("Entrez un nombre : "))
for i in range(nb_lines):
    stars = "*" * (2 * i + 1)
    blanks = " " * (nb_lines - i - 1)
    line = blanks + stars + blanks
    print(line)

