# generator function
def countdown():
    i = 5
    while i > 0:
        yield i  # yield define generator variable
        i -= 1


for i in countdown():
    print(i)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i  # yield similar to  return statement


print("Even Numbers")
print(list(numbers(11)))
