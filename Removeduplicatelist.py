list1 = [2,23,4,1,3,2,2,0]
lsit2 = []
for el in list1:
    if el not in lsit2:
        lsit2.append(el)
    else :
         pass
print("Duplicates Removed :")
print(lsit2)