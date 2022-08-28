import re

# their are several important methods in regular expression module
# match, search, findall, finditer
# suppose match is an object of re class so you can use method such as group , start , end , span for the object

pattern = r"spam"
print(pattern)

if re.match(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

if re.search(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

match = re.search(pattern, "eggspamsausagespam")

if re.findall(pattern, "eggspamsausagespam"):
    print("Match")
else:
    print("No Match")

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())

str1 = "My name is Akant, Hi Akant"
pattern = r"Akant"
newstr = re.sub(pattern, "Alex", str1) #search and replace
print(newstr)
str2 = r"I am \r\a\w!"
print(str2)