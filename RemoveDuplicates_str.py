str = input("Enter a string : ")
empty = ""
for i in str:
    if i in empty:
        pass
    else:
        empty= empty+i
print("<Remove String Duplicates With Order>\n: ",empty)