from person import Person
class Student(Person):
    def __init__(self, name:str, age:int, student_id:int, student_topic: str):
        super().__init__(name, age)
        self.student_id = student_id
        self.student_topic = student_topic
    def display_info(self):
       super().display_info()
       print(f"my student_id is {self.student_id} "
              f"and I study {self.student_topic}")