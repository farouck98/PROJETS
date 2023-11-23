
demo_list = [5, 1, 59, 42, 8, 3, 15, 9, 7]

def moy(list):
        somme = 0
        for i in list:
           somme = somme + i
           moyenne = somme / len(list)
        print(moyenne)

moy(demo_list)