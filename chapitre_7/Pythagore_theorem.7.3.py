from math import sqrt
def main():
    x = float(input("Entrez la longueur du premier côté : " ))
    y = float(input("Entrez la longueur du second côté : " ))
    hypothenuse = sqrt(x**2 + y**2)

    print(f"l'hypothénuse est de longueure {hypothenuse}. ")

if __name__ == "__main__":
    main()