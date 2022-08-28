class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


if __name__ == "__main__":
    spam = SpecialString("spam")
    Hello = SpecialString("Hello world!")
    print(spam / Hello)
