
l4= [1, 2, 3, 6]
l5 = [1, 2, 3, 7, 9]
def list_common_element(l1: list, l2: list):
    #autre méthode
    """l3 = []
    for i in l1:
        for j in l2:
            if i == j and i not in l3:
              l3.append(i)
    return l3"""

    set1 = set(l1)
    set2 = set(l2)
    return list(set1.intersection(set2))


print(list_common_element(l4, l5))
