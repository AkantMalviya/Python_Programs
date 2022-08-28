print("\t<Check String Contains Unique Element Or Duplicates>")
str = input("Enter a string : ")
count = 0 
for i in range(len(str)): 
    for j in range(i+1,len(str)):
        if str[j] == str[i]:
            count+=1
        else :
            pass    
if count == 0:
    print(f"UniQue {count} (Duplicates)")
else:
    print(f"False {count} (Duplicates)")
                