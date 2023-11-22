list = []
end = False
while not end:
    nbr = int(input("Entrez un nombre : "))
    if nbr == 0:
       print(f"la liste définitive est :{list}")
       end = True
    elif nbr % 2 == 0:
        list.append(nbr)
        print(list)
    elif nbr % 2 > 0:
        list.pop(-1)
        print(list)
    else:
        print(list)

