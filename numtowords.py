phone = input("Enter Digits :")
num_mapping = {"1":"One","2":"Two","3":"Three","4":"Four"}
output = ""
for ch in phone:
    output += num_mapping.get(ch,"!") + " "
print(output)