"""
Program to Interchange First and Last Element of the Given List
"""
print("< Interchange First and Last Element of the List >")
list1 = list()
len1 = int(input("Enter size of list : "))
for i in range(len1):
    list1.append(input("Enter Elements : "))
print("Entered List : ")
print(list1)
print("Interchanged List : ")
list1[0], list1[-1] = list1[-1], list1[0]
print(list1)
