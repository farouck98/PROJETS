l = ["a", "b", "c", "d", "e"]

nl = [l[i] for i in range(0, len(l)) if i%2 == 0]
print(nl)
