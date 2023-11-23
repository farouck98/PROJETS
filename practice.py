#listcomprehension
l1 = ["a", "b", "c", "d", "e", "f"]

#expression for i in iterator
#l4 = [l1[i] + l1[i+1] if i %2 == 0 else l1[i] for i in range(len(l1)-1)]
#print(l4)

l2 = [l1[i] for i in range(len(l1)-1) if i % 2 == 0]
print(l2)

#list comprehension pour la liste contenant le carré des expressions
#l3 = [i*2 for i in l1]
#print(l3)
