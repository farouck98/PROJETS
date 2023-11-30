def main():
    while True:
         try:
            x = float(input("Enter a valid number "))
            float_number = float(x)
            print(x)
            break
         except ValueError:
             continue

if __name__ == "__main__":
    main()