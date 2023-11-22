l = [5, 1, 3, -2, 8]

first_index = l[0]
nl = []

for i in l:
    if i < l[0:4] :
        nl.append(i)
print(nl)
