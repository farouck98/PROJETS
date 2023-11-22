metre = input("Entrez votre hauteur en metre (m) :")
poids = input("Entrez votre poids en (kg) : ")
result = float(poids) / float(metre)**2
result = round(result,2)

print(f"Your BMI is {result}")
