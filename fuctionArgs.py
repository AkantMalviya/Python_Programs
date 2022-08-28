"""
Function Arguments *args , **kwargs
"""


def function(named_arg, *args):
    print(named_arg)
    print(args)


function("Function", 2, 3, 4, 5, 6, 7, 8)


def function2(x, y, food="spam"):
    print(food, x, y)


# default argument must be the last argument of the function
function2(2, 3)
function(2, 3, "egg")


def my_func(x, y=7, *args, **kwargs):
    print(x)
    print(y)
    print(args)
    print(kwargs)


my_func(10, 2, 3, 4, 5, 6, a=20, b=30, c=40)
