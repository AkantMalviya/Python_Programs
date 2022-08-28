sentence = input("Enter a sentence :")
list1 = sentence.split()
print("Even Length Words Are : ")
for word in list1:
    if len(word)%2==0:
        print(word,end=" ")