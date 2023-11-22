demo_list = [5, 1, 59, 42, 8, 3, 15, 9, 7]
size_list = len(demo_list)
somme = demo_list[0]
#somme = sum(demo_list)
#print("somme = ", somme)
for i in range(1, size_list):
   somme = somme + demo_list[i]
print( somme )
