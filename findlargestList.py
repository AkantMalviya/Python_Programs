print("\t<Find Largest in List>")
list1 = list()
size = int(input("Enter Size of list : "))
for i in range(size):
    el  = int(input("Enter Element : "))
    list1.append(el)
max = -1
print(list1)
for i in range(size):
    if list1[i]>max:
        max = list1[i]
print("Largest : ",max)


