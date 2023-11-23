l1 = []
def max(l):
    if len(l) == 0 or l is None:
        return None
    else:
        max_index = l[0]
        for i in range(len(l)):
            if max_index < l[i]:
                max_index = l[i]
        return max_index

def min(l):
    if len(l) == 0 or l is None:
       return None
    else:
        min_index = l[0]
        for i in range(len(l)):
            if min_index > l[i]:
                min_index = l[i]
        return min_index

print(min(l1))
print(max(l1))
