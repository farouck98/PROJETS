print("This is not a loop")
end = False
while not end:
    user = input("Voulez-vous continuer à voir ce message Y/N ? :")
    if user.upper() == "Y":
        print("This is not a loop")
    elif user.upper() == "N":
        print("GoodBye")
        break
    else:
        print('Type Y or N')
