def decor2(func):
    def wrap():
        print("***************")
        func()
        print("***************")
    return  wrap


def decor(func):
    def wrap():
        print("===============")
        func()
        print("===============")
    return wrap


@decor
@decor2
def print_text():
    print("Hello World")


print_text() # 1 way to call decorator

# decorated = decor(print_text) # 2 way to call decorator
# decorated()