size = int(input("Enter the size of the list :"))
list1 = list()
for i in range(size):
    a = input("Enter Element : ")
    list1.append(a)
print("Entered List :\n",list1)
#print("Reversed List :\n ",list1[::-1])
list1.reverse()
print("Reversed List :\n ",list1)