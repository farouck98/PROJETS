class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"My name is {self.name} and I'm {self.age} years old")

class Student(Person):
    def __init__(self, name:str, age:int, student_id:int, student_topic: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.student_topic = student_topic
    def display_info(self):
       super().display_info()
       print(f"my student_id is {self.student_id} "
              f"and I study {self.student_topic}")

p1 = Person("Alice", 21)
p1.display_info()

st1 = Student("Farouck", "25", 105650, "3ALG")
st1.display_info()