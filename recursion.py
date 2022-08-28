def fact(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * fact(x - 1)


if __name__ == "__main__":
    print(fact(5))
