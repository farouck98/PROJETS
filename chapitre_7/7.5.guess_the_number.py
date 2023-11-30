import random

def guess_number():
    y = random.randint(1, 100)
    while True:
        x = ask_input()
        if x<y:
            print("Le nombre entré est plus petit que le nombre attendu ")
        elif x>y:
            print("Le nombre entré est plus grand que le nombre attendu ")
        else:
            break
    message = "Super vous avez gagné"
    return message
def main():
    print(guess_number())

if __name__ == "__main__":
    main()