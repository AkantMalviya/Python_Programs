sentence = input("Enter strings lines :")
list1 = sentence.split()
file1 = open("newfile.txt",'w')
print(list1)
for i in range(len(list1)):
    if i%2==0:
        str = list1[i]+" "
        file1.write(str)
    else :
        pass
file1.close()
file1 = open("newfile.txt","r")
content = file1.read()
file1.close()
print("Content of File : ",content)