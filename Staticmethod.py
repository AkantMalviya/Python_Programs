'''
for creating static method in class use @staticmethod decorator
for creating property method in class use @property decorator
properties can also be define or set by setter and getter functions
setter set the property value and getter gets the value
created by simply property name followed by a dot and the setter or getter keyword
'''
class Pizza:
    def __init__(self,topping):
        self.toppings = topping

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError
        else :
            return True

    @property
    def pineapple_allowed(self):
        return False

    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password = input("Enter the password")
            if password == "Akant@2000":
                self.pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


if __name__ == "__main__":
    ingredients = ["apple","banana","mango"]
    if all(Pizza.validate_topping(i) for i in ingredients):
        pizza = Pizza(ingredients)

    print(pizza.pineapple_allowed)
    # pizza.pinapple_allowed = True # show an attribute error bcz you can not use it outside of the class
    # here pineapple becomes an attribute of class ,and we can use it as a normal variable because of property method
    # that means pizza object is created via a static method that becomes true for every conditions
    # because there is no pineapples in ingredients list

    pizza.pineapple_allowed = True
    print(pizza.pineapple_allowed)