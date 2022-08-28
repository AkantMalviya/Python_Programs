print("<\tSum Of Dictionary Values>\n")
size = int(input("Enter Size of Dictionary : "))
dict1 = dict()
for i in range(size):
    k = str(input("Key : "))
    v = int(input("Value : ")) 
    dict1[k] = v 
sum = 0
for i in dict1.values():
    sum+=i
print("Entered Dictionary :\n",dict1)
print("Sum of Values : ",sum)
