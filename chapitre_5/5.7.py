demo_list = [4, 85, 6, 45, 85, 1, 2, 5, 1, -5, 96, -4, 58, 14, 23, 6, 7, 58, 85]
memory = []

for i in demo_list:
    if i not in memory:
        memory.append(i)
print(memory)

