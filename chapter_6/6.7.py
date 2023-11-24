e = [1, 2, 3, 5, 9]
"""e2 = []
for i in range(len(e)):
       e2.append(e[i-1])
print(e2)"""

def reverse_list(l: list):
    """l = l[::-1]
    return l"""
    new_list = []
    if l == [] or l is not None:
        for i in range(len(l)-1, -1, -1):
            new_list.append(l[i])
        return new_list
    else:
        return None
print(reverse_list(e))
