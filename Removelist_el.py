print("<Remove Nth Occurrence of Given Word>")
size = int(input("Enter size of the list :"))
list1 = list()
for i in range(size):
    el = input("Enter String Elements : ")
    list1.append(el)
print(list1)
word = str(input("Word : "))
N = int(input("Nth Occurence : "))
count=0
for i in range(size):
    if(word==list1[i]):
        count+=1
        if count == N:
            list1.pop(i)
            
print("New List : ")
print(list1)
    