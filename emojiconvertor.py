msg = input("Enter message : ")
lst = msg.split(" ")
emojis  = {":)":"đ" , 
":(":"âšī¸" }
output = ""
for ch in lst:
    output += emojis.get(ch,ch)+ " "
print(output)