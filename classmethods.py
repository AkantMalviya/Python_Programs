class Rectangle:
    def __init__(self,height,width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    @classmethod
    def square(cls,side_length):
        return cls(side_length,side_length)

if __name__ == "__main__":
    rect1 = Rectangle(10,20)
    print(rect1.area())
    sqr1 = Rectangle.square(5)
    print(sqr1.area())