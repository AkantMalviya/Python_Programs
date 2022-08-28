"""
Program to calculate sum of square of n natural numbers
"""
print("\t<Sum of squares of n Natural number>")
num = int(input("Enter a number : "))
sum1 = 0
for i in range(1, num + 1):
    sqr = i ** 2
    print(f"{sqr} + ", end="")
    sum1 += sqr
print("=", sum1)
