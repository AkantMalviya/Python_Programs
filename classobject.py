class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def output(self):
        print(self.x)
        print(self.y)
        print(self.z)
    def draw(self):
        print("Draw Points")

point1 = Point(10,20,30)
point1.output()
point1.draw()
        
