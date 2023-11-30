def main():
         c = float(input("Entrez le capital initial: "))
         r = float(input("Entrez le taux d'intérêt: "))
         n = int(input("Entrez la durée de l'investissement: "))

         if r>100:
            raise ValueError("le taux d'intérêt est supérieur à 100%")

         print(f"Le capital final est de {c*(1+r/100)**n}")


if __name__ == "__main__":
    main()