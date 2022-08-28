import re

str1 = "Please contact info@sololearn.com for assistance"
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
match = re.search(pattern, str1)
print("Email : ", end="")
if match:
    print(match.group())