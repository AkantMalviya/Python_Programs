class Area:
    def area1(self):
        aor = self.length * self.bredth
        return aor
    
class Area2(Area):
    def __init__(self,length,bredth,height):
        self.length = length
        self.bredth = bredth
        self.height = height
    def area2(self):
        aot = (0.5*self.length*self.bredth)
        return aot
    def volume(self):
        volofrec = self.length*self.bredth*self.height
        return volofrec


obj1 = Area2(10,20,30)
print(obj1.area1())
print(obj1.area2())
print(obj1.volume())

        
