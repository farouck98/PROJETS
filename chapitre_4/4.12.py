nbr = int(input('Entrez un nombre : '))
if nbr < 0:
    nbr = nbr * -1

for i in range(1, nbr+1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"FizzBuzz")
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print(f"Buzz")
    else:
        print(i)
