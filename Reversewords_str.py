sentence = input("Enter a sentence \n:")
list1 = sentence.split()
list1.reverse()
print("Reversed words of Strings :")
for word in list1:
    print(word,end=" ")