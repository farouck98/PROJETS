
def prime_number(nbr):
    if nbr in {0, 1, 2}:
        return True
    elif nbr == 2:
        return False
    else:
         for i in range(2, nbr):
             if nbr % i != 0:
                return True
    return False
print(prime_number(1))