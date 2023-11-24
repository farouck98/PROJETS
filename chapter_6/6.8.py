def reverse_number(nbr: float):
    str_nbr = str(nbr)
    if str_nbr[0] == "-":
        str_nbr = "-" + str_nbr[:0:-1]
    else:
        str_nbr = str_nbr[::-1]
    result = float(str_nbr)
    return result

print(reverse_number(-123))