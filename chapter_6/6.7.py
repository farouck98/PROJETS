e = [1, 2, 3, 5, 9]
"""e2 = []
for i in range(len(e)):
       e2.append(e[i-1])
print(e2)"""

def reverse_list(l: list):
    if l == [] or l is not None:
       for i in range(len(l)):
            return [l[len(l) - i -1]for i in range(len(l))]
    else:
        return None
print(reverse_list(e))
