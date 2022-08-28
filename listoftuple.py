list1 = []
size = int(input("Enter Size of  List : "))
print("Enter Elements >")
for i in range(size):
    a = int(input(": "))
    list1.append(a)
result = [(val,pow(val,3))for val in list1]
print("Converted List of Tuples : ", result)