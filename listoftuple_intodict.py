from typing import Sized


print("\t<Coverting List of Tuple into Dictionary>\n")
listoftup = [("akash", 10), ("gaurav", 12), ("anand", 14),
("suraj", 20), ("akhil", 25), ("ashish", 30)]
dict1 = dict()
for i , j in listoftup:
    dict1[i] = j
print(dict1)