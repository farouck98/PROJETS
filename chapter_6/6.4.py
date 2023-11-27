demo_list = [5, 1, 59, 42, 8, 3, 15, 9, 7]

def list_average(l : list):
    somme = 0
    for i in l:
        somme += i
    return round(somme/len(l), 3)
print(list_average(demo_list))