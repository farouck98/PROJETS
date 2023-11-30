l = ["a", "b", "c", "d", "e"]

#Concatener la valeur à l'index à la valeur qui suit
#print([l[i] + l[i+1] for i in range(len(l)-1)])

#Concatener seulement la valeur à l'index pair à la valeur qui suit
print([l[i] + l[i+1] if i%2==0 else l[i] for i in range(len(l)-1)])
