demo_list = [4, 85, 6, 45, 85, 1, 2, 5, 1, -5, 96, -4, 58, 14, 23, 6, 7, 58, 85]

unique_set = set(demo_list)
new_list = []


for i in unique_set:
    if demo_list.count(i) >  1:
        new_list.append(i)
print(new_list)