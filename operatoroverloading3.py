# we have magic methods for comparisions operators also
# __lt__ <, __gt__ >, __le__ <=, __ge__ >=, __eq__ ==,__ne__ !=,
'''
There are several magic methods for making classes act like containers.
__len__ for len
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (In for loops)
__contain__ magic method acts like in operator
'''
import random
class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


spam = SpecialString("spam")
eggs = SpecialString("eggs")


# spam > eggs
# As you can see , you can define any custom behavior for the overloaded operators

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-2, 2)]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)


vaguelist = VagueList(["A", "B", "C", "D", "E"])
print(len(vaguelist))
print(vaguelist[2])