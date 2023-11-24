l = [1, 2, 3, 4]


def find_index(ml: list, valeur: int):
    if ml == [] or ml is not None:
        for i in range(len(ml)):
           if ml[i] ==  valeur:
             return i
    else:
        return None
print(find_index(l, 5))