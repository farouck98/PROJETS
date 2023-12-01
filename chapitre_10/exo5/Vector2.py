class Vector2:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector of coordinates ({self.x}, {self.y})."

if __name__ == "__main__":
    vec1 = Vector2(4, 5)
    vec2 = Vector2(6, 5)
    print(f"{vec1 + vec2 = }")
    print(f"{vec1 - vec2 = }")