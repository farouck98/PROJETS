
from dataclasses import dataclass
@dataclass
class Cat():
    name: str
    age: int
    color: str
    is_lazy:bool

obiwan = Cat("farouck", 25, "Blue", False)
print(obiwan)

