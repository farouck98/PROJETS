
def divide():
    x = float(input("Enter a first number (x): "))
    y = float(input("Enter a second number(y) "))

    while True:
         try:
            division = x/y
            print(division)

         except ZeroDivisionError:

            print("Please enter another number y : 2")
            y = float(input("Enter a second number "))
            division = x/y
            print(division)
         break
def main():
    print(divide())

if __name__ == "__main__":
    divide()
