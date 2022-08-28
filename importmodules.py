import utilites
l = int(input("Enter length of list : "))
list1 = list()
for i in range(l):
    el = int(input("Enter Element : "))
    list1.append(el)

print("Entered list", list1)
max = utilites.find_max(list1)
print(f"Maximum : {max}")