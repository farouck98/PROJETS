class Cat:
    def __init__(self, name:str, age:int, color:str, is_lazy: bool):
        self.name = name
        self.age = age
        self.color = color
        self.is_lazy = is_lazy

cat1 = Cat("boubou", 8, "Orange", False)
print(f"{cat1.name}\n{cat1.age}\n{cat1.color}\n{cat1.is_lazy}")

