new_list = []
end = False

while not end:
    nbr = int(input("Enter a number : "))
    if nbr == 0:
        end = True
        print(f"la liste définitive est {new_list}")
    elif nbr%2 == 0:
        new_list.append(nbr)
        print(new_list)
    elif nbr%2 != 0:
        new_list.pop(-1)
    else:
        print(new_list)

