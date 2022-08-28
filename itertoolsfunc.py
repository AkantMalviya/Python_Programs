from itertools import count, repeat, cycle, accumulate, takewhile, product, permutations
# some useful function from itertools module
# used in functional programming in python
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

letters = ("A", "B","C")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
a = {1,2}
print((list(product(range(3),a))))