class Mammel:
    def walk(self):
        print("walking")

class Dog(Mammel):
    def bark(self):
        print("Dog Barking")

class Cat(Mammel):
    def mew(self):
        print("Cat Mewing")
    
dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.mew()