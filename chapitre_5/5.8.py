demo_list = [1, 2, 2, 3, 4, 5, 4, 2]
new_list = []

for i in set(demo_list):
    if demo_list.count(i) > 1:
        new_list.append(i)
print(new_list)
