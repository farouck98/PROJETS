l = [1, 1, 2, 2, 3, 3]
"""l2 = []
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)"""

def removing_duplicates(l1: list):
    l2 = []
    for i in l1:
        if i not in l2:
           l2.append(i)
    return l2

print(removing_duplicates(l))
