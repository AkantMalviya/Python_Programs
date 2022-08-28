"""
Program to Accept String that contains only vowels
"""
print("\t<String Containing All The Vowels>")
str1 = input("Enter a string : ")
str1.lower()
vow = ["a", "e", "i", "o", "u"]
list1 = list()
count = 0
for i in vow:
    if i in str1:
        count += 1
    else:
        list1.append(i)
if (count == 5):
    print("\tYes ! Accepted")
    print("\tAll vowels are presented")
else:
    print("\tNot Accepted")
    print(list1, "Are not present")
