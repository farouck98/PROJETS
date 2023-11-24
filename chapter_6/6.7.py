e = ["quatre", "cinq", 4, 7]
"""e2 = []
for i in range(len(e)):
       e2.append(e[i-1])
print(e2)"""

def reverse_list(l: list):
       for i in range(len(l)):
            return [l[len(l) - i -1]for i in range(len(l))]
print(reverse_list(e))
