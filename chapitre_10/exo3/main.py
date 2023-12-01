from person import Person
from student import Student

def main():

        p1 = Person("Alice", 21)
        p1.display_info()

        st1 = Student("Farouck", "25", 105650, "3ALG")
        st1.display_info()

if __name__ == "__main__":
    main()