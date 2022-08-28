"""
Two types of access specifier to hide data in python
1. _ single underscore infront of class attributes and methods (Private specifier)
2. __ double underscore infront of class attributes and methods (Strongly Private specifier)
"""
'''
__repr__ is a magic method for string representation of an instance of class
'''


class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

class Spam:
    __egg = 7
    def print(self):
        print(self.__egg)

if __name__ == "__main__":
    que1 = Queue([1, 2, 3])
    print(que1)
    que1.push(4)
    print(que1)
    print(que1.pop())
    print(que1._hiddenlist)
    s= Spam()
    s.print()
    print(s._Spam__egg) # we can use strongly private attributes by this syntex
    # print(s.__egg) because it is strongly private attribute

