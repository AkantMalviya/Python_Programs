"""
Program to swap element position in a given list
"""
size = int(input("Enter the size of the list:"))
print("Enter Elements >")
list1 = list()
for i in range(size):
    a = int(input(":"))
    list1.append(a)
print(list1)
pos1 = int(input("position1 = "))
pos2 = int(input("position2 = "))
list1[pos1 - 1], list1[pos2 - 1] = list1[pos2 - 1], list1[pos1 - 1]
print("swapped list : ")
print(list1)
