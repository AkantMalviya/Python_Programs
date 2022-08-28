"""
Program to calculate sum of cubes of n natural numbers
"""
print("\t<Sum of Cubes of n Natural number>")
num = int(input("Enter a number : "))
sum1 = 0
for i in range(1, num + 1):
    cub = i ** 3
    print(f"{cub} + ", end="")
    sum1 += cub
print("=", sum1)
