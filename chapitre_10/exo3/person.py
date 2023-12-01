
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"My name is {self.name} and I'm {self.age} years old")
