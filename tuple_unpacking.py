"""
Program to demonstrate packing and unpacking of list and tuples
"""
numbers = (1, 2, 3)
a, b, c = numbers
print(a, b, c)
a, b = b, a
print(a, b)

d, e, *f, g = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(d)
print(e)
print(f)
print(g)

# *f means that variable takes all the left values from a list or a tuple
