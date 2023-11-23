demo_list = [5, 1, 59, 42, 8, 3, 15, 9, 7]
first_index = demo_list[0]
nl = []
for i in range(len(demo_list)):
    if first_index < demo_list[i]:
        first_index = demo_list[i]
        nl.append(first_index)
        print(nl)