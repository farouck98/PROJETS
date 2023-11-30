try:
    raise ValueError("Ceci est une erreur.")
except ValueError as e:
    print(str(e))