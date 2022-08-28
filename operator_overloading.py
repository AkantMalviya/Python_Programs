class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # magic methods or operator overloading
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __mod__(self, other):
        return Vector2D(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return Vector2D(self.x ** other.x, self.y ** other.y)

# or | and & xor ^ more methods are their for this operations


if __name__ == "__main__":
    vector1 = Vector2D(10, 20)
    vector2 = Vector2D(10, 20)
    vector3 = vector1 + vector2
    print("Addition ",vector3.x, vector3.y)
    vector3 = vector1 - vector2
    print("Substraction ",vector3.x, vector3.y)
    vector3 = vector1 * vector2
    print("Multiplication ",vector3.x, vector3.y)
    vector3 = vector1 / vector2
    print("Division ",vector3.x, vector3.y)
    vector3 = vector1 % vector2
    print("Modules ",vector3.x, vector3.y)
    vector3 = vector1 ** vector2
    print("Exponentiation ",vector3.x, vector3.y)
