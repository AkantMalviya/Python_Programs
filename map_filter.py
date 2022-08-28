#functional programming
#high order function which takes another function as an argument
def apply_twice(func,arg):
    return func(func(arg))

def addfive(x):
    return x+5
#map function
nums = [11,22,33,44,55]
result = list(map(addfive,nums))
print(result)
#lambda keywords
result = list(map(lambda x:x+5,nums))
print(result)
#filter function
result = list(filter(lambda x:x%2==0,nums))
print(result)

print(apply_twice(addfive,10))