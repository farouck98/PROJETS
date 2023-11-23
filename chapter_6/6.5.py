l1 = []
def max(l):
    if len(l) != 0:
        max_index = l[0]
        for i in range(len(l)):
           if max_index < l[i]:
              max_index = l[i]
        print(max_index)
    else:
        print("None")

def min(l):
    if len(l) !=0:
        min_index = l[0]
        for i in range(len(l)):
            if min_index > l[i]:
                min_index = l[i]
        print(min_index)
    else:
        print("None")
    return 0
min(l1),max(l1)
