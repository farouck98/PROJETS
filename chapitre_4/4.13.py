for i in range(1,  11):
    for j in range(1, 11):
        n = i*j
        if n < 10:
            print(f"0{n}", end=" ")
        else:
            print(n, end=" ")
    print()

